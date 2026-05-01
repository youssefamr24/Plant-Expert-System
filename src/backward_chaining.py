import re

# Check if a condition is satisfied or not based my facts
def evaluate_condition(condition, facts):

    # Handling numerical comparisons like "diameter > 10"

    # Regex used
    match = re.search(r'([a-zA-Z_]+)\s*(==|>|<|>=|<=)\s*(\d+)', condition)

    if match:
        var, op, val = match.groups()
        var = int(val)

        if var in facts:
            facts_val = facts[var]
            if op == '==': return facts_val == var
            if op == '>': return facts_val > var
            if op == '<': return facts_val < var
            if op == '>=': return facts_val >= var
            if op == '<=': return facts_val <= var
        
        return False
        
    # check for 'key is value' format like 'color is orange'
    if ' is ' in condition:
        key, val = condition.split(' is ')
        return facts.get(key.strip()) == val.strip()
    
    # Other conditions are treated as boolean flags like 'skin_smell'
    return facts.get(condition, False) is True


def backward_chaining(goal, facts, rules, visited=None):
    if visited is None:
        visited = set()
    
    # 1- Base case: if the goal is already in our facts
    if evaluate_condition(goal, facts):
        return True
    
    # Avoid cycles
    if goal in visited:
        return False
    visited.add(goal)

    # 2- Find rules that can conclude the goal
    for rule in rules: 
        # Search the rules list for any rule where the then part matches my current goal
        conclusion_str = f"{rule['then'][0]} is {rule['then'][1]}" if isinstance(rule['then'][1], str) else rule['then'][0] 

        if conclusion_str == goal or rule['then'][0] == goal:
            print(f"--- Cycle: Trying to prove '{goal}' using rule: {rule['if']} ---")

            conditions = rule['if']
            if rule['logic'] == 'AND':
                if all(backward_chaining(cond, facts, rules, visited) for cond in conditions):
                    # Successfully proved the goal, add it to facts
                    facts[rule['then'][0]] = rule['then'][1]
                    print(f"Fact Added: {goal} | Current Facts: {facts}")
                    return True
            
            elif rule['logic'] == 'OR':
                # At least one condition must be true
                if any(backward_chaining(cond, facts, rules, visited) for cond in conditions):
                    facts[rule['then'][0]] = rule['then'][1]
                    print(f"Fact Added: {goal} | Current Facts: {facts}")
                    return True

    return False    


    


    


    

