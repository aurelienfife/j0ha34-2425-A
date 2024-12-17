# Insertion sort -> with words

def insert_sort(array):

    # Start from second element to the end
    # (main loop, left to ---> right)
    for index in range(1, len(array)):
        key = array[index]
        back_index = index - 1

        # Secondary loop, current place to left  <-----
        while back_index >= 0 and key < array[back_index]:
            array[back_index+1] = array[back_index]
            back_index -= 1
        array[back_index + 1] = key


def main():

    seasonal = ["reindeer", "snow", "santa", "presents", "krampus", "turkey", "pudding", "whisky", "wham", "sprouts"]

    print(seasonal)
    insert_sort(seasonal)
    print(seasonal)


if __name__ == "__main__":
    main()