# TASK 1
file = open("Task1.txt",'r')

with open("Task1.txt",'w') as st:
    st.write("This is a sample text file.\n")
    st.write("It contain multiple lines.")

import os
file = "Task1.txt"
if os.path.exists(file):
    print("File already exist.")
else:
    print("File doesn't exist.")

# TASK 2
file1 = open("Output.txt",'r')

with open("Output.txt",'a') as ot:
    ot.write("Hello Python!\n")
    ot.write("\n Learing file handing in Pyhton")