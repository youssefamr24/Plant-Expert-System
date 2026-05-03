from parser import parse_facts, parse_rules
from forward import forward_chaining
from backward_chaining import backward_chaining


def main():

    # ===== Load Data =====
    facts = parse_facts("data/facts.txt")
    rules = parse_rules("data/rules.txt")

    print("===== Expert System =====")
    print("Initial Facts:", facts)

    # ===== User يدخل goal =====
    goal = input("\nEnter goal (citrus_fruit or fruit is orange): ")

    # ===== Forward =====
    print("\n=== Forward Chaining ===")
    forward_result = forward_chaining(rules, facts.copy(), goal)

    # ===== Backward =====
    print("\n=== Backward Chaining ===")
    backward_result = backward_chaining(goal, facts.copy(), rules)

    # ===== Final =====
    print("\n=== Final Results ===")
    print("Forward:", forward_result)
    print("Backward:", backward_result)


if __name__ == "__main__":
    main()
