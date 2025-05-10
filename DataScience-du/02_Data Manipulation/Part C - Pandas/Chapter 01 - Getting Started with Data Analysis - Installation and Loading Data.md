```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/03_Data\ Manipulation/Part\ C\ -\ Pandas
```

# Chapter 1 - Getting Started with Data Analysis - Installation and Loading Data   
### Hey Techie,   
Welcome to the first notebook of this Pandas tutorial series. We encourage you to take this notebook as a template to code along the instruction video, which you may find at: https://youtu.be/ZyhVh-qRZPA. We have taken care of downloading the needed data already. Therefore, you can fully concentrate on absorbing the new coding concepts. At the end of this notebook, you can find tasks that test your knowledge of the topics covered in the video.    

**Here you may find the Pandas documentation:** https://pandas.pydata.org/docs/reference/index.html  
   
#### Have fun! :-)   
*Video length*: 23 minutes   
*Self-study time*: 23 minutes   
*Total*: **46 minutes**
<hr style="border:2px solid gray"> </hr>   
   
## Real-word Example


```python
# This is the convention used to import Pandas.
import pandas as pd
```


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

 #### 1. What are the dimensions of our survey DataFrame? How many rows, how many columns do we have?   
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>DataFrames have an attribute shape that contains this information.</li>
        <Li>The shape attribute returns a tuple that contains the rows first and the columns second.</li>
        <li>Remind yourself how to index tuple elements.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

rows = ...
columns = ...

# END YOUR CODE HERE.

print("Our survey data has {} rows and {} columns.".format(rows, columns))
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>rows = df.shape[0]</code><br />
    <code>columns = df.shape[1]</code><br /><br />
    Quickest way: <code>rows, columns = df.shape</code>
</p>
</details>   
   
#### 2. Five columns have the datatype float64: Which are those?   
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>The info-method, which is callable on a DataFrame, returns an output that contains the data type for every column.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

# Add the respective column names to this list as strings.
float64_columns = []  

# END YOUR CODE HERE.

print("The following columns have the data type float64: ", " ,".join(float64_columns))
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>df.info()</code> yields <em>CompTotal, ConvertedComp, WorkWeekHrs, CodeRevHrs, Age</em><br />
    <code>float64_columns = ["CompTotal", "ConvertedComp", "WorkWeekHrs", "CodeRevHrs", "Age"]</code>
</p>
</details>   
   
#### 3. Return the last 10 rows of the survey DataFrame.   
<br />
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>The tail-method, which is callable on a DataFrame, returns the last five rows by default.</li>
        <li>Inside the brackets of the method call, one can specify how many rows should be returned.</li>
    </ul>
</p>
</details>


```python
# START YOUR CODE HERE.

last_10_rows = ...

# END YOUR CODE HERE.

last_10_rows
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>last_10_rows = df.tail(10)</code>
</p>
</details>
