args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

library(ggplot2)

dataset <- read.csv("regression_data.csv")
x <- dataset$YearsExperience
y <- dataset$Salary

lr.model <- lm(y ~ x)

slope <- coef(lr.model)[2]
intercept <- coef(lr.model)[1]
r <- cor(x, y) #Pearson correlation coefficient
y_pred <- predict(lr.model)

mse <- mean((y - y_pred)^2)

cat(sprintf("Slope (m):%.4f\n", slope))
cat(sprintf("Intercept (b):%.4f\n", intercept))
cat(sprintf("Correlation Coefficient (r):%.4f\n", r))
cat(sprintf("Mean Squared Error (MSE):%.4f\n", mse))

plot <- ggplot(dataset, aes(x = YearsExperience, y = Salary)) +
  geom_point(color = "red") +
  geom_smooth(method = "lm", se = TRUE, color = "blue") +
  annotate("text", x = min(x), y = max(y),
           label = paste("y =", round(slope, 2), "x +", round(intercept, 2),
                         "\nr =", round(r, 2)),
           hjust = 0, vjust = 1, size = 4, color = "blue") +
  ggtitle("Linear Regression: Salary vs. Years of Experience") +
  xlab("Years of Experience") +
  ylab("Salary")

ggsave("regression_plot_r.png", plot)
print(plot)

summary(lr.model)
