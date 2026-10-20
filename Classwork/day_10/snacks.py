import pandas as pd

# Create a quick DataFrame to test
data = {'Fruits': ['Apples', 'Bananas'], 'Quantity': [5, 10]}
df = pd.DataFrame(data)

print("Pandas version:", pd.__version__)
print(df)
