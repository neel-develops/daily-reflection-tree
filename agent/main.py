import json
from engine import run_tree

def load_tree():
    with open("../tree/reflection-tree.json") as f:
        data = json.load(f)
        return {node["id"]: node for node in data["nodes"]}

if __name__ == "__main__":
    tree = load_tree()
    run_tree(tree)
