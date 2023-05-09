# FAQ

## How use the documentation?

The documentation is made with [mkdocs](http://www.mkdocs.org/). 
It will generate a static website from the markdown files inside the docs folder.
By default, the documentation is stored in the `documentation` branch. 
If you would like to change it check at `pyproject.toml`.
````toml
[tool.taskipy.variables]
src_dir = "src"
docs_branch = "documentation"
````

To check how the documentation looks like, you can run the following command:

```bash
task docs-serve
```

To build the documentation, you can run the following command:

```bash
task docs-build
```

To list all the available documentation versions available, you can run the following command:

```bash
task docs-list
```

To delete a documentation version, you can run the following command:

```bash
task docs-delete
```

To publish the documentation, you can run the following command:

```bash
task docs-pub
```

### Warning
Dont forget to set setup git to use the documentation branch as the site branch.
To do this, on your repository, go to Settings > Options > GitHub Pages and set the branch to documentation.