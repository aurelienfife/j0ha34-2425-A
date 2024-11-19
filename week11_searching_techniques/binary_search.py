'''

1. Set low boundary to 0 and high boundary to l
2. 
'''

term = "kitchen"

f = open("words.txt")
words = f.readlines()

low_boundary = 0
high_boundary = len(words) - 1

while low_boundary <= high_boundary:
    middle = low_boundary + (high_boundary - low_boundary) // 2

    if words[middle].strip().lower() ==  term:
        print("Found at", middle)
    
    elif words[middle] < term:
        low_boundary = middle + 1

    else:
        high_boundary = middle - 1
