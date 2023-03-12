# Dot-Product Attention


## Introduction
Dot-Product Attention is an attention mechanism that relates different positions of a single sequence in order to compute a representation of the sequence. It is used in a variety of tasks such as reading comprehension, abstractive summarization, textual entailment, and learning task-independent sentence representations.

## Scaled Dot-Product Attention
Scaled Dot-Product Attention is a particular attention function that maps a query and a set of key-value pairs to an output. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key. The input consists of queries and keys of dimension dk, and values of dimension dv. The output is computed as a matrix of outputs as: Attention(Q;K;V ) = softmax(QKTpdk)V. The dot product of the query and key, qk=Pdk
i=1qiki, has mean 0 and variance dk. MultiHead( Q;K;V ) = Concat(head 1;:::;head h)WO, where head i= Attention( QWQ
i;KWK
i;VWV
i). The projections are parameter matrices WQ
i2Rdmodeldk,WK
i2Rdmodeldk,WV
i2Rdmodeldv
andWO2Rhdvdmodel. The Transformer model uses dot-product attention in three different ways: encoder-decoder attention layers, self-attention layers in the encoder, and self-attention layers in the decoder.

## Multi-Head Attention
Multi-Head Attention consists of several attention layers running in parallel. Instead of performing a single attention function with dmodel-dimensional keys, values and queries, Multi-Head Attention linearly projects the queries, keys and values h times with different, learned linear projections to dk, dk and dv dimensions, respectively. On each of these projected versions of queries, keys and values, the attention function is performed in parallel, yielding dv-dimensional output values. These are concatenated and once again projected, resulting in the final values. In this work, h is set to 8 parallel attention layers, or heads, with dk=dv=dmodel=h= 64 .

## Dot-Product Attention vs. Additive Attention
Dot-product attention is identical to the Scaled Dot-Product Attention algorithm, except for the scaling factor of 1/pdk. Additive attention computes the compatibility function using a feed-forward network with a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code. For small values of dk, the two mechanisms perform similarly, but additive attention outperforms dot product attention without scaling for larger values of dk.

## Benefits of Dot-Product Attention
Dot-Product Attention reduces the number of operations required to relate signals from two arbitrary input or output positions to a constant number of operations. It is faster and more space-efficient than additive attention, and allows the model to jointly attend to information from different representation subspaces at different positions. It has been shown to be effective in tasks such as machine translation, where it has been used to achieve state-of-the-art results on the WMT 2014 English-to-German and English-to-French translation tasks. It has also been used to reduce training time and improve accuracy on tasks such as language modeling and question answering. Additionally