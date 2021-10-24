import json
import yaml


# 1. json to text parser
with open("json_file.json", "r") as json_f:
    data = json.load(json_f)
    with open("text_file.txt", "w") as text_f:
        text_f.wrte(str(data))


# 2. json to yaml parser
with open("json_file.json", "r") as json_f:
    data = json.load(json_f)
    with open("yaml_file.yaml", "w") as yaml_f:
        yaml.dump(data, yaml_f)


# 3. Yaml to json parser
with open("yaml_file.yaml", "r") as yaml_f:
    data = yaml.safe_load(yaml_f)
    with open("json_file.json", "w") as json_f:
        json.dump(data, json_f, indent=4)


# 4. Yaml to text parser
with open("yaml_file.yaml", "r") as yaml_f:
    data = yaml.safe_load(yaml_f)
    with open("text_file.txt", "w") as text_f:
        text_f.write(str(data))