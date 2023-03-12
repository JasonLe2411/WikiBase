# Self-Attention


## Introduction
Self-attention, also known as intra-attention, is an attention mechanism that relates different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations, as the model learns to be more unsure, but improves accuracy and BLEU score.

## Multi-Head Attention
Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. It consists of several attention layers running in parallel, with each layer having queries, keys and values of dimension dk,dk and dv respectively. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key. In this work, the model employs 8 parallel attention layers, or heads, with dk,dv and dmodel all equal to 64.

## Scaled Dot-Product Attention
Scaled dot-product attention is a particular attention function that computes the dot products of the query with all keys, divides each by pdk, and applies a softmax function to obtain the weights on the values. It is much faster and more space-efficient in practice than additive attention, which computes the compatibility function using a feed-forward network with a single hidden layer.

## Additive Attention
Additive attention computes the compatibility function using a feed-forward network with a single hidden layer. It performs similarly to dot-product attention for small values of dk, but outperforms it without scaling for larger values of dk.

## Dot-Product Attention
Dot-product attention is identical to scaled dot-product attention, except for the scaling factor of 1/pdk. It has a theoretical complexity similar to additive attention, but is much faster and more space-efficient in practice. The Transformer uses multi-head attention in three different ways: in "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder; the encoder contains self-attention layers, where all of the keys, values and queries come from the same place; and self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers and achieves a new state of the art. Additionally, the Transformer can be used for tasks such as abstractive summarization, language modeling, and learning task-independent sentence representations.