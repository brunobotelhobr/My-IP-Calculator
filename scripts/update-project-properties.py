"""Do project properties update."""
import toml
import yaml

with open('pyproject.toml', 'r') as file:  # pylint: disable=w1514
    data = toml.load(file)


print("Current project properties:")
print(f"   name: {data['tool']['poetry']['name']}")
print(f"   version: {data['tool']['poetry']['version']}")
print(f"   license: {data['tool']['poetry']['license']}")
print(f"   description: {data['tool']['poetry']['description']}")
print(f"   authors: {data['tool']['poetry']['authors']}")
print(f"   maintainers: {data['tool']['poetry']['maintainers']}")
print(f"   readme: {data['tool']['poetry']['readme']}")
print(f"   packages: {data['tool']['poetry']['packages']}")
print(f"   repository: {data['tool']['poetry']['repository']}")
print(f"   homepage: {data['tool']['poetry']['homepage']}")
print(f"   keywords: {data['tool']['poetry']['keywords']}")
print(f"   docker-context: {data['tool']['taskipy']['variables']['docker_context']}")  # pylint: disable=line-too-long
print("Type new values for the project properties or press enter to keet the actual value:")  # pylint: disable=line-too-long

# Read new values
new_values = []
old_name = ""  # pylint: disable=invalid-name
new_name = ""  # pylint: disable=invalid-name
old_version = ""  # pylint: disable=invalid-name
new_version = ""  # pylint: disable=invalid-name
new_docker_context = ""  # pylint: disable=invalid-name
update = False  # pylint: disable=invalid-name

new_values = []
for key in data['tool']['poetry']:
    if key != "group" and key != "dependencies" and key != "dev-dependencies":
        value = input(f"   {key} :")
        if value != "":
            new_values.append(f"{key} = \"{value}\"")
value = input("   docker-context :")
if value != "":
    new_docker_context = value
    update = True  # pylint: disable=invalid-name

if len(new_values) > 0:
    with open('pyproject.toml', 'r+') as file:  # pylint: disable=w1514
        data_str = file.read()
        for new_value in new_values:
            data_str = data_str.replace(
                f"{new_value.split('=')[0].strip()} = \"{data['tool']['poetry'][new_value.split('=')[0].strip()]}\"", new_value)   # pylint: disable=line-too-long
            if new_value.split('=')[0].strip() == "name":
                old_name = data['tool']['poetry'][new_value.split('=')[
                    0].strip()]
                new_name = new_value.split('=')[1].strip().replace("\"", "")
                update = True
            if new_value.split('=')[0].strip() == "version":
                old_version = data['tool']['poetry'][new_value.split('=')[
                    0].strip()]
                new_version = new_value.split('=')[1].strip().replace("\"", "")
                update = True
        file.seek(0)
        file.write(data_str)
        file.truncate()


with open('pyproject.toml', 'r') as toml_file:  # pylint: disable=w1514
    tom_data = toml.load(toml_file)
    with open('mkdocs.yml', 'r+') as mkdoc_file:  # pylint: disable=w1514
        mkdoc_data = yaml.load(mkdoc_file, Loader=yaml.FullLoader)
        mkdoc_data['site_name'] = tom_data['tool']['poetry']['name']
        mkdoc_data['site_description'] = tom_data['tool']['poetry']['description']  # pylint: disable=line-too-long
        mkdoc_data['site_author'] = tom_data['tool']['poetry']['authors'][0]
        mkdoc_data['site_url'] = tom_data['tool']['poetry']['homepage']
        mkdoc_data['edit_uri'] = tom_data['tool']['poetry']['homepage'] + "/docs"   # pylint: disable=line-too-long
        mkdoc_data['repo_url'] = tom_data['tool']['poetry']['repository']
        mkdoc_data['repo_name'] = tom_data['tool']['poetry']['repository'].split(   # pylint: disable=line-too-long
            "/")[-1]
        # save
        mkdoc_file.seek(0)
        yaml.dump(mkdoc_data, mkdoc_file)
        mkdoc_file.truncate()

with open('pyproject.toml', 'r+') as f:  # pylint: disable=w1514
    lines = f.readlines()
    if update is True:
        for i, line in enumerate(lines):
            if line.startswith('packages = [{include = "'):
                if (old_name is not None) and (new_name is not None):
                    lines[i] = line.replace(old_name, new_name)
            if line.startswith('package_name = "'):
                if (old_name is not None) and (new_name is not None):
                    lines[i] = line.replace(old_name, new_name)
            if line.startswith('package_version = "'):
                if (old_version is not None) and (new_version is not None):
                    lines[i] = line.replace(old_version, new_version)
            if line.startswith('docker_context = "'):
                if new_docker_context is not None:
                    lines[i] = line.replace(
                        f"docker_context = \"{data['tool']['taskipy']['variables']['docker_context']}\"", f"docker_context = \"{new_docker_context}\"")  # pylint: disable=line-too-long
    f.seek(0)
    f.writelines(lines)
    f.truncate()
