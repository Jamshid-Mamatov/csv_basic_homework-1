def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   list_data=data.split('\n')
  
   return list_data[1].split(',')

# Read the csv file

with open('data.csv','r') as f:
    fr=f.read()
    get_first_row(data=fr)