
### Learning rate
Why do we need warm up for the learning rate?

[Reference](https://stackoverflow.com/questions/55933867/what-does-learning-rate-warm-up-mean)
If your data set is highly differentiated, you can suffer from a sort of "early over-fitting". If your shuffled data happens to include a cluster of related, strongly-featured observations, your model's initial training can skew badly toward those features -- or worse, toward incidental features that aren't truly related to the topic at all.

Warm-up is a way to reduce the primacy effect of the early training examples. Without it, you may need to run a few extra epochs to get the convergence desired, as the model un-trains those early superstitions.

Many models afford this as a command-line option. The learning rate is increased linearly over the warm-up period. If the target learning rate is p and the warm-up period is n, then the first batch iteration uses 1*p/n for its learning rate; the second uses 2*p/n, and so on: iteration i uses i*p/n, until we hit the nominal rate at iteration n.

This means that the first iteration gets only 1/n of the primacy effect. This does a reasonable job of balancing that influence.

Note that the ramp-up is commonly on the order of one epoch -- but is occasionally longer for particularly skewed data, or shorter for more homogeneous distributions. You may want to adjust, depending on how functionally extreme your batches can become when the shuffling algorithm is applied to the training set.