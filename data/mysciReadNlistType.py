# Read the data file
filename = "wxobs20170821.txt"
with open(filename,'r') as datafile:
   data = datafile.read()

#Debug
print(type(data))

