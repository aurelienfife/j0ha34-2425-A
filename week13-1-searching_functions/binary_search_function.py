
# Function returns index of found item
# or None if not found
def binary_search(sorted_list, search_term):
    # When we start, we haven't found yet
    found = False
    # Starting point
    start = 0
    # Ending point
    end = len(sorted_list)
    # Location of found item
    location = -1

    # Repeat indefinitely
    # While number not found and
    # start < end
    while found == False and start < end:

        # Calculate midpoint index -> sum of start and end//2
        midpoint = (start + end) // 2
        mid_number = sorted_list[midpoint]

        # If found - indicate so, break out of loop
        if mid_number == search_term:
            location = midpoint
            found = True

        else:
            # If the midnumber > target
            # Midpoint index is the new end of search space
            # Otherwise index + is the new start of search space
            if mid_number > search_term:
                end = midpoint
            else:
                start = midpoint + 1

    if not found:
        return None
    else:
        return location


def main():
    # Set up the data we look into
    sequence = [1,4,6,8,19,26,30,35,45,49,50,53,55,56,58,66,67,70,77,79,83,84,89,93,100]

    # Get the target number
    target = int(input("What number are you looking for?"))

    result = binary_search(sequence, target)
    if  result == None:
        print("Value not found")
    else:
        print("Value found at", result)

if __name__ == "__main__":
    main()
