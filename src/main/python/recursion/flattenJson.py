"""Given a JSON object with nested objects, write a function flatten_json
that flattens all the objects to a single key-value dictionary.
Do not use the library that actually performs this function.
"""

import json

def flatten_json(d):
    result_dict = {}
    for key, value in d.items():
        # if value is another dict then recursive call flatten again
        if isinstance(value, dict):
            inner_dict = flatten_json(value)
            for inner_key, inner_value in inner_dict.items():
                # append parent key with inner key
                result_dict[key + '_' + inner_key] = inner_value
        elif not isinstance(input, dict):
            result_dict[key] = value

    return result_dict

# depth first search use a stack
def flatten_json2(input):
    def dfs(input, curr_path):
        if not isinstance(input, dict):
            output["_".join(curr_path)] = input
            return
        for key in input:
            curr_path.append(key)
            dfs(input[key], curr_path)
            curr_path.pop()
    output = {}
    dfs(input, [])
    return output

json_str = {'a': {'b': 'c', 'd': {'e': 'f'}}}
json_str = json.dumps(flatten_json2(json_str))
print(json_str)
