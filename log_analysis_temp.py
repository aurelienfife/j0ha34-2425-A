''' 
This is an example of log file analysis
it's an example of data reduction - 
similar to a pivot table in Excel
in Python you can also use Numpy or data science
packages to do it
'''

# Open the file for reading
# Will open read-only / text by default
f = open("full_log.txt")

# Dictionary of IP addresses
ip_addr = {}    # empty now

# treat the file like a list
# And iterate like a for loop
for line in f:
    # split the string between spaces
    elts = line.split(" ")
    # Now we have a separated list of sub-strings,
    # the IP is the first element
    current_ip = elts[0]

    # if the current IP is already in the dictionary keys
    # increment value
    if current_ip in ip_addr.keys():     # Returns a list of keys
        ip_addr[current_ip] += 1
    else:
        # if not already in dictionary, set to 1
        ip_addr[current_ip] = 1

# Close file for resource efficiency
f.close()

# Take the dictionary and obtain a list of key/value pairs
# So we can sort them
ip_count_list = ip_addr.items()

# Next we take the list and sort it by count (descending)
# To do that we need to create a lambda function 
# that take a tuple and returns the second element (the count)
# in this case t is a tuple (key, value) and t[1] is the value alone
sorted_list = sorted(ip_count_list, key=lambda t:t[1], reverse=True)

# Show on screen
for pair in sorted_list:
    print(pair[0], "appears:", pair[1])

# Alternatively save to a file (example: CSV)
new_f = open("results.csv", "w")

for pair in sorted_list:
    new_f.write(pair[0] + "," + str(pair[1]) + "\n")  # \n -> new line

new_f.close()
