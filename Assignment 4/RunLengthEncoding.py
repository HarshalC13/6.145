def flatten_list(x):
    out = []
    for element in x:
        if type(element) != list:
            out.append(element)
        else:
            f = flatten_list(element)
            for e2 in f:
                out.append(e2)
    return out


def run_length_encode_2d(array):
    flat_array = flatten_list(array)
    list = []
    count = 0
    cur_character = flat_array[0]
    for i in flat_array:
        if i == cur_character:
            count += 1
        else:
            list.append((count, cur_character))
            count = 1
            cur_character = i
    list.append((count, cur_character))
    return list

