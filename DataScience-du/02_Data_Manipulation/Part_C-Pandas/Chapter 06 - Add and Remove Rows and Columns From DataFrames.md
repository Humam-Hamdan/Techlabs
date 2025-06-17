# Chapter 6 - Add and Remove Rows and Columns From DataFrames 
## Hey Techie,
Welcome to the sixth notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/HQ6XO9eT-fc. In the instruction video, Corey explains adding and removing columns and rows to and from DataFrames. At the notebook's end, you find practice tasks to test your newly gained knowledge with the real-world survey data we already know.   

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html

## Have fun! :-)

*Video length*: 17 minutes   
*Self-study time*: 17 minutes   
*Total*: **34 minutes**

# Code-Snippets

```python
# This is the convention used to import Pandas.
import pandas as pd
people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}
pdf = pd.DataFrame(people)

# START YOUR CODE HERE.

pdf['first'] + ' ' + pdf['last']
pdf['full_name'] = pdf['first'] + ' ' + pdf['last']
pdf # to see
pdf.drop(columns=['first','last'])
pdf.drop(columns=['first','last'], inplace=True)
pdf['full_name'].str.split(' ')
pdf['full_name'].str.split(' ', expand=True)
pdf[['first', 'last']] = pdf['full_name'].str.split(' ', expand=True)
pdf[['first', 'last']] = pdf['full_name'].str.split(' ', expand=True)
pdf._append({'first': 'Tony'}, ignore_index=True)

people2 = {
    'first' : ['Tony', 'Steve'],
    'last' : ['Stark', 'Rogers'],
    'email' : ['Ironman@avenge.com', 'Cap@avenge.com']
}
pdf2 = pd.DataFrame(people2)
pdf2
pdf._append(pdf2, ignore_index=True)
pdf = pdf._append(pdf2, ignore_index=True, sort=False) # false sort is the default now.
pdf.drop(index=4)
pdf.drop(index=4, inplace=True)

pdf.drop(index=pdf[pdf['last'] == 'Doe' ].index)
# OR:
last_name_filter = pdf['last'] == 'Doe'
pdf.drop(index=pdf[last_name_filter].index)

```

# Practice Tasks

```python
# These options help us to inspect our data more easily.
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)
# Load a clean DataFrame.
df = pd.read_csv("data/survey_results_public.csv", index_col = "Respondent")
```

## 1. Below you will find information for a new row. Add it to the survey DataFrame. 

One can use the append-method to add a row to a DataFrame.

The append-method returns a new DataFrame. In this case, there is no inplace-argument.

As we are applying a dictionary, set the ignore_index-argument to True.

```python
new_row = {"MainBranch": "I am a student who is learning to code", 
           "Hobbyist": "Yes",
           "OpenSourcer": "Once a month or more often",
           "Employment": "Employed part-time",
           "Country": "Germany",
           "Student": "Yes, full-time"}
# START YOUR CODE HERE.

df = df._append(new_row, ignore_index=True)

# END YOUR CODE HERE.
# THIS CELL TESTS YOUR RESULTS.
assert df.iloc[-1, 1] == "Yes", "It seems that adding the new row to the DataFrame did not work!"
assert df.iloc[-1, 4] == "Employed part-time", "It seems that adding the new row to the DataFrame did not work!"
assert df.shape[0] == 88884, "It seems that adding the new row to the DataFrame did not work!"
```

## 2. Below you will find three columns that appear to contain many NaN values. Remove these columns from the survey DataFrame.

One can use the drop-method to drop rows/columns from a DataFrame.

As we are trying to drop columns, what value should we the axis-argument assign to?

Remind yourself of the inplace-argument.

```python
columns_drop = ["BlockchainOrg", "CodeRevHrs", "ConvertedComp"]
# START YOUR CODE HERE.

df.drop(columns=columns_drop, inplace=True)

# END YOUR CODE HERE.
# THIS CELL TESTS YOUR RESULTS.
assert "BlockchainOrg" not in df.columns, "As it seems you did not drop the BlockchainOrg column."
assert "CodeRevHrs" not in df.columns, "As it seems you did not drop the CodeRevHrs column."
assert "ConvertedComp" not in df.columns, "As it seems you did not drop the ConvertedComp column."
```

## 3. Drop every survey respondent who is not resident in the US.

Remind yourself of conditionals to filter DataFrames.

One can negate a filter by using the ~-operator. 

To drop rows from a DataFrame, you need the row indexes.

One can use the drop-method to drop rows/columns from a DataFrame.

As we are trying to drop columns, what value should we the axis-argument assign to?

Remind yourself of the inplace-argument.

```python
# START YOUR CODE HERE.

# DEFINE A FILTER HERE.
filt = ~(df['Country'] == 'United States')
# DROP THE ROWS HERE.

df.drop(index=df[filt].index, inplace=True)

# END YOUR CODE HERE.
# THIS CELL TESTS YOUR RESULTS.
assert len(df["Country"].unique()) == 1, "Your filter seems to not work!"
assert df["Country"].unique()[0] == "United States", "You did not extract residents from the US!"
```

