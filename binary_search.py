
def binary_search(number_list, item):
    """
    method that returns the index of an element in an ordered list. The element is the item that needs to be informed
    :param number_list: an ordered list
    :param item: item to seek
    :return: item index
    """
    first_number = 0
    last_number = len(number_list) - 1

    while first_number <= last_number:
        mid = (first_number + last_number) // 2
        number = number_list[mid]

        if number == item:
            return mid
        if number > item:
            last_number = mid - 1
        else:
            first_number = mid + 1

    return None


if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9]
    print(binary_search(lista, 3))
