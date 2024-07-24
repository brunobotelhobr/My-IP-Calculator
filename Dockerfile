FROM python:alpine3.20

# Update the system
RUN apk update && apk upgrade

# Create User
RUN mkdir /code
RUN adduser -D -h /code -s /bin/bash app 

# install gcc
RUN apk update && apk add python3-dev gcc libc-dev libffi-dev

# Install dependencies
RUN pip install --upgrade pip
RUN pip install setuptools
RUN pip install wheel
RUN pip install poetry

# Install the package
WORKDIR /code
COPY src src
COPY pyproject.toml /code/pyproject.toml
COPY README.md /code/README.md

# Install the packages
# Disable virtualenvs creation
RUN poetry config virtualenvs.create false
RUN poetry install --without dev,docs

# Adjust Permissions
RUN chown -R app:app /code/*

#Enable app User
USER app

HEALTHCHECK --interval=30s --timeout=3s \
    CMD python /code/src/app/cmd.py version || exit 1

# # Define the entrypoint
ENTRYPOINT ["python", "/code/src/app/cmd.py"]