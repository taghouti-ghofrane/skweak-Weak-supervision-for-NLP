# Comparison of automatic annotations and the mix between automatic and manual annotations provided by UBIAI

<br>
<p align="center">
   <img alt="skweak logo" src="https://github.com/taghouti-ghofrane/skweak-Weak-supervision-for-NLP/blob/main/data/logo.png"/>
</p><br>

# Automatic annotations
In the last few years, the real impact of machine learning (ML) has increased significantly.
in large part, this is due to the advent of deep learning models, which allow practitioners to get state-of-the-art scores on benchmark datasets without any hand-engineered features.

There is a hidden catch, however: the reliance of these models on massive sets of hand-labeled training data.

Manually labeled training sets are costly and time consuming to create .
for these reasons , practitioners have increasingly been turning to **weak supervision**, such as heuristically generating training data with external knowledge bases, patterns/rules, or other classifiers. Essentially, these are all ways of programmatically generating training data—or, more succinctly, programming training data.

## What's Weak Supervision !

Weak supervision is an emerging machine learning paradigm based on a simple idea: instead of labeling data points by hand, we use labeling functions derived from domain knowledge to automatically obtain annotations for a given dataset.

**skweak**  is a Python-based software toolkit for weak supervision. skweak is built around a very simple idea: I we define a set of **labelling functions** to automatically label our documents, and then **aggregate** their results to obtain a labelled version of our corpus.

# UBIAI Easy to Use Text Annotation Tool

UBIAI labeling tool offers the option to auto-annotate your documents by using dictionaries and an ML model.

You can easily auto-label your data by defining rules, dictionaries, and regular expressions with no code required and minimize hand annotation by 80%.

# The limits of Weak supervision

Based on the project **Job_Description** , we made a comparaison between two modeles.

* Skweak model evaluation :

```
                     P       R       F
DIPLOMA         100.00   11.11   20.00
DIPLOMA_MAJOR    50.00   33.33   40.00
EXPERIENCE      100.00   27.27   42.86
SKILLS           31.46   16.97   22.05

```

* UBIAI model evalution :

```

                    P       R       F
DIPLOMA         85.71   66.67   75.00
DIPLOMA_MAJOR   33.33   16.67   22.22
EXPERIENCE      81.82   81.82   81.82
SKILLS          74.05   83.03   78.29
```

*