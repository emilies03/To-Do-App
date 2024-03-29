# DevOps Apprenticeship: Project Exercise

This project creates a To Do flask app. The to do app is hosted on Azure [here](http://test-em-todoapp.azurewebsites.net/).
Tasks are stored in a Azure Cosmos DB which is encrypted at rest by default.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change).

There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

The database name and connection string will also need to be added. To log to Loggly, the LOGGLY_TOKEN has to be added.

### Dependency Checking

Safety if used to check for vulnerabilities. This is done in the pipeline part of the `Build and Test` step.

To check vulnerabilities locally:
```bash
$ poetry run safety check
```

## Running the App

### Development mode
Once the all dependencies have been installed, you can start the flask app

#### Running code locally
start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

#### Developer mode docker container

##### Getting the Docker Image
You can either build the docker image locally or pull it from DockerHub

To build the docker image run
`docker build --target developer --tag todo-app:dev .`

The Docker Image is deployed on DockerHub here: https://hub.docker.com/repository/docker/emilie03/todo-app/general
To download a the image run
`docker pull emilie03/todo-app:prod`

##### Running the docker container

To run docker container run the following, where `<DESKTOP-ROUTE>` is the file path to the code e.g. `C:\Dev Ops\To Do App\DevOps-Course-Starter`
` docker run -d -p 8080:5000 --env-file .env --mount 'type=bind,source=<DESKTOP-ROUTE>\todo_app\,target=/app/todo_app/' todo-app:dev`
Then you can go to http://localhost:8080/ to view the app

### Production mode docker container
To create the docker image run
`docker build --target production --tag todo-app:prod .`
To run docker container run
`docker run -p 8080:8000 --env-file .env todo-app:prod`
Then you can go to http://localhost:8080/ to view the app

## Running Tests

To run the test suite in VS code, you need to set up the virtual environment. Press `Cmd/Ctrl + Shift + P` and select `Python: Select Interpreter`. Select the Python executable in the new `.venv` directory, which is `./.venv/Scripts/python.exe` on Windows.

To run the tests (integration and unit), use the command `poetry run pytest tests` in the DevOps-Course-Starter directory. This will search the "tests" directory for files starting in `test_` or ending in `_test`. Inside those files, any function starting with `test_` will be considered a test.

### Running tests in Docker container

To create the docker image run
`docker build --target test --tag todo-app:test .`
To run docker container run
`docker run todo-app:test`

## To run To Do App on managed nodes

Copy the contents of the `Ansible` repository to the control node

On the control node run `ansible-playbook my-ansible-playbook.yml -i my-ansible-inventory`, you should then see the app running on port 80 of the managed node e.g. go to http://18.170.89.124

## Logging

Loggly is used to log the app at this [`subdomain`](https://emtodoapp.loggly.com/).
If the `LOGGLY_TOKEN` is not set, the app will only log to console.

To update the logging level, change the `LOG_LEVEL` variable in the `.env` file.

## Terraform

Infrastructure is defined using Terraform in the `/infrastructure` directory. The terrform state files are stored in Azure Storage Account.
The Azure Storage Account is not tracked in Terraform and must be created manually on project set up.

### Pipeline infrastructure changes

Terraform changes are implemented in the pipeline on the `main` branch.
For this you must provide a Servie Principal (`ARM_CLIENT_ID`, `ARM_CLIENT_SECRET`, `ARM_TENANT_ID` and `ARM_SUBSCRIPTION_ID`) secrets in the pipeline. 

### Applying changes locally

All Terraform changes should be implemented in the pipeline, however you can run terraform commands locally.
You must first navigate to the infrastructure directory.
```bash
$ cd infrastructure
$ terraform plan
$ terraform apply
```