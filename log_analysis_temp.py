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
