# How Install

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
# Clone the repository
git clone https://github.com/brunobotelhobr/My-Template=Python.git

# Check the python version, you must use the version that the project will use.
python -V

# Install the dependencies
pip install poetry
poetry shell
poetry install

# Check the taskipi commands:
task --list

# Update projetct metadata
task meta
```

## How Start?

### 1. Fork the project
```shell
# Clone the repository
git clone

# Check the python version, you must use the version that the project will use.
python -V

# Install the dependencies
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