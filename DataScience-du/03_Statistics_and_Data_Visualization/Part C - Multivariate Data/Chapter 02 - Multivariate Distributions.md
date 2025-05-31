```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
from google.colab import drive
drive.mount('/content/drive')
```


```python
# RUN THIS COMMAND ONLY IF YOU USE GOOGLE COLAB.
%cd drive/MyDrive/TechLabs/03_Statistics\ and\ Data\ Visualization/Part\ B\ -\ Multivariate\ Data
```

# Chapter 2 - Multivariate Distributions
### Hey Techie,
Welcome to the second notebook of this part. Its contents refer to a video which you may find under: https://www.coursera.org/learn/understanding-visualization-data/lecture/8nSra/multivariate-distributions. To access this video, you need to audit the [Understanding and Visualizing Data with Python course on Coursera](https://www.coursera.org/learn/understanding-visualization-data) first.   
We encourage you to take this notebook as a template to code along the instruction video and try things out for yourself.
#### Have fun! :-)   
   
### Credits
Understanding and Visualizing Data with Python, University of Michigan (Coursera), https://www.coursera.org/learn/understanding-visualization-data
   
<hr style="border:2px solid gray"> </hr>   
   
## Notes

* Take notes here.
    * And here.
* ...
* ...

<hr style="border:2px solid gray"> </hr>   

## Multivariate Distributions in Python

Sometimes we can get a lot of information about how two variables (or more) relate if we plot them together. This tutorial aims to show how plotting two variables together can give us information that plotting each one separately may miss.




```python
# import the packages we are going to be using
import numpy as np # for getting our distribution
import matplotlib.pyplot as plt # for plotting
import seaborn as sns; sns.set() # For a different plotting theme

# Don't worry so much about what rho is doing here
# Just know if we have a rho of 1 then we will get a perfectly
# upward sloping line, and if we have a rho of -1, we will get 
# a perfectly downward slopping line. A rho of 0 will 
# get us a 'cloud' of points
r = 1

# Don't worry so much about the following three lines of code for now
# this is just getting the data for us to plot
mean = [15, 5]
cov = [[1, r], [r, 1]]
x, y = x, y = np.random.multivariate_normal(mean, cov, 400).T

# Adjust the figure size
plt.figure(figsize=(10,5))

# Plot the histograms of X and Y next to each other
plt.subplot(1,2,1)
plt.hist(x = x, bins = 15)
plt.title("X")

plt.subplot(1,2,2)
plt.hist(x = y, bins = 15)
plt.title("Y")

plt.show()
```


```python
# Plot the data
plt.figure(figsize=(10,10))
plt.subplot(2,2,2)
plt.scatter(x = x, y = y)
plt.title("Joint Distribution of X and Y")

# Plot the Marginal X Distribution
plt.subplot(2,2,4)
plt.hist(x = x, bins = 15)
plt.title("Marginal Distribution of X")


# Plot the Marginal Y Distribution
plt.subplot(2,2,1)
plt.hist(x = y, orientation = "horizontal", bins = 15)
plt.title("Marginal Distribution of Y")

# Show the plots
plt.show()
```
