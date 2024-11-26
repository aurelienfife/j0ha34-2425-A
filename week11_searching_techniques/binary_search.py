'''
Find <-- 7
Found <-- False
Start <-- 0
End <-- length(list)

WHILE Found = False AND Start <= End
     Mid <-- (Start + End) DIV 2

     IF list[Mid] = Find THEN
        OUTPUT 'Found at' +  Mid
        Found <-- True
     ELSE
        IF List[Mid] > Find THEN
           End <-- Mid - 1
        ELSE
          Start <-- Mid + 1
        ENDIF
     ENDIF
ENDWHILE

IF Found = False THEN
     OUTPUT 'Not found'
ENDIF
'''

# Set up the data we look into
sequence = [1,4,6,8,19,26,30,35,45,49,50,53,55,56,58,66,67,70,77,79,83,84,89,93,100]
# When we start, we haven't found yet
found = False
# Starting point
start = 0
# Ending point
end = len(sequence)

# Get the target number
target = int(input("What number are you looking for?"))

# Repeat indefinitely
# While number not found and
# end >= start
while found == False and start <= end:

    # For visualisation: create a new list
    search_space = sequence[start:end]

    # Calculate midpoint index -> sum of start and end//2
    midpoint = (start + end) // 2
    mid_number = sequence[midpoint]

    # If found - indicate so, break out of loop
    if mid_number == target:
        print("Found at index:", midpoint)
        found = True

    else:
        # If the midnumber > target
        # Midpoint index is the new end of search space
        # Otherwise index + is the new start of search space
        if mid_number > target:
            end = midpoint
        else:
            start = midpoint + 1

if not found:
    print("Not found")
