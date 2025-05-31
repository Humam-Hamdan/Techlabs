```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/02_Data\ Manipulation/Part\ C\ -\ Pandas
```

# Chapter 5 - Updating Rows and Columns - Modifying Data Within DataFrames  
### Hey Techie,   
Welcome to the fifth notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/DCDe29sIKcE. The video deals with how to change values within Series objects and DataFrames. The underlying principles are first explained along a simple example and then applied to the real dataset we already know. At the end, as always, there are practical tasks, this time also two, to which you can write short answers as well.   

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html

#### Have fun! :-)   
    
*Video length*: 40 minutes   
*Self-study time*: 40 minutes   
*Total*: **80 minutes**
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

#### 1. Adjust the DataFrame's column names so that every column name is lowercased. 
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Make use of list comprehensions.</li>
        <li>The lower-method converts strings to lowercasing.</li> 
    </ul>
</p>
</details>


```python
old_columns = df.columns
# YOUR CODE STARTS HERE.

df.columns = ...

#YOUR CODE ENDS HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert df.columns[0] == "mainbranch", "Your lowercasing does not seem to work!"
assert df.columns[-1] == "surveyease", "Your lowercasing does not seem to work!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>df.columns = [column.lower() for column in df.columns]</code>
</p>
</details>


```python
# For better readability, we undo this change. We applied it just for practice reasons. 
df.columns = old_columns
```

#### 2. Some column names are misleading. Rename the columns *CareerSat* and *MgrIdiot* to *CareerSatisfaction* and *ManagerAwareness*. 
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>One can use Pandas' rename-function to rename indexes/columns.</li>
        <li>How should you set the axis-argument inside the rename-functioncall?</li>
        <li>How should you set the inplace-parameter inside the rename-functioncall?</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert "CareerSatisfaction" in df.columns, "You did not rename CareerSat correctly!"
assert "ManagerAwareness" in df.columns, "You did not rename MgrIdiot correctly!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>df.rename({"CareerSat": "CareerSatisfaction", "MgrIdiot": "ManagerAwareness"}, axis = "columns", inplace = True)</code>
</p>
</details>   
   
#### 3. For comparison reasons, we want to convert the current dollar salaries to euro salaries (*CompTotal* column). At that, we assume an exchange ratio of 85%. Therefore, one dollar should equal 85 cents. 
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Which method should you use? Apply, applymap, or map?</li>
        <li>To be very efficient, you might want to solve this problem by using a lambda function inside the function call.</li>
        <li>CompTotal is of dtype float64. Therefore, arithmetics operations work as you would expect.</li> 
    </ul>
        
</p>
</details>


```python
# START YOUR CODE HERE.

df["CompTotal"] = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert df["CompTotal"].loc[3] == 19550, "Your conversion does not seem to work properly!"
assert df["CompTotal"].loc[10] == 807500, "Your conversion does not seem to work properly!"
assert df["CompTotal"].loc[20] == 2550, "Your conversion does not seem to work properly!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>df["CompTotal"] = df["CompTotal"].apply(lambda x: x*0.85)</code>
</p>
</details>

#### 4. In the *OpenSourcer* column, respondents were asked how often they contribute to open source projects. The answer options were: "Never," "Less than once per year," "Less than once a month but more than once per year," and "Once a month or more often." Complete the *adjust_OpenSourcer*-function so that it can be applied to the *OpenSourcer* column. The goal is for the new *OpenSourcer* column to contain False (boolean) if a respondent answered "Never". Otherwise, it should contain True (boolean). 
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>One can compare two values with the ==-operator.</li>
        <li>The original OpenSourcer column contains strings.</li>
        <li>Remind yourself of if/else conditionals.</li>
    </ul>
        
</p>
</details>


```python
def adjust_OpenSourcer(answer):
    
    # START YOUR CODE HERE.
    
    # END YOUR CODE HERE.
    
df["OpenSourcer"] = df["OpenSourcer"].apply(adjust_OpenSourcer)
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert df["OpenSourcer"].dtype == "bool", "adjust_OpenSourcer shall return boolean values!"
assert df["OpenSourcer"].iloc[0] == False, "Your adjustment seems to be incorrect!"
assert df["OpenSourcer"].iloc[-1] == True, "Your adjustment seems to be incorrect!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>def adjust_OpenSourcer(answer):</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;if answer == "Never":</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return False</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;else:</code><br />
    <code>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return True</code>
</p>
</details>

#### 5. Which method should you use if you want to adjust every value within a DataFrame?

*Your Answer* (enter by double-clicking): 

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    applymap
</p>
</details>

#### 6. What is the main difference between *replace* and *map* as Series/DataFrame functions?

*Your Answer* (enter by double-clicking): 

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    Map assigns NaN to each element that is not present in its mapper dictionary. Replace substitutes only the values that are present in its mapper dictionary, values that are not present remain unchanged. 
</p>
</details>
