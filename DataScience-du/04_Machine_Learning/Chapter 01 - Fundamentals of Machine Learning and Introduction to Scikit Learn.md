```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/04_Machine\ Learning
```


```python
# IMPORT THESE FIRST.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from data.adspy_shared_utilities import plot_fruit_knn
from sklearn.datasets import load_breast_cancer
```

# Chapter 01 - Fundamentals of Machine Learning and Introduction to Scikit Learn
### Hey Techie,   
Welcome to the first notebook of this Machine Learning tutorial series. Today's videos serve as a kick-off to the field of Machine Learning.   
This notebook is designed to allow you to take notes as you watch each video and learn along the code discussed in the videos. At the end of the notebook, you will find practice tasks that you can solve on your own and compare to our sample solution.   
After auditing the course, you may find the respective materials here: https://www.coursera.org/learn/python-machine-learning/home/week/1
#### Have fun! :-)   
*Video length in total*: 70 minutes   
*Self-study time*: 70 minutes   
*Total*: **140 minutes**   
#### Credits
Applied Machine Learning in Python, University of Michigan (Coursera), https://www.coursera.org/learn/python-machine-learning?specialization=data-science-python
<hr style="border:2px solid gray"> </hr>   
   
## Notes

* Take notes here.
    * And here.
* ...
* ...

<hr style="border:2px solid gray"> </hr>   
   
## Applied Machine Learning, Module 1:  A simple classification task


```python
# Load the data.
fruits = pd.read_table('data/fruit_data_with_colors.txt')
fruits.head()
```


```python
# create a mapping from fruit label value to fruit name to make results easier to interpret
lookup_fruit_name = dict(zip(fruits.fruit_label.unique(), fruits.fruit_name.unique()))   
lookup_fruit_name
```


```python
# plotting a scatter matrix

X = fruits[['height', 'width', 'mass', 'color_score']]
y = fruits['fruit_label']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

cmap = cm.get_cmap('gnuplot')
scatter = pd.plotting.scatter_matrix(X_train, c= y_train, marker = 'o', s=40, hist_kwds={'bins':15}, figsize=(9,9), cmap=cmap)
```


```python
# plotting a 3D scatter plot

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(X_train['width'], X_train['height'], X_train['color_score'], c = y_train, marker = 'o', s=100)
ax.set_xlabel('width')
ax.set_ylabel('height')
ax.set_zlabel('color_score')
plt.show()
```

### Create train-test split


```python
# For this example, we use the mass, width, and height features of each fruit instance
X = fruits[['mass', 'width', 'height']]
y = fruits['fruit_label']

# default is 75% / 25% train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```

### Create classifier object


```python
knn = KNeighborsClassifier(n_neighbors = 5)
```

### Train the classifier (fit the estimator) using the training data


```python
knn.fit(X_train, y_train)
```

### Estimate the accuracy of the classifier on future data, using the test data


```python
knn.score(X_test, y_test)
```

### Use the trained k-NN classifier model to classify new, previously unseen objects


```python
# first example: a small fruit with mass 20g, width 4.3 cm, height 5.5 cm
fruit_prediction = knn.predict([[20, 4.3, 5.5]])
lookup_fruit_name[fruit_prediction[0]]
```


```python
# second example: a larger, elongated fruit with mass 100g, width 6.3 cm, height 8.5 cm
fruit_prediction = knn.predict([[100, 6.3, 8.5]])
lookup_fruit_name[fruit_prediction[0]]
```

### Plot the decision boundaries of the k-NN classifier


```python
plot_fruit_knn(X_train, y_train, 5, 'uniform')   # we choose 5 nearest neighbors
```

### How sensitive is k-NN classification accuracy to the choice of the 'k' parameter?


```python
k_range = range(1,20)
scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test, y_test))

plt.figure()
plt.xlabel('k')
plt.ylabel('accuracy')
plt.scatter(k_range, scores)
plt.xticks([0,5,10,15,20]);
```

### How sensitive is k-NN classification accuracy to the train/test split proportion?


```python
t = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

knn = KNeighborsClassifier(n_neighbors = 5)

plt.figure()

for s in t:

    scores = []
    for i in range(1,1000):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1-s)
        knn.fit(X_train, y_train)
        scores.append(knn.score(X_test, y_test))
    plt.plot(s, np.mean(scores), 'bo')

plt.xlabel('Training set proportion (%)')
plt.ylabel('accuracy');
```

<hr style="border:2px solid gray"> </hr>   
   
## Practice Tasks   
For these practice tasks, you will be using the Breast Cancer Wisconsin (Diagnostic) Database to create a classifier that can help diagnose patients. First, read through the description of the dataset (below).


```python
cancer = load_breast_cancer()
# Print the dataset description.
#print(cancer.DESCR)
```

The object returned by `load_breast_cancer()` is a scikit-learn Bunch object, which is similar to a dictionary.


```python
cancer.keys()
```

