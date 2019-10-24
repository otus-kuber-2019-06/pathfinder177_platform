hw-10 kubernetes-templating

Working with chartmuseum

1) Add the chartmuseum to helm repo list
helm repo add chartmuseum http://localhost:8080/

2) Upload a new chart to cm as a binary
First create mychart-0.1.0.tgz using the Helm CLI:

cd mychart/
helm package .

Upload mychart-0.1.0.tgz:

curl --data-binary "@mychart-0.1.0.tgz" http://localhost:8080/api/charts

If you’ve signed your package and generated a provenance file, upload it with:

curl --data-binary "@mychart-0.1.0.tgz.prov" http://localhost:8080/api/prov

Both files can also be uploaded at once (or one at a time) on the /api/charts route using the multipart/form-data format:

curl -F "chart=@mychart-0.1.0.tgz" -F "prov=@mychart-0.1.0.tgz.prov" http://localhost:80

3) Upload a new chart by the helm-push plugin

You can also use the helm-push plugin:

helm push mychart/ chartmuseum

4) Install a chart from cm into the kubernetes
helm install chartmuseum/mychart
