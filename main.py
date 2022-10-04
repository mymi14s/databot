import os, json

def get_json(file_path):
    """
    :param file_path:
    :return: dict with results
    """
    try:
        return {'found':True, 'data':json.load(open(file_path))}
    except Exception as e:
        return {'found':False, 'data': str(e)}


def process_data(data):
    """
    :param data:
    :return: None, data exported to json
    """
    output = {}
    keys = data.keys()
    data_type = ''
    for key in keys:
        export_data = {'tag':'', 'description':'', 'required':False}
        key_type = type(data[key])

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
        data_type = ''

    # output json object
    output_path = os.getcwd()+'/schema/export.json'
    with open(output_path, 'w+') as f:
        json.dump(output, f, indent=4)

    print(f"Done, export is located at {output_path}")


if __name__ == "__main__":
    print("Started....")
    data_path = os.getcwd()+'/data/data_1.json'
    print(data_path)
    get_data = get_json(data_path)
    if get_data['found'] and get_data['data']:
        process_data(get_data['data']['message'])
    else:
        print("No data file found")
else:
    print("No execution")