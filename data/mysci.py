# Column names an dcolumn indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7}

#Data types for each column (only if non-string)
types = {'tempout':float, 'windspeed': float}

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
#       headerline=datafile.readline()
#       print(headerline)
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

# DEBUG
print(data['tempout'])


