
import os
import sys
import json

def generate_file_structure(path):
    stack = [path]
    result = {
        "type": "directory",
        "items": {}
    }

    while stack:
        current_path = stack.pop()
        folder_node = result["items"]
        path_components = os.path.relpath(current_path, path).split(os.path.sep)
        for component in path_components:
            folder_node = folder_node.setdefault(component, {
                "type": "directory",
                "items": {}
            })

        for filename in os.listdir(current_path):
            file_path = os.path.join(current_path, filename)
            if os.path.isdir(file_path):
                stack.append(file_path)
            else:
                folder_node["items"][filename] = {
                    "type": "file"
                }

    return result

path_to_explore = 'path_here'
output_structure = generate_file_structure(path_to_explore)

with open("output.json", "w") as outfile:
    json.dump(output_structure, outfile, indent=4)

print("DONE!")