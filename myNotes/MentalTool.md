# Mental tool for remember basic concepts

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



