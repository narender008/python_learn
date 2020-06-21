
print("importing my module....")

test = "test string"


def find_index(to_search, target):
    """finding indexes for provided string,list,tuple....."""
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return "not found"
