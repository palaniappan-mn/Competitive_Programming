input_json = {
"test_id": "50",
"test_name": "Amazon",
"schedule": {
    "test_interval":"30",
    "day": "Tuesday",
    "level2":{
                "level1":"test"
              }
}
}

def flatten_json(input_json):
    result = {}

    def flatten_recursively(nested_json, prefix=''):
        for key in nested_json:
            if type(nested_json[key]) is not dict:
                result[prefix+key] = nested_json[key]
            else:
                prefix += key+'_'
                flatten_recursively(nested_json[key], prefix)

    flatten_recursively(input_json)

    return result

print(flatten_json(input_json))

"""
Expected Output:
{
"test_id": "50",
"test_name": "Amazon",
"schedule_test_interval":"30",
"schedule_day": "Tuesday",
"schedule_level2_level1":"test"
}
"""
