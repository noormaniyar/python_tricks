"""
Let's continue with the tip from the previous tip (38). One of the
most important aspects of pandas DataFrame is that it is very
flexible. We can add and remove columns. Let's add a column
called Age to the DataFrame. The column will have the ages of
the cars.
"""
import pandas as pd
listl = ['Tesla', 'Ford', 'Fiat']
models = ['X', 'Focus', 'Doblo']
df = pd.DataFrame(list(zip(listl,models)),
index =[1, 2, 3] ,
columns=['Brands','Models'])
df['Age'] = [2, 4, 3]
print(df)

"""
    Dropping or removing a column
    Pandas has a drop() method that we can use to remove columns
    and rows from a DataFrame. Let's say we want to remove the
    column "Models" from the DataFrame above. You can see from
    the output that the "Models" column has been removed. The
    inplace=True means we want the change to be made on the
    original DataFrame. On a DataFrame, axis 1 means columns. So,
    when we pass 1 to the axis parameter, we are dropping a column.
"""

df.drop('Models', inplace=True, axis=1)
print(df)