# Basic concepts


## what is a input data?

"It’s a number that you recorded in the real world somewhere". andrew trask

## what is a prediction?

"A prediction is what the neural network tells you". It not always is right but it can learn from it. It can predict with multiple inputs and multiple outputs 

## what is a weight?

It is like the sensitive of the net. When you train the neural net it means to adjust the weights for have an accurate prediction how we can do it?

The objective of build a neural network is to compute a error function with a bunch of weight. Then you will have a relationship of the error and the weight of the network and with that information, you can change the weight to reduce the error to 0.

You will  use the alpha variable to reduce weight update so it doesn’t overshoot.

## Learning methods

Hot and cold: it consist on wiggling the weight to see when it reduce the error

gradient descent: it consist on to find the minimums error for learning.

Exists 3 gradient descent. When we talk about stochastic gradient descent, it updates the weights one example at the time. The full gradient descent, it updates one dataset at the time. Batch gradient descent, in this case you choose a batch size for updates the weight. 

## Overfitting

"Error is shared among all the weights. If a particular configuration of weights accidentally creates perfect correlation between the prediction and the output dataset without giving the heaviest weight to the best inputs, the neural network
will stop learnin". andrew trask

The greatest challenge is convincing my neural network to generalize instead of just memorize

##  Backpropagation

It consist  on moving delta around to take a correlation of input and output. More technicaly it is about calculating deltas for intermediate layers for perform gradient descent 


## tips regularizations(ignore noise)

<ul>
    <li>neural networks find and create correlation</li>
    <li>stop training the NN when it getting worse to dont overfit</li>
    <li>
        use validation dataset for see when to stop train the neural net
    </li>
    <li>
        dropout: radomly turn off the neurons(set them to 0) during training (multiply the layer values by a random matrix of 1s and 0s)
    </li>
    
    


</ul>

## Correlation summarization

"Neural networks seek to find direct and indirect correlation between an input layer and an output layer, which are determined by the input 
and output datasets, respectively". andrew Trask

## Local Correlation summarization

"Any given set of weights optimizes to learn how to correlate its input layer with what the output layer says it should be." andrew Trask

## Global correlation summarization

"What an earlier layer says it should be can be determined by taking what a later layer says it should be and multiplying it by the weights in between them. This way, later layers can tell earlier layers what kind of signal they need, to ultimately find correlation with the output. This cross-communication is called backpropagation." andrew Trask

## notation
<ul>
    <li>
        I0W0: Take the layer 0 vector and perform vector-
        matrix multiplication with the weight matrix 0.”
    </li>
    <li>
        l1 = relu(l0W0): To create the layer 1 vector, take the layer 0 vector and perform vector-matrix multiplication with the weight matrix 0; then perform the relu function on the output (setting all negative numbers to 0).
    </li>
</ul>



