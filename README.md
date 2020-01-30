# Car API sample project

This is a Car API sample application written in Python.

## Environment

As a dependency manager for this project we are using [Pipenv](https://pipenv.readthedocs.io/en/latest/). To install it, please check [this](https://pipenv.kennethreitz.org/en/latest/install/#installing-pipenv) link. To check that Pipenv is installed just run:

```
$ pipenv --version
```

### Install dependencies

To create a new python virtual environment and install all the neccessay dependencies there, just run the following command:

```
$ pipenv install
```

To activate this project's virtualenv, run `pipenv shell`. If you want to desactivate the virtualenv, just perform `deactivate`. Pipenv creates all your virtual environments in a default location.

## Run the project

To run the project locally we can run the following command:

```
$ pipenv run python app.py
```

Then, your Flask docker server instance will be running on [http://localhost:5000](http://localhost:5000).

## Makefile commands

There is a [Makefile](https://www.gnu.org/software/make/manual/make.html#toc-An-Introduction-to-Makefiles) that provide us an easy way to run different action around the project. You just need to run:

```
$ make <action>
```

All the supported actions are (you can see the list running `$ make help`):

| Action      | Description                                              |
| :---------- | :------------------------------------------------------- |
| clean       | remove all build, test, coverage and Python artifacts    |
| clean-build | remove build artifacts                                   |
| clean-pyc   | remove Python file artifacts                             |
| clean-test  | remove test and coverage artifacts                       |
| lint        | check style with flake8                                  |
| test        | run tests quickly with the default Python                |
| test-all    | run tests on every Python version with tox               |
| coverage    | check code coverage quickly with the default Python      |
| docs        | generate Sphinx HTML documentation, including API docs   |
| servedocs   | compile the docs watching for changes                    |
| release     | package and upload a release                             |
| dist        | builds source and wheel package                          |
| install     | install the package to the active Python's site-packages |
| develop     | install the package as develop                           |
| uninstall   | uninstall the package                                    |

## Swagger API Definition

Please execute the following commands to run the Editor in your local machine from Docker.

```
$ docker pull swaggerapi/swagger-editor
$ docker run -p 8085:8080 -e SWAGGER_JSON=/tmp/swagger.yml -v `pwd`:/tmp swaggerapi/swagger-ui
```

This will run Swagger Editor (in detached mode) on port 8085 on your machine, so you can open it by navigating to [http://localhost:8085](http://localhost:8085) in your browser.

![header image](https://github.com/fgriberi/car-api/blob/2-add-swagger-api/resources/swagger.png)

## Docker

For learning purpose, you need to install Docker Community Edition. Select your OS from the list below and follow the setup instructions.

-   [Mac OS](https://docs.docker.com/docker-for-mac/install/)
-   [Windows](https://docs.docker.com/docker-for-windows/install/)
-   [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
-   [Debian](https://docs.docker.com/install/linux/docker-ce/debian/)
-   [CentOS](https://docs.docker.com/install/linux/docker-ce/centos/)
-   [Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/)

## TODO's

-   setup Travis integration
