import kopf
import yaml
import kubernetes
import time
from jinja2 import Environment, FileSystemLoader

def render_template(filename, vars_dict):
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template(filename)
    yaml_manifest = template.render(vars_dict)
    json_manifest = yaml.load(yaml_manifest)
    return json_manifest

@kopf.on.create('otus.homework', 'v1', 'mysqls')
def mysql_on_create(body, spec, **kwargs):
    name = body['metadata']['name']
    image = body['spec']['image']
    password = body['spec']['password']
    database = body['spec']['database']
    storage_size = body['spec']['storage_size']
    
    persistent_volume = render_template('mysql-pv.yml.j2',{'name': name, 'storage_size': storage_size})
    persistent_volume_claim = render_template('mysql-pvc.yml.j2',{'name': name, 'storage_size': storage_size})
    service = render_template('mysql-service.yml.j2',{'name': name})
    deployment = render_template('mysql-deployment.yml.j2', {
        'name': name,
        'image': image,
        'password': password,
        'database': database})
    
    api = kubernetes.client.CoreV1Api()
    api.create_persistent.volume(persistent_volume)
    api.create_namespaced_persistent_volume_claim('default', persistent_volume_claim)
    api.create_namespaced_service('default', service)
    
    api = kubernetes.client.AppsV1Api()
    api.create_namespaced_deployment('default', deployment)