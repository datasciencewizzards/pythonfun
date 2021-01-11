# File Handling
# The key function for working with files in Python is the open() function.
#
# The open() function takes two parameters; filename, and mode.
#
# There are four different methods (modes) for opening a file:
#
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists
#
# In addition you can specify if the file should be handled as binary or text mode
#
# "t" - Text - Default value. Text mode
#
# "b" - Binary - Binary mode (e.g. images)
f = open("demofile.txt" , "w")
f.write("Now the file has more content! - 1 ")
f.write("Now the file has more content! - 2 ")
f.close()

# open and read the file after the appending:
f = open("demofile.txt" , "r")
print(f.read())
f.close()

# open and read the file : Partially:
f = open("demofile.txt" , "r")
print(f.read(5))
f.close()

# Read file line by line
f = open("demofile.txt" , "r")
print(f.readline())
print(f.readline())
f.close()

# Read file line by line and looping
f = open("demofile.txt" , "r")
for x in f:
    print(x)
f.close()

# Delete file
import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# Delete Folder
# To delete an entire folder, use the os.rmdir() method:
try :
    os.rmdir("myfolder")
except:
    print("Folder myfolder doesn't exist")


# Check if file exists, then delete it:

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