### Task 1
How many features does the breast cancer dataset have?    
    
*This function should return an integer.*   
   
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>Above, you can see the cancer dictionary's key names. Which of those contains information about all the features?</li>
        <li>What sequence type is returned if you access the key you are looking for?</li>
    </ul>
</p>
</details>


```python
def answer_one():
    # START YOUR CODE HERE.
    
    return # RETURN YOUR ANSWER HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert answer_one() == 30, "This is not the correct amount of features!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>def answer_one():</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;return len(cancer["feature_names"])</code>
</p>
</details> 

### Task 2

Scikit-learn works with lists, numpy arrays, scipy-sparse matrices, and pandas DataFrames, so converting the dataset to a DataFrame is not necessary for training this model. Using a DataFrame does however help make many things easier such as munging data, so let's practice creating a classifier with a pandas DataFrame. 



Convert the sklearn.dataset `cancer` to a DataFrame. 

*This function should return a `(569, 31)` DataFrame with* 

*columns =*

    ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
    'mean smoothness', 'mean compactness', 'mean concavity',
    'mean concave points', 'mean symmetry', 'mean fractal dimension',
    'radius error', 'texture error', 'perimeter error', 'area error',
    'smoothness error', 'compactness error', 'concavity error',
    'concave points error', 'symmetry error', 'fractal dimension error',
    'worst radius', 'worst texture', 'worst perimeter', 'worst area',
    'worst smoothness', 'worst compactness', 'worst concavity',
    'worst concave points', 'worst symmetry', 'worst fractal dimension',
    'target']

*and index =*

    RangeIndex(start=0, stop=569, step=1)
   
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>You need to stack the feature and target values horizontally.</li>
        <li>You can change an array's orientation from horizontally to vertically by using the reshape-method with parameter values -1 and 1.</li>
        <li>The feature_names list does not contain a target instance so far.</li>
    </ul>
</p>
</details>


```python
def answer_two():
    # START YOUR CODE HERE.
    
    return # RETURN YOUR ANSWER HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert answer_two().shape[0] == 569, "You did not extract every sample!"
assert answer_two().shape[1] == 31, "You did not extract every column!"
assert answer_two().iloc[1, -1] == 0, "Your data are in the wrong order!"
assert answer_two().iloc[-1, 1] == 24.54, "Your data are in the wrong order!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>def answer_two():</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;data = np.hstack((cancer["data"], cancer["target"].reshape(-1, 1)))</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;column_names = [*cancer["feature_names"], "target"]</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;return pd.DataFrame(data, columns = column_names)</code><br/>
</p>
</details> 

### Task 3
What is the class distribution? (i.e. how many instances of `malignant` (encoded 0) and how many `benign` (encoded 1)?)

*This function should return a Series named `target` of length 2 with integer values and index =* `['malignant', 'benign']`.
   
   
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>During our Pandas tutorial series, you encountered one method that extracts unique value counts for a Series object. Remind yourself of that method.</li>
        <li>You can access a Series object's index with the dot notation.</li>
    </ul>
</p>
</details>


```python
def answer_three():
    # START YOUR CODE HERE.
    
    return # RETURN YOUR ANSWER HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert answer_three()["benign"] == 357, "As it seems you extracted the wrong counts!"
assert answer_three()["malignant"] == 212, "As it seems you extracted the wrong counts!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>def answer_three():</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;series = answer_two()["target"].value_counts()</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;series.index = series.index.map({1: "benign", 0: "malignant"})</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;return series</code><br/>
</p>
</details> 

### Task 4
Split the DataFrame into `X` (the data) and `y` (the labels).

*This function should return a tuple of length 2:* `(X, y)`*, where* 
* `X`*, a pandas DataFrame, has shape* `(569, 30)`
* `y`*, a pandas Series, has shape* `(569,)`   
   
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <ul>
        <li>To return X, you only need to drop the target column from the cancer_df.</li>
        <li>To return y, you only need to extract the target column from the cancer_df.</li>
    </ul>
</p>
</details>


```python
def answer_four():
    cancer_df = answer_two()
    # START YOUR CODE HERE.

    return X, y
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert type(answer_four()[0]) == type(pd.DataFrame()), "You should return X as a DataFrame!"
assert type(answer_four()[1]) == type(pd.Series(dtype = "float64")), "You should return y as a Series!"
assert answer_four()[0].shape == (569, 30), "Your X has the wrong dimensions!"
assert answer_four()[1].shape == (569,), "Your y has the wrong dimensions!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>def answer_four():</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;cancer_df = answer_two()</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;X = cancer_df.drop(["target"], axis = 1)</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;y = cancer_df["target"]</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;return X, y</code><br/>
</p>
</details> 

### Task 5   
Using `train_test_split`, split `X` and `y` into training and test sets `(X_train, X_test, y_train, and y_test)`.

**Set the random number generator state to 0 using `random_state=0` to make sure your results are reproducible!**

