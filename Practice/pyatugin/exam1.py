list_c = [20, 89, "A", 0, "Word", "Name"]

def get_number_of_elements(list):
    count = 0
    for element in list:
        count += 1
    return count

print("Number of elements in the list: ", get_number_of_elements(list_c))