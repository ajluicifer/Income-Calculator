# Importing Libraries
import pandas as pd

#path = r"C:\Users\hp\Desktop\june.csv"
path = input("Enter path of file")

# Reading CSV file and Formatting it according to situation
df = pd.read_csv(path,skiprows=19)

# Dropping useless rows from last
df.drop(df.tail(2).index,inplace = True)

# For removing all commas
df['Credit'] = df['Credit'].str.replace(',','')

# For replacing all Blank Spaces with zero
df['Credit'] = df['Credit'].str.replace(' ','0')

# For converting all strings to numeric Datatypes
df[["Credit"]] = df[["Credit"]].apply(pd.to_numeric)

# For slicing the Description column
df["Description"] = df["Description"].str.slice(3,19)

# For grouping the data wrt Description and finding sum
x = df.groupby(["Description"]).sum()

# For taking out required values from grouped data
income = x.loc["BY TRANSFER-NEFT","Credit"]
print(income)