# Activation Functions

It is a function applied to the neurons in a layer during the prediction.

## Constraints

<ul>
    <li>The function must be continuous and infinite in domain.</li>
    <li>Good activation functions are monotonic, never changing direction</li>
    <li>Good activation functions are nonlinear (they squiggle or turn)</li>
    <li>
        Good activation functions (and their derivatives) should be efficiently computable.
    </li>
</ul>

## Typical activation functions

## Sigmoid

![](/images/sigmoid.png "sigmoid")

## tanh

It is better for hidden layers

![](/images/tanh.png "tanh")

## softmax

for predict a single lable

![](/images/softmax.png "softmax")

## typical configurations output layer

### configuration 1 Predicting raw data into values(no act function)

One case could be people want to train a neural network to transform one matrix into another where the range of output is something is a probability. It means we want the right answer no 0 or 1.

### configuration 2  predicting unrelated (yes/no) probabilities(sigmoid)

If we want to make multiple binary probabilities  in one neural network, it’s best to use the sigmoid activation function, because it models individual probabilities separately for each output node.

### configuration 3 predicting which-one probabilities(softmax) [chapter 9]

The most common use of neural networks is predicting a single label out of many. softmax asks, “Which digit seems like the best fit for this input?" softmax raises each input value exponentially and then
divides by the layer’s sum.



