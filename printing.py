def print_comparision(name, dates, times, original_data, computed_data):
    """
    Print a comparison of two time series (original and computed)

    Parameters:
       name: A string name for the data being cmpared. (Limited to 9 chars in length)
       dates: List of strings representing the dates fro each data element
       times: List of strings representing time of day for each data element
       original_data: List of original data (floats)
       computed_data: List of computed data (floats)
    """

# Output comparison of data
print(f'                ORIGINAL   COMPUTED')
print(f' DATE   TIME   {name.upper():>9} {name.upper():>9} DIFFERENCE')
print(f'------- ------ --------- --------- ----------')
zip_data = zip(data['date'], data['time'], data['heatindex'], heatindex)
for date, time, orig, comp in zip(dates, times, original_data, computed_data):
    print(f'{date} {time:>6} {orig:9.6f} {comp:9.6f} {orig-comp:10.6f}')

