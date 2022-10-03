import json, os

def get_json(file_path):
    try:
        return {'found':True, 'data':json.load(open(file_path))}
    except exception as e:
        return {'found':False, 'data': str(e)}


def process_data(data):
    output = {}
    keys = data.keys()
    data_type = ''
    for key in keys:
        export_data = {'tag':'', 'description':'', 'required':False}
        key_type = type(data[key])
        print()
        if key_type == str:
            data_type = 'STRING'
        elif key_type == int:
            data_type = 'INTEGER'
        elif key_type == list and len(data[key]):
            if type(data[key][0]) == str:
                data_type = 'ENUM'
            elif type(data[key][0]) == dict:
                data_type = 'ARRAY'
        output = {**output, **{key: {**{'type': data_type, **export_data}}}}

    # output json object
    output_path = os.getcwd()+'/schema/export.json'
    with open(output_path, 'w+') as f:
        json.dump(output, f, indent=4)

    print(f"Done, export is located at {output_path}")
