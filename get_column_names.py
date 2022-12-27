#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    list_data=data.split('\n')
    
    return list_data[0].split(',')

# Read the csv file

with open('data.csv','r') as f:
    fr=f.read()
    get_column_names(data=fr)