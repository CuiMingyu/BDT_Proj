# Twitter Analysis

A project about Twitter Analysis of Big data course

## Goal

Our goal is to find a more efficient way to figure out Twitter uses who obtain a huge influence on others by using big data techniques.

### Prerequisites & Reading materials

Python3.5 Tensorflow TWINT

```
pip install python3
```

Some papers

```

SIGMOD
Robust, Scalable, Real-Time Event Time Series Aggregation at Twitter.

SIGKDD
Dynamic Embeddings for User Profiling in Twitter. 

ICDE
Predicting Named Entity Location Using Twitter.

SIGIR
The Evolution of Content Analysis for Personalized Recommendations at Twitter.

AAAI
Twitter Summarization Based on Social Network and Sparse Reconstruction.
Cooperative Multimodal Approach to Depression Detection in Twitter.

IJCAI
A Comparative Study of Transactional and Semantic Approaches for Predicting Cascades on Twitter.
Automatic Opioid User Detection from Twitter: Transductive Ensemble Built on Different Meta-graph Based Similarities over Heterogeneous Information Network.

EMNLP
Exploring Optimism and Pessimism in Twitter Using Deep Learning. 
Transferring from Formal Newswire Domain with Hypernet for Twitter POS Tagging.

CIKM
Causal Dependencies for Future Interest Prediction on Twitter. 
An Effective Approach for Modelling Time Features for Classifying Bursty Topics on Twitter.

ACL
ClaimPortal: Integrated Monitoring, Searching, Checking, and Analytics of Factual Claims on Twitter
A web server monitoring real things in twitter.

Multi-Modal Sarcasm Detection in Twitter with Hierarchical Fusion Model
Sarcasm detection by triple models.

Twitter Homophily: Network Based Prediction of User’s Occupation
Using GCN to exploit homophily to predict occupation.

Categorizing and Inferring the Relationship between the Text and Image of Twitter Posts
Judge four relationships of image and text.

EMNLP
Exploring Optimism and Pessimism in Twitter Using Deep Learning

NAACL
Deep Learning for Depression Detection of Twitter Users.
Only consider text of users which have completely dataset.
```

```
Main Idea:
Based on user's actions and tweets to decide whether a user has potential depression.
```


### Procedure

A step by step series of whole procedure that tell you how to finish Twitter analysis.



```
1. Prepare dataset. Plan to crawl 10,000 users in Twitter and 100 tweets of each user and 'following & follower' of each user.

2. Cleaning data and build relation entries of users. Delete some words like 'the', 'a' and some useless blanks. Store user information in database.
```
## Timeline of class

Nov. 5 Proposal

Dec. 3 Proj pre

## Timeline of our progress

* ### Oct. 5 - 11 (researching week & running models)

1. Crawl data : 2 person (needs same as the aaai paper data format)
2. text model : 1 per
3. graph model : 1 per
4. follower/following : 1 per

* ###Oct. 12 - 18 (coding week & combining code)

1. Data part : Washing data &  Splicing data format (1 per)
2. Define api : 1 per
3. Text model coding : 1 per
4. Graph model coding : 1 per 
5. Follower/following coding : 1 per

* ###Oct. 19 - 28 (Combining week & runing model)

We need to combine all code and fix bugs.

* ###Oct. 29 - Nov. 5 (Writing week)

Writing proposal.

* ###Nov. 6 -

Find tricks which can improve our performances.




## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Cui Mingyu** 
* **Li Zenan**
* **Liu Yanyan**
* **Su Linyin**
* **Xu Jiangyue**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration: We need pay more attention on those who has a depression experience.

