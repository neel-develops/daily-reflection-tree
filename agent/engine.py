def run_tree(tree):
    current = "START"
    state = {
        "answers": {},
        "signals": {
            "axis1": {"internal": 0, "external": 0},
            "axis2": {"contribution": 0, "entitlement": 0},
            "axis3": {"self": 0, "altro": 0}
        }
    }

    while True:
        node = tree[current]
        print("\n" + node.get("text", ""))

        if node["type"] == "end":
            break

        if node["type"] == "question":
            options = node["options"]
            for i, opt in enumerate(options):
                print(f"{i+1}. {opt}")

            choice = int(input("Choose: ")) - 1
            answer = options[choice]
            state["answers"][node["id"]] = answer

            # signal update
            if "signal" in node:
                axis, val = node["signal"].split(":")
                state["signals"][axis][val] += 1

            current = get_next_node(tree, node, answer)

        elif node["type"] == "decision":
            prev_answer = list(state["answers"].values())[-1]
            current = evaluate_rules(node, prev_answer)

        else:
            input("Press Enter to continue...")
            current = get_next_node(tree, node, None)

def evaluate_rules(node, answer):
    for rule in node["rules"]:
        if answer in rule["if"]:
            return rule["goTo"]
    return None

def get_next_node(tree, node, answer):
    # simple sequential fallback
    ids = list(tree.keys())
    idx = ids.index(node["id"])
    return ids[idx + 1] if idx + 1 < len(ids) else "END"
