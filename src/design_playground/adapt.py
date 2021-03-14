import os
import json
import pathlib


DESIGN_PATH = pathlib.Path(pathlib.Path(__file__).parent, 'basic_design.json')


def load_design():
    with open(DESIGN_PATH, "r") as f:
        return json.load(f)


design = load_design()
new_design_id = 'aaa'
new_project_id = 'bbb'

for elm in design['elements']:
    elm.update({'designId': new_design_id, 'projectId': new_project_id})

for rel in design['relationships']:
    rel.update({'designId': new_design_id, 'projectId': new_project_id})
a = json.dumps(design['elements'][5]['specifications'])
print(design['elements'])
