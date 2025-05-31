```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/02_Data\ Manipulation/Part\ C\ -\ Pandas
```

# Chapter 2 - DataFrame and Series Basics - Selecting Rows and Columns  
### Hey Techie,   
Welcome to the second notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/zmdjNSmRXF4. In the instruction video's first half, Corey explains the concepts of selecting rows and columns in DataFrames with code snippets that you find below. Then, he applies the newly gained knowledge to the real-world survey data which we already know. As always, at the end of this notebook are practice tasks to deepen your knowledge.   

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html  

#### Have fun! :-)   
    
*Video length*: 34 minutes   
*Self-study time*: 34 minutes   
*Total*: **1 hour 8 minutes**
<hr style="border:2px solid gray"> </hr>   

## Code-Snippets


```python
# This is the convention used to import Pandas.
import pandas as pd
```


```python
person = {
    "first": "Corey", 
    "last": "Schafer", 
    "email": "CoreyMSchafer@gmail.com"
}
```


```python
people = {
    "first": ["Corey"], 
    "last": ["Schafer"], 
    "email": ["CoreyMSchafer@gmail.com"]
}
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
df = pd.read_csv("data/survey_results_public.csv")
schema_df = pd.read_csv("data/survey_results_schema.csv")
```


```python
# START YOUR CODE HERE.

```

<hr style="border:2px solid gray"> </hr>   
   
## Practice Tasks   


```python
# Load a clean DataFrame.
df = pd.read_csv("data/survey_results_public.csv")
```

#### 1. Grab the 20th column and the 20th row from the survey dataset. 
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>DataFrames have an iloc-attribute with which one can index rows and columns.</li>
        <li>The iloc-attribute starts counting at zero.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

column_20 = ...
row_20 = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert column_20.iloc[2] == "Not sure", "It seems as you picked the wrong column!"
assert row_20["Hobbyist"] == "No", "It seems as you picked the wrong row!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>column_20 = df.iloc[:, 19]</code><br />
    <code>row_20 = df.iloc[19, :]</code><br /><br />
</p>
</details>   
   
#### 2. Grab the 10th, 500th, and 4500th row as well as the columns EdLevel, CompTotal, and CodeRevHrs from the survey dataset.
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Currently, our DataFrame index ranges from 0 to n-1, with n being the number of respondents. Hence, iloc and loc yield the same results when indexing rows.</li>
        <li>We can index multiple rows/columns at the same time by packing them in lists.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

index_df = ...

# END YOUR CODE HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert index_df.iloc[0, -1] == 4.0, "It seems as you filtered the wrong rows/columns!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>index_df = df.loc[[9, 499, 4499], ["EdLevel", "CompTotal", "CodeRevHrs"]]</code>
</p>
</details>   
   
#### 3. Grab the first hundred rows, as well as the columns between Hobbyist and Student (both including) from the survey dataset.
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>One can index multiple rows/columns together using the 
            ":"-notation inside the iloc/loc attribute.</li>
        <li>Other than regular indexing in Python, using the 
            ":"-notation inside iloc/loc extracts from x up to y including.</li>
    </ul>
        
</p>
</details>


```python
# START YOUR CODE HERE.

index_df = df.loc[:99, "Hobbyist":"Student"]

# END YOUR CODE HERE.
```


```python
assert index_df.loc[0, "Country"] == "United Kingdom", "It seems as you filtered the wrong rows/columns!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>index_df = df.loc[:99, "Hobbyist":"Student"]</code>
</p>
</details>
