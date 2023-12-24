def binary_search(element, sorted_list):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]

        if guess == element:
            return mid
        elif guess < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1


moi_sorted_list = [11, 12, 22, 25, 34, 64, 90]
element_to_find = 22

result = binary_search(element_to_find, moi_sorted_list)

if result != -1:
    print(f"Элемент {element_to_find} найден по индексу {result}.")
else:
    print(f"Элемент {element_to_find} не найден в списке.")
