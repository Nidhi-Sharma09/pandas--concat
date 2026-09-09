import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Aman", "Priya"],
    "Marks": [85, 92]
})

df2 = pd.DataFrame({
    "Name": ["Rahul", "Neha"],
    "Marks": [78, 88]
})

df3 = pd.DataFrame({
    "Age": [21, 22]
})

#Q1 — Stack the rows
print(pd.concat([df1, df2]))

#Q2 — Stack rows + reset index
print(pd.concat([df1,df2], ignore_index=True))

#Q3 — Combine columns side-by-side
print(pd.concat([df1, df2], axis=1))
print(pd.concat([df1, df3], axis=1))