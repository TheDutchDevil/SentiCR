
# SentiCR

SentiCR is an automated sentiment analysis tool for code review comments originally developed by Ahmed et al. and published on [GitHub](https://github.com/senticr/SentiCR). 

SentiCR uses supervised learning algorithms to train models based on 1600 manually label code review comments (https://github.com/senticr/SentiCR/blob/master/SentiCR/oracle.xlsx). Features of SentiCR include:

- Special preprocessing steps to exclude URLs and code snippets
- Special preprocessing for emoticons
- Preprocessing steps for contractions
- Special handling of negation phrases through precise identification 
- Optimized for the SE domain 

This fork of SentiCR ports SentiCR to Python 3.8 (Based on the work by [eslerd](https://github.com/eslerd/SentiCR)), and makes SentiCR available as a package. Hopefully allowing for easier usage and retraining of SentiCR. 

## Getting started

To use this fork of SentiCR you have to install the package using pip, and then you can use the SentiCR class as exposed by the package. 

`pip install git+https://github.com/TheDutchDevil/SentiCR.git`

```
from SentiCR import SentiCR

senti = SentiCR()

senti.get_sentiment_polarity("This code frankly sucks!")
```


## Performance
In the hundred ten-fold cross-validations performed by the original authors, SentiCR achieved 83.03% accuracy (i.e., human level accuracy), 67.84% precision, 
58.35% recall, and 0.62 f-score on a Gradient Boosting Tree based model. Detailed cross validation results can be found in the original repository included here: 
https://github.com/senticr/SentiCR/tree/master/cross-validation-results

## Cite

Ahmed, T. , Bosu, A., Iqbal, A. and Rahimi, S., "SentiCR: A Customized Sentiment Analysis Tool for Code Review Interactions", In Proceedings of the 32nd IEEE/ACM International Conference on Automated Software Engineering (NIER track).

```
@INPROCEEDINGS{Ahmed-et-al-SentiCR,

 author = {Ahmed, Toufique and Bosu, Amiangshu and Iqbal, Anindya and Rahimi, Shahram},
 
 title = {{SentiCR: A Customized Sentiment Analysis Tool for Code Review Interactions}},
 
 year = {2017},
 
 series = {ASE '17},
 
 booktitle = {32nd IEEE/ACM International Conference on Automated Software Engineering (NIER track)}, 
}
```