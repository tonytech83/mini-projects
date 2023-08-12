import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

df = pd.DataFrame(data)

# display the DataFrame
print(df)
print()

# add a new column
df['Profession'] = ['Engineer', 'Doctor', 'Architect', 'Scientist']
print(df)
print()

# filter the DataFrame based on age
filtered_df = df[df['Age'] > 30]
print(filtered_df)
print()
