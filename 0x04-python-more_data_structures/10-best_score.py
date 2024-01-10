#!/usr/bin/python3
def best_score(my_dict):
    if not isinstance(my_dict, dict) or len(my_dict) == 0:
        return None

    r_value = list(my_dict.keys())[0]
    b_score = list(my_dict.values())[0]
    for k, v in my_dict.items():
        if v > b_score:
            b_score = v
            r_value = k
    return (r_value)
