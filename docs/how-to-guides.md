## How Contribute

To Start Contributing, you must follow the steps below:

## 1. Fork the project
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

## 2. Create a new branch with your changes
```shell
# Create a new branch
git checkout -b <branch-name>
```

## 3. Make the changes and commit
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

## 4. Open a Pull Request
```shell
git commit -m "feat: add a new feature"
git push origin <branch-name>
```

