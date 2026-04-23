import json

def load_tree(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    # Convert list → dict for fast lookup
    tree = {node["id"]: node for node in data["nodes"]}
    return tree


def validate_tree(tree):
    for node_id, node in tree.items():
        if "type" not in node:
            raise ValueError(f"Node {node_id} missing 'type'")

        if node["type"] == "question":
            if "options" not in node or not node["options"]:
                raise ValueError(f"Question node {node_id} missing options")
