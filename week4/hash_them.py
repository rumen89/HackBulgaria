#hash_them.py

def hash_them(keys, values):
    result = {}

    index = 0

    for key in keys:
        if index >= len(values):
            result[key] = None
        else:
            result[key] = values[index]

        index += 1

    return result

# keys = ["rumen", "ciklama", "tsvetan"]
# values = [1, 2]

# print(hash_them(keys, values))