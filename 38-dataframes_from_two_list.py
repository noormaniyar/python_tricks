"""
    The easiest way to create dataframe from two lists is to use the pandas module.
    First Install pandas with pip : pip install pandas
    Import pandas, and pass the lists to the DAtaFrame constructor.
    Since we have two lists, we have to use the zip() function to combine the lists.
    Below, we have a list of car brands and a list of car models.
    We are going to create a DataFrame, the DataFrame will have one column called Brands and 
    another called Models and the index will be the numbers in ascending order.

"""
import pandas as pd
listl = ['Tesla', 'Ford', 'Fiat']
models = ['X', 'Focus', 'Doblo']
df = pd.DataFrame(list(zip(listl,models)),
index =[1, 2, 3] ,
columns=['Brands','Models'])
print(df)