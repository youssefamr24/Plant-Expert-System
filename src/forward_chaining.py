import re

def forward_chaining(rules, facts, goal):

    def condition_holds(cond, facts):
        match = re.search(r'([a-zA-Z_]+)\s*(==|>=|<=|>|<|=)\s*(\d+)', cond)
        if match:
            var, op, val = match.groups()
            val = int(val)
            if var not in facts:
                return False
            fv = facts[var]
            if op in ('=', '=='): return fv == val
            if op == '>':         return fv > val
            if op == '<':         return fv < val
            if op == '>=':        return fv >= val
            if op == '<=':        return fv <= val
        if ' is ' in cond:
            key, val = cond.split(' is ', 1)
            return facts.get(key.strip()) == val.strip()
        return facts.get(cond.strip(), False) is True

    print("--- Starting Forward Chaining ---")
    print(f"Initial Facts: {facts}\n")

    new_fact_added = True
    cycle = 1

    while new_fact_added:
        new_fact_added = False
        print(f"Cycle {cycle}:")

        for rule in rules:
            if rule.get('triggered', False):
                continue

            # ✅ AND vs OR support
            if rule['logic'] == 'OR':
                fired = any(condition_holds(cond, facts) for cond in rule['if'])
            else:
                fired = all(condition_holds(cond, facts) for cond in rule['if'])

            if fired:
                key, val = rule['then']
                if facts.get(key) == val:
                    rule['triggered'] = True
                    continue

                facts[key] = val
                result_str = f"{key} is {val}" if isinstance(val, str) else key
                new_fact_added = True
                rule['triggered'] = True
                print(f"  > Rule Fired: IF {' AND '.join(rule['if'])} THEN {result_str}")

        print(f"  Facts at end of cycle {cycle}: {facts}")

        if ' is ' in goal:
            g_key, g_val = goal.split(' is ', 1)
            goal_reached = facts.get(g_key.strip()) == g_val.strip()
        else:
            goal_reached = facts.get(goal, False) is True

        if goal_reached:
            print(f"\nGoal '{goal}' has been PROVEN!")
            return True

        cycle += 1
        if not new_fact_added:
            print("\nNo more rules can be fired.")

    print(f"\nGoal '{goal}' could not be proven.")
    return False
