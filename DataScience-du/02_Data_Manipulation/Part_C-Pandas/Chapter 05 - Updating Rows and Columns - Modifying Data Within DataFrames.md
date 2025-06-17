# Chapter 5 - Updating Rows and Columns - Modifying Data Within DataFrames  
## Hey Techie,
Welcome to the fifth notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/DCDe29sIKcE. The video deals with how to change values within Series objects and DataFrames. The underlying principles are first explained along a simple example and then applied to the real dataset we already know. At the end, as always, there are practical tasks, this time also two, to which you can write short answers as well.   

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html

## Have fun! :-)

*Video length*: 40 minutes
*Self-study time*: 40 minutes
*Total*: **80 minutes**

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

# How to update data

pdf.columns

# to change all of the columns
pdf.columns = ['name', ...]

# switch case, replace text
pdf.columns = [x.upper() for x in pdf.columns]
pdf.columns = [x.lower() for x in pdf.columns]
pdf.columns = pdf.columns.str.replace(' ', '_')

# to only change one name
pdf.rename(columns={'FIRST':'first_name', 'LAST':'last_name'})
pdf.rename(columns={'FIRST':'first_name', 'LAST':'last_name'}, inplace=True)

# ------

# To update the rows, which is usually the thing being done and is diverse

pdf.loc[2]
pdf.loc[2] = ['John', 'Smith', 'JohnSmith@email.com']

# To change less than the whole row
pdf.loc[2, ['last', 'email']] = ['Doe', 'JohnDoe@email.com']

# To change a single value.
pdf.loc[2, 'last'] = 'Smith'
pdf.at[2, 'last'] = 'Doe'

filtr = pdf['email'] == 'JohnDoe@email.com'
# pdf[filtr]['last'] = 'Smith'
pdf.loc[filtr, 'last'] = 'Smith'

pdf['email'] = pdf['email'].str.lower()

# APPLY
# is used to call a function on the values, used on either a series or a dataframe
# when used on a series, it is applied on each value of the series

## SERIES

pdf['email'].apply(len)
def update_email(email):
    return email.upper()
pdf['email'].apply(update_email)

# you can also use a lambda function
pdf['email'].apply(lambda x: x.lower())

## with DATAFRAMES

pdf.apply(len)
# returns the number of entries for each series
# you can have the same result for a series by len(pdf['col_name'])

pdf.apply(len, axis='columns')
# the number of entries for each row

pdf.apply(pd.Series.min)
pdf.apply(lambda x: x.min())

# Applymap passes the values, available only on dataframes.
pdf.applymap(len)
pdf.applymap(str.lower)

# MAP is used on series and substitute values.

pdf['first'].map({'Corey': 'Chris', 'Jane': 'Mary' })
pdf['first'].replace({'Corey': 'Chris', 'Jane': 'Mary' })

```

# Real-word Example

```python
# These options help us to inspect our data more easily.
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)

# These commands load the same survey data Corey is using in his video.
df = pd.read_csv("data/survey_results_public.csv", index_col = "Respondent")
schema_df = pd.read_csv("data/survey_results_schema.csv", index_col = "Column")

# START YOUR CODE HERE.

df.rename(columns={'ConvertedComp': 'SalaryUSD'})
df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)
# It is saner to have inplace as false, because you might be doing discovery data analysis, which might need you to change things, if you did it wrongly then you might break the whole process.
df['SalaryUSD']
df['Hobbyist'].map({'Yes':'True', 'No':'False'})
df['Hobbyist'].replace({'Yes':'True', 'No':'False'}) # If the column has more than yes/no entries.
df['Hobbyist'] = df['Hobbyist'].map({'Yes':'True', 'No':'False'})

```

# Practice Tasks

```python
# Load a clean DataFrame.
df = pd.read_csv("data/survey_results_public.csv", index_col = "Respondent")
```

## 1. Adjust the DataFrame's column names so that every column name is lowercased. 

Make use of list comprehensions.
The lower-method converts strings to lowercasing. 

```python
old_columns = df.columns
# YOUR CODE STARTS HERE.

