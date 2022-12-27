def find_number_of_rows(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    list_data=data.split('\n')
    num_row=len(list_data)-1
    return num_row

# Read the csv file

with open('data.csv','r') as f:
    fr=f.read()
    find_number_of_rows(data=fr)