# Calculating the variance

In the previous exercise, we estimated the variance for a uniform random variable using:

![](https://render.githubusercontent.com/render/math?math=S^2=\frac{1}{n}\sum_{i=1}^{n}[X_i-\mathbb{E}(X)]^2

Furthermore, we showed that this quantity converged towards a particular value as n increased.  In this exercise, however, I would like you to estimate the variance for a sample mean that is itself calculated from m random variables.  In other words, I want you to write a function to generate:

![](https://render.githubusercontent.com/render/math?math=S^2=\frac{1}{n}\sum_{i=1}^n\left[\frac{1}{m}\left(\sum_{j=1}^{m}X_{ij}\right)-\mathbb{E}(X)\right]^2)

In this expression, the ![](https://render.githubusercontent.com/render/math?math=X_{ij}) are all uniform random variables that lie between 0 and 1 so ![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(X)) is still 0.5 because, as we learned last week the expectation of a sample mean computed from m identical random variables is the same as the expectation of the underlying random variable.  To get you started with this task I have written two functions, which you should complete:

1. `sample_mean` - takes a single integer `m` in input.  It should return a sample mean that is computed by generating `m` uniform random variables that lie between 0 and 1.
2. `variance` - takes two integers in input `m` and `n`.  This function should return an estimate of the variance for a sample mean computed from `m` uniform random variables that lie between 0 and 1.  This variance should be calculated by generating `n` estimates of the sample mean.
