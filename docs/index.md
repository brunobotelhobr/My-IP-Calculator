# Welcome to Project Documentation

![Project Logo](assets/logo.png){: width=160 .center}
# My-Python-Template

![GitHub Action CI](https://github.com/brunobotelhobr/My-Template-Python/actions/workflows/ci.yml/badge.svg?branch=main)
![GitHub Action CodeQL](https://github.com/brunobotelhobr/My-Template-Python/actions/workflows/codeql.yml/badge.svg?branch=main)
![GitHub Action Trivy](https://github.com/brunobotelhobr/My-Template-Python/actions/workflows/trivy.yml/badge.svg?branch=main)
[![codecov](https://codecov.io/gh/brunobotelhobr/My-Template-Python/branch/main/graph/badge.svg?token=EPMON2XJW2)](https://codecov.io/gh/brunobotelhobr/My-Template-Python)

This is a template repository for Python projects. 

It uses Poetry for dependency management and includes pre-configured tools such as black, flake8, mypy, pylint, pytest, and others, for formatting, linting, testing, and documentation management. 
The project also includes security tools like trivy and bandit. 

The pyproject.toml file contains various configurations like project metadata, dependencies, build system, and commands for release and documentation management.

To have more details, check the [Documentation](https://brunobotelhobr.github.io/My-Template-Python/)

## Features
- Project Management
    - ✅ [Poetry](https://python-poetry.org/docs/)
    - ✅ Script to manage project metadata (Name, Version, Description, etc)
    - ✅ Script to Upgrade all dependencies
    - ✅ Script to clean all temporary files
- Code Formatting
    - ✅ [Black](https://github.com/psf/black)
    - ✅ [isort](https://pycqa.github.io/isort/)
    - ✅ [autoflake](https://github.com/myint/autoflake)  
- Code Linting
    - ✅ [Pylint](https://www.pylint.org/)
    - ✅ [Flake8](https://flake8.pycqa.org/en/latest/)
    - ✅ [Mypy](https://mypy.readthedocs.io/en/stable/)
- Testing
    - ✅ [Pytest](https://docs.pytest.org/en/stable/)
    - ✅ [Coverage](https://coverage.readthedocs.io/en/coverage-5.5/)
    - ✅ Default tests structure folder for unit and functional tests
- Security
    - ✅ [Trivy](https://aquasecurity.github.io/trivy/v0.40/getting-started/installation/)
    - ✅ [Bandit](https://pypi.org/project/bandit/)
    - ✅ [Horusec](https://horusec.io/docs/quick-start/installation/)
- Autoamtion commands
    - ✅ [Taskipy](https://github.com/taskipy/taskipy)
- PyPI
    - ✅ Scripts to build and publish to PyPI
- Docker
    - ✅ Scripts to build and publish to Docker Hub
- Documentation
    - ✅ [MkDocs](https://www.mkdocs.org/)
    - ✅ [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)
    - ✅ [MkDocs Versioning with mike](https://github.com/jimporter/mike)
    - ✅ Scripts to generate SBOM (Software Bill of Materials)
    - ✅ Scripts to generate requirements.txt
- CI/CD
    - ✅ GitHub Actions to do CI/CD


## Tasks
This project uses [Taskipy](https://github.com/taskipy/taskipy) to automate common development tasks.

All tasks are defined in the `pypoject.toml` file.

Almost all tools used in this project uses `pyproject.toml` to store their configurations.

List of preset tasks:
````
task --list
pre-commit      Run all pre-commit tasks
pre-release     Run all pre-release tasks
-----------     ----------------------------------------
info            Show project info
meta            Update project properties
upgrade         Upgrade all dependencies
sec             Run all security checks
format          Run all formaters
lint            Run all linters
bom             Generate BOM
req             Generate requirements.txt
test            Run all tests
pypi-build      Build package for PyPI
pypi-auth       Authenticate to PyPI
pypi-pub        Publish package to PyPI
docker-list     List docker images
docker-build    Build docker image
docker-sec-scan Scan a docker image looking for vulenrabilities
docker-auth     Authenticate to Docker Hub
docker-latest   Tag a docker image as latest
docker-pub      Publish docker image to Docker Hub
docs            Run docs server
docs-list       List docs versions
docs-build      Add a new version to docs
docs-delete     Delete a version of the docs
docs-latest     Set the latest Version.
docs-purge      Purge all versions of the docs.
docs-pub        Publish documentation to the doc branch on GitHub.
clean           Clean all generated files
````

## Project Structure
````
.
├── Dockerfile
├── README.md
├── docs
│   ├── assets
│   │   └── logo.png
│   ├── code.md
│   ├── css
│   │   └── extra.css
│   ├── faq.md
│   ├── how-to-guides.md
│   ├── index.md
│   ├── install.md
│   ├── manual.md
│   └── overwrites
│       └── main.html
├── meta
│   ├── bom
│   │   ├── bom.json
│   │   └── bom.xml
│   └── requirements
│       ├── requirements-dev.txt
│       └── requirements.txt
├── mkdocs.yml
├── poetry.lock
├── pyproject.toml
├── scripts
│   ├── update-doc.py
│   └── update-project-properties.py
├── src
│   └── app
│       ├── __init__.py
│       ├── calc.py
│       └── main.py
└── tests
    ├── __init__.py
    ├── funcional
    │   └── __init__.py
    ├── integral
    │   └── __init__.py
    └── unity
        ├── __init__.py
        ├── calc_test.py
````
## Requirements
You must install manually the following tools:

- Install [Python](https://www.python.org/downloads/)
- Install [Poetry](https://python-poetry.org/docs/#installation)
- Install [Trivy](https://aquasecurity.github.io/trivy/v0.40/getting-started/installation/)
- Install [Horusec](https://horusec.io/docs/quick-start/installation/)
- Install [Docker](https://docs.docker.com/get-docker/)

Be sure you have installed all the requirements and that you on the desired python Version, you can check it with: 
    `python --version`

## Setup
```shell
# Clone the repository:
git clone https://github.com/brunobotelhobr/My-Template=Python.git

# Check the python version, you must use the version that the project will use:
python -V

# Install the dependencies:
pip install poetry
poetry shell
poetry install

# Check the taskipi commands:
task --list

# Update projetct metadata:
task meta
```

## How Start?

### 1. Fork the project
```shell
# Clone the repository:
git clone

# Check the python version, you must use the version that the project will use:
python -V

# Install the dependencies:
pip install poetry
poetry shell
poetry install

# Check the taskipi commands:
task --list
```

### 2. Create a new branch with your changes
```shell
# Create a new branch
git checkout -b <branch-name>
```

### 3. Make the changes and commit
```shell
# Check for lint errors
task format
task lint

# Check for security errors
task sec

# Update the meta
task meta
task bom
task req

# Add the changes
git add .
```

### 4. Open a Pull Request
```shell
git commit -m "feat: add a new feature"
git push origin <branch-name>
```

## Hints
- How add a Dev Package
   -  `poetry add --dev <package-name>`
- How add a Prod Package
    - `poetry add <package-name>`
- How add a Package with extras
    - `poetry add <package-name> -E <extras>`
- How remove a Package
    - `poetry remove <package-name>`

## Call for Contributors
We invite you to contribute to this repository and help us make it even better. 
Whether it's bug fixes, new features, or documentation improvements, we welcome all contributions. 
Please read our documentation for guidelines on how to contribute. 

Check [How to Contribute](how-to-guides.md)
Happy coding!

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/brunobotelhobr)
