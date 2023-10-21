import json
import models

def main(json_obj):
    data = json.loads(str(json_obj))
    #print(data['forklift_id'])
    print(models.Forklift.query.get(data['forklift_id']))
