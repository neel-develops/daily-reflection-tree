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

        # Replace placeholders in text
        text = interpolate(node.get("text", ""), state)
        print("\n" + text)

        if node["type"] == "end":
            break

        elif node["type"] == "question":
            options = node["options"]

            for i, opt in enumerate(options):
                print(f"{i+1}. {opt}")

            choice = get_valid_input(len(options))
            answer = options[choice - 1]

            state["answers"][node["id"]] = answer

            # Update signal if exists
            if "signal" in node:
                axis, val = node["signal"].split(":")
                state["signals"][axis][val] += 1

            current = get_next_node_after_question(tree, node["id"])

        elif node["type"] == "decision":
            prev_answer = list(state["answers"].values())[-1]
            current = evaluate_rules(node, prev_answer)

        elif node["type"] in ["reflection", "bridge"]:
            input("\nPress Enter to continue...")
            current = get_next_node_after_question(tree, node["id"])

        elif node["type"] == "summary":
            print("\n--- SUMMARY ---")
            print(generate_summary(state))
            current = get_next_node_after_question(tree, node["id"])


# -------- Helper Functions -------- #

def evaluate_rules(node, answer):
    for rule in node["rules"]:
        if answer in rule["if"]:
            return rule["goTo"]
    raise ValueError("No matching rule found")


def get_next_node_after_question(tree, current_id):
    keys = list(tree.keys())
    idx = keys.index(current_id)
    return keys[idx + 1] if idx + 1 < len(keys) else "END"


def get_valid_input(max_option):
    while True:
        try:
            choice = int(input("Choose option: "))
            if 1 <= choice <= max_option:
                return choice
        except:
            pass
        print("Invalid input. Try again.")


def get_dominant(axis_dict):
    return max(axis_dict, key=axis_dict.get)


def generate_summary(state):
    axis1 = get_dominant(state["signals"]["axis1"])
    axis2 = get_dominant(state["signals"]["axis2"])
    axis3 = get_dominant(state["signals"]["axis3"])

    return f"""
You leaned toward {axis1} control,
{axis2} orientation, and a {axis3}-focused perspective.

This combination reflects how you approached your day.
Awareness of these patterns is the first step toward growth.
"""


def interpolate(text, state):
    for key, value in state["answers"].items():
        placeholder = "{" + key + ".answer}"
        text = text.replace(placeholder, value)
    return text