*This function should return a tuple of length 4:* `(X_train, X_test, y_train, y_test)`*, where* 
* `X_train` *has shape* `(426, 30)`
* `X_test` *has shape* `(143, 30)`
* `y_train` *has shape* `(426,)`
* `y_test` *has shape* `(143,)`   
   
<br /> 
<details>    
<summary>
    <font size="3" color="red"><b>Hints (click to expand)</b></font>
</summary>
<p>
    <li>By default, train_test_split returns a 75/25 split.</li>
    <li>Set the random_state parameter to 0.</li>
</p>
</details>


```python
def answer_five():
    X, y = answer_four()
    # START YOUR CODE HERE.
    
    return X_train, X_test, y_train, y_test
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert answer_five()[0].shape == (426, 30), "Your X_train has the wrong dimensions!"
assert answer_five()[1].shape == (143, 30), "Your X_test has the wrong dimensions!"
assert answer_five()[2].shape == (426,), "Your y_train has the wrong dimensions!"
assert answer_five()[3].shape == (143,), "Your y_test has the wrong dimensions!"
assert answer_five()[0].iloc[10, 10] == 0.1998, "Adjust your setting of the random_state parameter!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>def answer_five():</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;X, y = answer_four()</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;return X_train, X_test, y_train, y_test</code><br/>
</p>
</details> 

### Task 6   
Using KNeighborsClassifier, fit a k-nearest neighbors (knn) classifier with `X_train`, `y_train` and using one nearest neighbor (`n_neighbors = 1`).

*This function should return a* `sklearn.neighbors.classification.KNeighborsClassifier`.


```python
def answer_six():
    X_train, X_test, y_train, y_test = answer_five()
    # START YOUR CODE HERE.
    
    return # RETURN YOUR ANSWER HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert type(answer_six()) == type(KNeighborsClassifier()), "Please return a KNN Classifier!"
assert answer_six().get_params()["n_neighbors"] == 1, "Please use one nearest neighbor!"
assert answer_six().kneighbors()[0].shape == (426, 1), "Please use X_train and y_train for training the classifier!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>def answer_six():</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;X_train, X_test, y_train, y_test = answer_five()</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;return KNeighborsClassifier(n_neighbors = 1).fit(X_train, y_train)</code><br/> 
</p>
</details> 

### Task 7
Using your knn classifier, predict the class label using the mean value for each feature.

Hint: You can use `cancerdf.mean()[:-1].values.reshape(1, -1)` which gets the mean value for each feature, ignores the target column, and reshapes the data from 1 dimension to 2 (necessary for the precict method of KNeighborsClassifier).

*This function should return a numpy array either `array([ 0.])` or `array([ 1.])`.*


```python
def answer_seven():
    cancerdf = answer_two()
    means = cancerdf.mean()[:-1].values.reshape(1, -1)
    # START YOUR CODE HERE.
    
    return # RETURN YOUR ANSWER HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert answer_seven() == np.array([1]), "Your predictions seems to be wrong!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>def answer_seven():</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;cancerdf = answer_two()</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;means = cancerdf.mean()[:-1].values.reshape(1, -1)</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;return answer_six().predict(means)</code><br/>
</p>
</details> 

### Task 8
Using your knn classifier, predict the class labels for the test set `X_test`.

*This function should return a numpy array with shape `(143,)` and values either `0.0` or `1.0`.* 


```python
def answer_eight():
    X_train, X_test, y_train, y_test = answer_five()
    knn = answer_six()
    # START YOUR CODE HERE.
    
    return # RETURN YOUR ANSWER HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert answer_eight().shape == (143,), "Please predict X_test!"
assert answer_eight()[0] == 1, "Your predictions seem to be incorrect!"
assert answer_eight()[-1] == 0, "Your predictions seem to be incorrect!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>def answer_eight():</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;X_train, X_test, y_train, y_test = answer_five()</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;knn = answer_six()</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;return knn.predict(X_test)</code><br/>
</p>
</details>

### Task 9
Find the score (mean accuracy) of your knn classifier using `X_test` and `y_test`.

*This function should return a float between 0 and 1.*


```python
def answer_nine():
    X_train, X_test, y_train, y_test = answer_five()
    knn = answer_six()
    # START YOUR CODE HERE.
    
    return # RETURN YOUR ANSWER HERE.
```


```python
# THIS CELL TESTS YOUR RESULTS.
assert answer_nine() == 0.916083916083916, "Your accuracy seems to be wrong!"
```

<details>    
<summary>
    <font size="3" color="darkgreen"><b>Solution (click to expand)</b></font>
</summary>
<p>
    <code>def answer_nine():</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;X_train, X_test, y_train, y_test = answer_five()</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;knn = answer_six()</code><br/>
    <code>&nbsp;&nbsp;&nbsp;&nbsp;return knn.score(X_test, y_test)</code><br/>
</p>
</details>
