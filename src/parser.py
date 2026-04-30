import re
import json

def parse_facts(file_path):

    facts = {}
    with open(file_path, 'r', encoding='utf-8') as f:

        for line in f:

            line = line.strip()

            if not line or line.startswith('#'):
                continue

            if '=' in line:
                key, val = line.split('=')
                facts[key.strip()] = int(val.strip())

            elif ' is ' in line:
                key, val = line.split(' is ')
                facts[key.strip()] = val.strip()

            else:
                facts[line] = True

    return facts

def parse_rules(file_path):

    rules = []
    pattern = re.compile(r"IF\s+(.*?)\s+THEN\s+(.*)", re.IGNORECASE)

    with open(file_path, 'r', encoding='utf-8') as f:

        for line in f:

            line = line.strip()
            if not line: continue
            
            match = pattern.match(line)

            if match:
                condition_str, result_str = match.groups()
                
                logic = "OR" if " OR " in condition_str else "AND"

                conditions = re.split(r'\s+AND\s+|\s+OR\s+', condition_str, flags=re.IGNORECASE)

                if ' is ' in result_str:
                    res_key, res_val = result_str.split(' is ')
                    conclusion = (res_key.strip(), res_val.strip())

                else:
                    conclusion = (result_str.strip(), True)

                rules.append({
                    "if": [c.strip() for c in conditions],
                    "then": conclusion,
                    "logic": logic
                })

    return rules

# this for testing only and not important in assignment 
# print(json.dumps(parse_facts("facts.txt"), indent=4))
# print(json.dumps(parse_rules("rules.txt"), indent=4))
