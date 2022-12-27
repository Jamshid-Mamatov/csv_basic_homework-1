def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    list_data=data.split('\n')
    num_col=list_data[0].split(',')
    return len(num_col)

# Read the csv file

with open('data.csv','r') as f:
    fr=f.read()
    find_number_of_columns(data=fr)