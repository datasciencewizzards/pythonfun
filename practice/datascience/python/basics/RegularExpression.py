# Package for the Regular Expressions

import re

# Check if the string starts with "The" and ends with "Spain":

txt = "The The rain in Spain"
x = re.search("^The.*Spain$" , txt)

if x:
    print("YES! We have a match! as \"{}\"".format(x.group()))
else:
    print("No match")

txt = "The The rain in Spain"

x = re.findall("^The.*ra" , txt)
print("String found {}".format(x))

# The split() Function
# The split() function returns a list where the string has been split at each match:
txt = "The rain in Spain"
# Words separated by whitespace

x = re.split("\s" , txt)
print("Return type of the result {} and the result {}".format(type(x),x))

# Control the number of occurrences. Split the string at the first instance only.
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# Find and Replace
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# The regular expression looks for any words that starts with an upper case "S":
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


