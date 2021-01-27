def read_data(columns, types={}, filename="data/wxobs20170821.txt"):
    """
    Read data from CU Boulder Weather Station data file

    Parameters:
        columns: A dictionary of column names mapping to column indices
        types: A dictionary of column names mapping to the types to which to convert each column of data
        filename: A string path pointing tot he CU Boulder Wx Station data file
    """
    # Initialize my data as a data dictionary;
    # curly brackets => dictionary keys are strings, colon maps
    data = {}
    for column in columns:
        data[column] = []

    # Read the data file
    with open(filename,'r') as datafile:

       # read the first three lines (header) using a for loop
       # underscore is for variable used only as index
       for _ in range(3):
           datafile.readline()

       # Read and parse the rest of the file line var is a string
       for line in datafile:
           split_line = line.split()
           for column in columns:
               i = columns[column]
               t = types.get(column, str)
               value = t(split_line[i])
               data[column].append(value)

    return data

