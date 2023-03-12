# Scaled Dot-Product Attention


## Introduction
Scaled Dot-Product Attention is an attention mechanism that maps a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key. It is used in the Transformer architecture, a sequence transduction model based entirely on attention, which replaces the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention. The Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers, and has achieved a new state of the art BLEU score of 28:4 on both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks.

## Multi-Head Attention
Multi-Head Attention consists of several attention layers running in parallel. It allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this. The multi-head attention is computed as a concatenation of the attention heads, with each head being a scaled dot-product attention with projections of the query, keys, and values of dimension dk, dk, and dv respectively.

## Attention Function
The two most commonly used attention functions are additive attention and dot-product (multiplicative) attention. Dot-product attention is identical to the scaled dot-product algorithm, except for the scaling factor of 1/dk. Additive attention computes the compatibility function using a feed-forward network with a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code. The feed-forward network consists of two linear transformations with a ReLU activation in between, and the dimensionality of input and output is dmodel = 512, and the inner-layer has dimensionality dff= 2048.

## Dot-Product Attention
Scaled Dot-Product Attention is an attention function that takes queries and keys of dimension dk, and values of dimension dv. It computes the dot products of the query with all keys, divides each by pdk, and applies a softmax function to obtain the weights on the values.

## Additive Attention
Additive attention computes the compatibility function using a feed-forward network with a single hidden layer. The feed-forward network consists of two linear transformations with a ReLU activation in between, and the dimensionality of input and output is dmodel = 512, and the inner-layer has dimensionality dff= 2048. It is used in the Transformer architecture, which can be trained significantly faster than architectures based on recurrent or convolutional layers, and has achieved a new state of the art BLEU score of 28:4 on both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks.