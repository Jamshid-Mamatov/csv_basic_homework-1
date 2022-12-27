#Define function,Get coloumn names from a csv file
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    list_data=data.split('\n')
   
    return list_data[0].split(',')
# Read the csv file

with open('data.csv','r') as f:
    fr=f.read()
    find_number_of_columns(data=fr)
