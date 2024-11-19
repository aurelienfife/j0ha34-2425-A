'''
Linear search:
Look for a value in a sequential list
Pros: 
    - You don't need to to have sorted values
    - Simple to implement
    - On short lists, quite efficient
Cons:
    - Inefficient on long lists (Up to O(N))
    - Assuming values are unique, otherwise it's a variation
    on counting occurences

Pseudocode

1. Get search term from user
2. Initialise "found index" to a negative value or something similar
3. For loop, with index, for each element in the list
    3.1 If current element matches search term
        3.1.1 set found index to current element's index
        3.1.2 Break out of the loop
3.2 Next loop
4. Return found index or "null/None/-1 etc" if not found

'''

# Linear search in Python

def linear_search(search_list, search_term):
    found_index = None  # Assume not found
    for index in range(len(search_list)):
        # If value matches search term, stop loop
        if search_list[index] == search_term:
            found_index = index
            break # Stop the loop
    return found_index

def main():

    names = ["Mark", "Arthur", "Lorna", "Jim"]
    
    term = input("Enter a search term")
    position = linear_search(search_list=names, search_term=term)

    if position == None:
        print("Not found")
    else:
        print("Found at: ", position)

if __name__ == "__main__":
    main()