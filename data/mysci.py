# Column names an dcolumn indices to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}

#Data types for each column (only if non-string)
types = {'tempout':float, 'windspeed': float, 'windchill': float}

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

# Compute the wind chill temperature
def compute_windchill(t, v):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v16 = v ** 0.16
    wci = a + (b * t) - (c * v16) + (d * t * v16)
    return wci

# Running the function to compute windchill index
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

# DEBUG
#print(data['tempout'])
#print(windchill)
for wc_data, wc_comp in zip(data['windchill'], windchill):
    print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')

#for i,j in zip([1,2],[3,4,5]):
#    print(i,j)

