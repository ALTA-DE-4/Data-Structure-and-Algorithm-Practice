def count_item_and_sort(items):
    result = {}
    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return " ".join([f"{item}->{count}" for item, count in sorted_result])

print (count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
print (count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
print (count_item_and_sort(["football", "basketball", "tenis"]))
