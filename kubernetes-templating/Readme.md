0) Created manageable GKE k8s cluster with Istio
1) Installed helm3
2) Added stable, jetstack, harbor repos into helm
2.1) Created corresponded namespaces
3) Install nginx ingress for cluster access outside by helm
4) Install cert-manager for certificates issuing by helm
5) Install chartmuseum with customed values:
* Added ingress annotations
* Added tls annotations - pay attention to cert-man resources API versions!
* Added Certmanager Let's Encrypt ClusterIssuer - staging and Prod
ingress:
  enabled: true
  annotations:
    kubernetes.io/ingress.class: nginx
    kubernetes.io/tls-acme: "true"
    cert-manager.io/cluster-issuer: letsencrypt-prod
    cert-manager.io/acme-challenge-type: http01
  hosts:
    - name: chartmuseum.35.228.114.10.nip.io
      path: /
      tls: true
      tlsSecret: chartmuseum.35.228.114.10.nip.io
6) Install harbor with customed values
expose:
  type: ingress
  tls:
    enabled: true
    commonName: "harbor.35.228.114.10.nip.io"
  ingress:
    hosts:
      core: harbor.35.228.114.10.nip.io
    # set to the type of ingress controller if it has specific requirements.
    # leave as `default` for most ingress controllers.
    # set to `gce` if using the GCE ingress controller
    # set to `ncp` if using the NCP (NSX-T Container Plugin) ingress controller
    controller: default
    annotations:
      nginx.ingress.kubernetes.io/ssl-redirect: "true"
      kubernetes.io/ingress.class: nginx
      kubernetes.io/tls-acme: "true"
      cert-manager.io/cluster-issuer: letsencrypt-prod
      cert-manager.io/acme-challenge-type: http01
externalURL: https://harbor.35.228.114.10.nip.io
imagePullPolicy: IfNotPresent
updateStrategy:
  type: RollingUpdate
logLevel: debug
harborAdminPassword: "n0tWE@kH@ZBO#r"
trivy:
  enabled: false
notary:
  enabled: false
7) Create helmfile.yaml which described components desired state
Describing enviroments configuration
Added repo, releases, other config: https://github.com/roboll/helmfile/tree/v0.92.1
helmfile is a little bit templated
