def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """

    list_data=data.split('\n')
    first_column=[]
    for i in list_data[1:]:
        
        first_column.append(i.split(',')[0])
    
    return first_column
    
# Read the csv file

with open('data.csv','r') as f:
    fr=f.read()
    get_first_column(data=fr)