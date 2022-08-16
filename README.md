# flask-gunicorn
flask gunicorn hello world

$ docker build -f Dockerfile -t flask/hello-world .
$ docker run -p 8000:8000 flask/hello-world &

$ kubectl run hello-world --image=flask/hello-world:v1 -- port=8000
$ kubectl expose deployment hello-world --type=NodePort

Reference: https://betterprogramming.pub/create-a-running-docker-container-with-gunicorn-and-flask-dcd98fddb8e0