df.columns = [x.lower() for x in old_columns]

#YOUR CODE ENDS HERE.
# THIS CELL TESTS YOUR RESULTS.
assert df.columns[0] == "mainbranch", "Your lowercasing does not seem to work!"
assert df.columns[-1] == "surveyease", "Your lowercasing does not seem to work!"

# For better readability, we undo this change. We applied it just for practice reasons. 
df.columns = old_columns
```

## 2. Some column names are misleading. Rename the columns *CareerSat* and *MgrIdiot* to *CareerSatisfaction* and *ManagerAwareness*. 

One can use Pandas' rename-function to rename indexes/columns.
How should you set the axis-argument inside the rename-functioncall?
How should you set the inplace-parameter inside the rename-functioncall?

```python
# START YOUR CODE HERE.

df.rename(columns={'CareerSat':'CareerSatisfaction', 'MgrIdiot':'ManagerAwareness'}, inplace=True)

# END YOUR CODE HERE.
# THIS CELL TESTS YOUR RESULTS.
assert "CareerSatisfaction" in df.columns, "You did not rename CareerSat correctly!"
assert "ManagerAwareness" in df.columns, "You did not rename MgrIdiot correctly!"
```

## 3. For comparison reasons, we want to convert the current dollar salaries to euro salaries (*CompTotal* column). At that, we assume an exchange ratio of 85%. Therefore, one dollar should equal 85 cents. 

Which method should you use? Apply, applymap, or map?
To be very efficient, you might want to solve this problem by using a lambda function inside the function call.
CompTotal is of dtype float64. Therefore, arithmetics operations work as you would expect. 


```python
# START YOUR CODE HERE.

df['CompTotal'] = df["CompTotal"].apply(lambda x: x*0.85)

# END YOUR CODE HERE.
# THIS CELL TESTS YOUR RESULTS.
assert df["CompTotal"].loc[3] == 19550, "Your conversion does not seem to work properly!"
assert df["CompTotal"].loc[10] == 807500, "Your conversion does not seem to work properly!"
assert df["CompTotal"].loc[20] == 2550, "Your conversion does not seem to work properly!"
```

## 4. In the *OpenSourcer* column, respondents were asked how often they contribute to open source projects. The answer options were: "Never," "Less than once per year," "Less than once a month but more than once per year," and "Once a month or more often." Complete the *adjust_OpenSourcer*-function so that it can be applied to the *OpenSourcer* column. The goal is for the new *OpenSourcer* column to contain False (boolean) if a respondent answered "Never". Otherwise, it should contain True (boolean). 

One can compare two values with the ==-operator.
The original OpenSourcer column contains strings.
Remind yourself of if/else conditionals.

```python
def adjust_OpenSourcer(answer):
    
    # START YOUR CODE HERE.
    if(answer == 'Never'):
        return False
    else:
        return True
    # END YOUR CODE HERE.
    
df["OpenSourcer"] = df["OpenSourcer"].apply(adjust_OpenSourcer)
# THIS CELL TESTS YOUR RESULTS.
assert df["OpenSourcer"].dtype == "bool", "adjust_OpenSourcer shall return boolean values!"
assert df["OpenSourcer"].iloc[0] == False, "Your adjustment seems to be incorrect!"
assert df["OpenSourcer"].iloc[-1] == True, "Your adjustment seems to be incorrect!"
```

## 5. Which method should you use if you want to adjust every value within a DataFrame?

*Your Answer* (enter by double-clicking): applymap

## 6. What is the main difference between *replace* and *map* as Series/DataFrame functions?

*Your Answer* (enter by double-clicking): map needs all entries, while replace only replaces the specified ones.

> Map assigns NaN to each element that is not present in its mapper dictionary. Replace substitutes only the values that are present in its mapper dictionary, values that are not present remain unchanged. 


