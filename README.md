# BSGP 7030 – Assignment 2: Linear Regression in Python and R

## Purpose of the Assignment

The purpose of this assignment is to demonstrate a simple linear regression analysis using both Python and R to model the relationship between "Salary" and "Years of Experience". The task involves creating visualizations, fitting regression models, and evaluating the results using two different programming environments.


## Tools and Libraries Used

### Python (via Jupyter Notebook)
- `pandas` – for data manipulation
- `matplotlib` – for visualization
- `scikit-learn` – for performing linear regression

### R (via RKernel in Jupyter)
- `base R` – for reading data and plotting
- `ggplot2` – for data visualization


## Files Included
- `environment_assignment2.yml` – the customized working environment for this assignment
- `regression_data.csv` – the dataset used for both Python and R analyses
- `linear_regression_python.ipynb` – Jupyter Notebook using Python
- `linear_regression_python.html` – HTML export of the Python notebook
- `linear_regression_python.py` - Python scripts
- `linear_regression_python_output.png` - Visualization of model fit
- `linear_regression_r.ipynb` – Jupyter Notebook using R
- `linear_regression_r.html` – HTML export of the R notebook
- `linear_regression_r.r` – R scripts
- `linear_regression_r_output.png` - Visualization of model fit
- `Rplots.pdf` - Combined visualization of model images in the R environment


## Results 
- The regression line shows a clear positive correlation between years of experience and salary.
- R² score (Python): 0.7851515863136573
- Summary output (R):
- Call:
lm(formula = Salary ~ YearsExperience, data = dataset)

Residuals:
    Min      1Q  Median      3Q     Max 
-7540.2 -2564.9  -199.1  2814.8  6230.6 

Coefficients:
                Estimate Std. Error t value Pr(>|t|)    
(Intercept)        29204       4092   7.136 9.84e-05 ***
YearsExperience     8285       1532   5.407 0.000641 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 4680 on 8 degrees of freedom
Multiple R-squared:  0.7852,	Adjusted R-squared:  0.7583 
F-statistic: 29.24 on 1 and 8 DF,  p-value: 0.0006407


---
