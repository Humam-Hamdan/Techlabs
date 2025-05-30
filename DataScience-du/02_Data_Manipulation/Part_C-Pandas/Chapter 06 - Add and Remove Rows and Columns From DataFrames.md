```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/02_Data\ Manipulation/Part\ C\ -\ Pandas
```

# Chapter 6 - Add and Remove Rows and Columns From DataFrames 
### Hey Techie,   
Welcome to the sixth notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/HQ6XO9eT-fc. In the instruction video, Corey explains adding and removing columns and rows to and from DataFrames. At the notebook's end, you find practice tasks to test your newly gained knowledge with the real-world survey data we already know.   

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html

#### Have fun! :-)   
    
*Video length*: 17 minutes   
*Self-study time*: 17 minutes   
*Total*: **34 minutes**
<hr style="border:2px solid gray"> </hr>   

## Code-Snippets


```python
# This is the convention used to import Pandas.
import pandas as pd
```


```python
people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}
```


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Practice Tasks   


```python
# These options help us to inspect our data more easily.
pd.set_option("display.max_columns", 85)
pd.set_option("display.max_rows", 85)
# Load a clean DataFrame.
df = pd.read_csv("data/survey_results_public.csv", index_col = "Respondent")
```

#### 1. Below you will find information for a new row. Add it to the survey DataFrame. 
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>One can use the append-method to add a row to a DataFrame.</li>
        <li>The append-method returns a new DataFrame. In this case, there is no inplace-argument.</li>
        <li>As we are applying a dictionary, set the ignore_index-argument to True.</li>
    </ul>
</p>
</details>


```python
new_row = {"MainBranch": "I am a student who is learning to code", 
           "Hobbyist": "Yes",
           "OpenSourcer": "Once a month or more often",
           "Employment": "Employed part-time",
           "Country": "Germany",
           "Student": "Yes, full-time"}
# START YOUR CODE HERE.

df = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert df.iloc[-1, 1] == "Yes", "It seems that adding the new row to the DataFrame did not work!"
assert df.iloc[-1, 4] == "Employed part-time", "It seems that adding the new row to the DataFrame did not work!"
assert df.shape[0] == 88884, "It seems that adding the new row to the DataFrame did not work!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>df = df.append(new_row, ignore_index = True)</code>
</p>
</details>   
   
#### 2. Below you will find three columns that appear to contain many NaN values. Remove these columns from the survey DataFrame.
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>One can use the drop-method to drop rows/columns from a DataFrame.</li>
        <li>As we are trying to drop columns, what value should we the axis-argument assign to?</li>
        <li>Remind yourself of the inplace-argument.</li>
    </ul>
</p>
</details>


```python
columns_drop = ["BlockchainOrg", "CodeRevHrs", "ConvertedComp"]
# START YOUR CODE HERE.

...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert "BlockchainOrg" not in df.columns, "As it seems you did not drop the BlockchainOrg column."
assert "CodeRevHrs" not in df.columns, "As it seems you did not drop the CodeRevHrs column."
assert "ConvertedComp" not in df.columns, "As it seems you did not drop the ConvertedComp column."
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>df.drop(labels = columns_drop, axis = "columns", inplace = True)</code>
</p>
</details>   
   
#### 3. Drop every survey respondent who is not resident in the US.

<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Remind yourself of conditionals to filter DataFrames.</li>
        <li>One can negate a filter by using the ~-operator.</li> 
        <li>To drop rows from a DataFrame, you need the row indexes.</li>
        <li>One can use the drop-method to drop rows/columns from a DataFrame.</li>
        <li>As we are trying to drop columns, what value should we the axis-argument assign to?</li>
        <li>Remind yourself of the inplace-argument.</li>
    </ul>
        
</p>
</details>


```python
# START YOUR CODE HERE.

# DEFINE A FILTER HERE.
filt = ...
# DROP THE ROWS HERE.
...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert len(df["Country"].unique()) == 1, "Your filter seems to not work!"
assert df["Country"].unique()[0] == "United States", "You did not extract residents from the US!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>filt = ~(df["Country"] == "United States")</code><br />
    <code>df.drop(labels = df.loc[filt].index, axis = "rows", inplace = True)</code>
</p>
</details>
