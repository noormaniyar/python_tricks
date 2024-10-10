"""
    Let's say you have a list of names and you want to write them
    in a file, and you want all the names to be written vertically.
    Here is a sample code that demonstrates how you can do it.
    The code below creates a CSV file. We tell the code to write
    each name on a new line by using the escape character C\n').
    Another way you can create a CSV file is by using the CSV module.
"""
names = ['John Kelly', 'Moses Nkosi', 'Joseph Marley']
with open('names.csv', 'w') as file:
    for name in names:
        file.write(name)
        file.write('\n')
# reading CSV file
with open ('names.csv', 'r') as file:
    print(file. read())



"""
    Using CSV module
    If you don't want to use this method, you can import the CSV
    module. CSV is a built-in module that comes with Python, so
    there is no need to install it. Here is how you can use the CSV
    module to accomplish the same thing. Example code on the
    next page:
"""
import csv
names = ['John Kelly', 'Moses Nkosi', 'Joseph Marley']
with open('names.csv', 'w') as file:
    for name in names:
        writer = csv.writer(file,lineterminator = '\n')
        writer.writerow([name])
# Reading the file
with open ('names.csv', 'r') as file:
    print(file.read())