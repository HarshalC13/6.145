out = []

def tree_max(tree):
    if len(tree['children']) == 0:
        out.append(tree['value'])
    else:
        for element in tree['children']:
            tree_max(element)
            out.append(tree['value'])

    return max(out)