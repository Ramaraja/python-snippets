
import yaml

with open("details.yml", 'r') as f:
    try:
        print(yaml.load(f))
    except yaml.YAMLError as exc:
        print(exc)
