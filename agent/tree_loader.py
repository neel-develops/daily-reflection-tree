import json

def load_tree(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    # convert list → dict for fast lookup
    tree = {node["id"]: node for node in data["nodes"]}

    return tree
