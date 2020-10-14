# Read the data file
filename = "wxobs20170821.txt"
with open(filename,'r') as datafile:
   data = datafile.read()
# this file read method uses a context manager
# other way: 
#
# datafile = open(filename,'r')
# data = datafile.read()
# datafile.close()
# # Debug
# print(data)
# print(type(data))
