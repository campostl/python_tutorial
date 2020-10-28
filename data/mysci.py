# Initialize my data variable as a list variable
data = []

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
       datum = line.split()
# line.split('\t') for tab delimiter, etc. default is whitespace
       data.append(datum) 

# DEBUG
# this won't work because the list we create with our nested indices is only
# 3 elements in length
#print(data[5:8][4])


#print(data[8][4])
#print(data[8][:5])
#print(data[8][::2])
#print(data[8][4][0]) # print only first character of the selected element
#print(data[8[4]])


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


