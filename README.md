# Williams test

Significance test of increase in correlation for NLP evaluations in python

## Prerequisites
* python3
* numpy, scipy


## Usage

To run a one-sided application of Williams Test to test the significance of the increase in correlation between r12 and r13 below, with sample size n, where

- r12: Pearson correlation between Human scores and metric A, 
- r13: Pearson correlation between Human scores and metric B,
- r23: Pearson correlation between metric A and metric B. 

This returns the p-value for the test that r12 is greater than r13.

For example, Williams test with the following:

```
$ python3 williams.py --r12 0.65 --r13 0.55 --r23 0.3 --n 50
```

Will produce the following output:

```
-----------------------------------------
Williams Test for Increase in Correlation

    r12 correlation( Human, metric A ) : 0.65
    r13 correlation( Human, metric B ) : 0.55
    r23 correlation( metric A, metric B) : 0.3

    Sample size: 50

P-value: 0.20928617286753592
-----------------------------------------
```

Since p > 0.05, the increase in correlation is **not** significant. 


---
### Reference

1. https://github.com/ygraham/nlp-williams
2. Yvette Graham & Timothy Baldwin. "Testing for Significance of Increased Correlation with Human Judgment", EMNLP 2014.
