def process_items(items):
    result = []
    for item in items:
        for other in items:
            if item == other:
                result.append(item)
    return result
