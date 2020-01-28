# Car API sample project

This is a Car API sample application written in Python.

## Swagger API Definition

Please execute the following commands to run the Editor in your local machine from Docker.

```
docker pull swaggerapi/swagger-editor
docker run -p 8085:8080 -e SWAGGER_JSON=/tmp/swagger.yml -v `pwd`:/tmp swaggerapi/swagger-ui
```

This will run Swagger Editor (in detached mode) on port 8085 on your machine, so you can open it by navigating to [http://localhost:8085](http://localhost:8085) in your browser.

## Docker

For learning purpose, you need to install Docker Community Edition. Select your OS from the list below and follow the setup instructions.

- [Mac OS](https://docs.docker.com/docker-for-mac/install/)
- [Windows](https://docs.docker.com/docker-for-windows/install/)
- [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [Debian](https://docs.docker.com/install/linux/docker-ce/debian/)
- [CentOS](https://docs.docker.com/install/linux/docker-ce/centos/)
- [Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/)
