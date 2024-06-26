import pandas as pd

#Define a dictionary 'x'


x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)
#dictAppend = {"Name":"jame", "ID": 5, "Department": "engineer", "Salary" :70000}
df.loc[len(df.index)] = ['nils', 105, "Engineer", 75000] #syntax for new row Nils added new row

#display the result df
print(df)