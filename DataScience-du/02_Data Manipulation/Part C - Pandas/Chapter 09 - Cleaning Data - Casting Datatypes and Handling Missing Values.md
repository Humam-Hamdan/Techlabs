```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/02_Data\ Manipulation/Part\ C\ -\ Pandas
```

# Chapter 9 - Cleaning Data - Casting Datatypes and Handling Missing Values
### Hey Techie,   
Welcome to the ninth notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/KdmPHEnPJPs. In the instruction video's first half, Corey explains how to clean data within DataFrames. Afterward, he demonstrates the new skills with the real-world example which we already know. As always, at the end of this notebook are practice tasks to test your skills.     

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html

#### Have fun! :-)   
    
*Video length*: 32 minutes   
*Self-study time*: 32 minutes   
*Total*: **64 minutes**
<hr style="border:2px solid gray"> </hr>   

## Code-Snippets


```python
# This is the convention used to import Pandas.
import pandas as pd
# OTHER LIBRARIES.
import numpy as np
```


```python
people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', 
              None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}
```


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
    
## Real-word Example


```python
# These options help us to inspect our data more easily.
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)
```


```python
# These commands load the same survey data Corey is using in his video.
df = pd.read_csv("data/survey_results_public.csv", index_col = "Respondent")
schema_df = pd.read_csv("data/survey_results_schema.csv", index_col = "Column")
```


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Practice Tasks   


```python
# Load a clean DataFrame.
df = pd.read_csv("data/survey_results_public.csv", index_col = "Respondent")
```

#### 1. The survey DataFrame's index ranges from 1 to n, where n corresponds to the number of survey participants. Drop every row from the DataFrame where the questions Country, YearsCode, and ConvertedComp have not been answered. Do not make this drop in place but instead assign the cleaned DataFrame to a new variable named *cleaned_df*. Your final goal is to store the dropped indexes (i.e., 2679, 4271, etc.) in a list called *dropped_indexes*.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>To solve this task, you need to set three parameters within the dropna-method: axis, how, and subset.</li>
        <li>One can access a DataFrame's index by calling the index attribute (i.e., df.index).</li>
        <li>A DataFrame's index can be treated the same as a list.</li>
        <li>To check whether a list contains a specific element, one can use the in operator (i.e., if element in list).</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

cleaned_df = ...
dropped_indexes = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert cleaned_df.shape == (88751, 84), "Your drop seems to be incorrect!"
assert len(dropped_indexes) == 132, "Your dropped_indexes list seems to have the wrong length!"
assert 12032 in dropped_indexes, "Your dropped_indexes list does not contain every index!"
assert 57311 in dropped_indexes, "Your dropped_indexes list does not contain every index!"
assert 73522 in dropped_indexes, "Your dropped_indexes list does not contain every index!"
assert 88802 in dropped_indexes, "Your dropped_indexes list does not contain every index!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>cleaned_df = df.dropna(axis = 0, how = "all", subset = ["Country", "YearsCode", "ConvertedComp"])</code><br />
    <code>dropped_indexes = [index for index in df.index if index not in cleaned_df.index]</code><br />
</p>
</details>   
   
#### 2. On average, when did participants write their first line of code (Age1stCode column)? To answer this question, replace "younger than" and "older than" statements within the YearsCode column with the nearest age. For example, "older than 45" would become 46. Store the mean in a variable named *mean_age_code*.
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Remind yourself of the unique method which is applicable to Series objects.</li>
        <li>One needs to make replace-statements using Pandas in place or assign them to an existing/new Series object/DataFrame.</li>
        <li>You need to convert the Age1stCode column to float since NaN values are handled as float values.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

mean_age_code = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert df["Age1stCode"].dtype == float, "You need to change the column's data type!"
assert round(mean_age_code, 2) == 15.41, "Your result seems to be incorrect!"
assert len(str(mean_age_code)) == 18, "Your result seems to be incorrect!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>df["Age1stCode"].replace("Younger than 5 years", 4, inplace = True)</code><br />
    <code>df["Age1stCode"].replace("Older than 85", 86, inplace = True)</code><br />
    <code>df["Age1stCode"] = df["Age1stCode"].astype(float)</code><br />
    <code>mean_age_code = df["Age1stCode"].mean()</code><br />
</p>
</details>
