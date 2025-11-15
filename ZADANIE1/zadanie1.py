def find_max_deep(obj, deep):
    max_deep_found = -1

    if isinstance(obj, list):
        max_deep_found = deep

    if isinstance(obj, (list, tuple, dict)):
        items = obj if not isinstance(obj, dict) else obj.values()
        for element in items:
            deep_in_child = find_max_deep(element, deep + 1)
            if deep_in_child > max_deep_found:
                max_deep_found = deep_in_child

    return max_deep_found

def dodaj_element(wejscie):
    max_deep = find_max_deep(wejscie, 0)
    
    def modify_at_depth(obj, level, target_depth):
        if isinstance(obj, list) and level == target_depth:
            if len(obj) > 0:
                max_val = max([x for x in obj if isinstance(x, (int, float))], default=0)
                new_value = max_val + 1
            else:
                new_value = 1
            obj.append(new_value)
            return

        if isinstance(obj, (list, tuple)):
            for element in obj:
                modify_at_depth(element, level + 1, target_depth)
        elif isinstance(obj, dict):
            for value in obj.values():
                modify_at_depth(value, level + 1, target_depth)
    
    if max_deep != -1:
        modify_at_depth(wejscie, 0, max_deep)

    return wejscie

if __name__ == '__main__':
    input_list = [1, [2, 3], 4]
    output_list = dodaj_element(input_list)
    print(output_list)