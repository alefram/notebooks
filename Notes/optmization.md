# Optimization 

Are algorithms that enable models to learn from data by adapting their parameters and reduce de measures of mistakes made by the model. 

## Notation 

**Parameters:** \theta in R^{n}

**Objective function:** h(\theta)

**Goal:**  \theta^{*} = arg min h(\theta) 
  
## Standart Neural Network training objective

h(\theta) = \frac{1}{m}\sum^{m}_{i=1}l(y_{i},f(x_{i},\theta))

where

l(y,z) is a loss function to measure disagreement between y and z. The
f(x,\theta) is a neural network taking input x and giving a prediction.

## Some optimizations methods deterministics

1) gradient descend
2) momentum method
3) 2nd-order method

## Some optimizations methods stochastics

 1) Stochastic gradient descent


# Usefull resources

<ul>
    <li>Numerical Optimization (Nocedal & wright)</li>
    <li>
        Introductory Lectures on Convex Optimization: A Basic Course (Nesterov)
    </li>
</ul>
