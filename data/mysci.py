# Column names an dcolumn indices to read
columns = {'date':0, 'time':1, 'tempout':2}

#Data types for each column (only if non-string)
types = {'tempout':float}

# Initialize my data as a data dictionary; 
# curly brackets => dictionary keys are strings, colon maps
data = {}
for column in columns:
    data[column] = []

# Read the data file
filename = "wxobs20170821.txt"
with open(filename,'r') as datafile:

   # read the first three lines (header) using a for loop
   # underscore is for variable used only as index
   for _ in range(3):
       print(_)
       datafile.readline()

   # Read and parse the rest of the file line var is a string
   for line in datafile:
       split_line = line.split()
       for column in columns:
           i = columns[column]
           t = types.get(column, str)
           value = t(split_line[i])
           data[column].append(value)

# line.split('\t') for tab delimiter, etc. default is whitespace
#       data.append(datum) 

# old DEBUG
#for datum in data[:10:2]:
#    print(datum)
# print(data[-1])
# [-1] implies last data pt
#for datum in data:
#      print(datum)

#with open(filename,'r') as datafile:
#   data = datafile.read()
# this file read method uses a context manager
# other way: 
#
# datafile = open(filename,'r')
# data = datafile.read()
# datafile.close()
# # Debug
# print(data)
# print(type(data))


