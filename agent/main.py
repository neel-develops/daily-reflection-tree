from tree_loader import load_tree, validate_tree
from engine import run_tree

if __name__ == "__main__":
    tree = load_tree("../tree/reflection-tree.json")
    validate_tree(tree)

    print("Starting Reflection Session...\n")
    run_tree(tree)
