'''
Bubble sort algorithm

L - list of items, not sorted
Sorted - Boolean flag, True if sorted, False if not

Start assuming not sorted (set flag to false)

Repeat while Sorted is False

    Flag Sorted to True
    For loop, from index 1 to end of L
        If value at L[index] < L[index-1]
            Swap the values
            Flag Sorted to False
        End If
    Next value
Next

1 - Set sorted to False to enter the While loop
2 - Each iteration of the while loop, set sorted to True
3 - If a swap happens, set it back to false

We're certain the list is sorted, if we do one last pass on it
without swapping anything
'''


def bubble_sort(unsorted_list):
    # Flag
    sorted = False

    while not sorted:
        # Flag sorted to True first
        sorted = True
        # Go through second to last value in list
        for index in range(1,len(unsorted_list)):
            # If current element is smaller than previous, swap them
            if unsorted_list[index] < unsorted_list[index-1]:
                # Swap them [generic programming way]
                c = unsorted_list[index]
                unsorted_list[index] = unsorted_list[index-1]
                unsorted_list[index-1] = c
                # If a swap occurs, flag sorted to False
                sorted = False

    return unsorted_list

def main():
    values = ["Jim", "Mark", "Arthur", "Lorna", "Aurelien", "Fiona", "Jacqui"]
    sorted_values = bubble_sort(values)
    print(sorted_values)

if __name__ == "__main__":
    main()
