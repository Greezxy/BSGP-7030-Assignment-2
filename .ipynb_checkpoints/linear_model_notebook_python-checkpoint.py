#!/usr/bin/env python
# coding: utf-8

# This notebook is an advanced version from the previous assignment demonstrating a simple linear regression analysis with annotations using Python to model Salary based on Years of Experience.

# # Install Packages

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error


# # Load the Dataset

# In[2]:


dataset = pd.read_csv("regression_data.csv")
x = dataset["YearsExperience"]
y = dataset["Salary"]


# # Fit Linear Regression

# In[3]:


slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept


# We use *scipy.stats.linregress* to calculate the slope and intercept of the best-fit line, the Pearson correlation coefficient(r), and the standard error.

# # Compute MSE-Mean Squared Error

# In[4]:


mse = mean_squared_error(y, y_pred)


# The Mean Squared Error(MSE) measures the average squared difference between actual and predicted salaries. A smaller MSE indicates better model performance. 

# # Print Model Statistics

# In[5]:


print(f"Slope (m):{slope:.4f}")
print(f"Intercept (b):{intercept:.4f}")
print(f"Correlation Coefficient (r):{r_value:.4f}")
print(f"Mean Squared Error (MSE):{mse:.4f}")


# Interpretation:
# - Slope(m): For every additional year of experience, the model predicts that salaray increases by $8285.29. This suggests a strong positive relationship between experience and salary.
# 
# - Intercept(b): When years of experience is 0, the model predicts a baseline salary of approximately $29203.52. It represents the starting point of the regression line.
# - Correlation Coefficient(r): A high r value (0.8861 close to 1) indicates a strong positive linear relationship between years of experience and salary.
# - Mean Squared Error(MSE): This value quantifies the average squared difference between actual and predicted salaries. The smaller MSE indicates better predictive performance of the model.

# # Plot with Annotations

# In[9]:


plt.figure(figsize=(8, 6))
plt.scatter(x, y, color="red", label="Data Points")
plt.plot(x, y_pred, color="blue", label="Fitted Line")
plt.title("Linear Regression: Salary vs. Years of Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.text(min(x), max(y), f"y={slope:.2f}x + {intercept:.2f}\nr={r_value:.2f}", fontsize=8, color="blue")
plt.legend()
plt.show()


# The scatter plot includes the regression line and an annotation with the regression equation and r value.
