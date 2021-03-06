# plugml
easy-to-use and highly modular machine learning framework based on scikit-learn with postgresql data bindings

## why plugml
* focus on the main problems, i.e. the machine learning, not the data munging
* supports many use cases out of the box, e.g. document retrieval, document similarity
* simply define the structure of your SQL table and automatically get your data
* no boilerplate code anymore for handling your numerical, categorical and text features
* high modularity allows to easily plug your custom algorithms; no fighting against the framework
* plugml is used for prototyping models for our production app, so it is part of the lifecycle of an actually used product

## features
* directly load data from a SQL table, no more boilerplate code
* easy data preprocessing and filtering with user-defined functions
* out-of-the-box support for numerical, categorical and text features
* high performance as it utilizes scikit-learn, sparse scipy matrices, ...
* plug your custom feature extractors with minimal effort
* automatic feature scaling and imputation; custom weights
* dimensionality reduction supporting very large features
* kNN queries

## roadmap
### v0.3
* theanets autoencoders as compressors (feed-forward)

### v0.4
* theanet recurrent autoencoder
* use recurrent autoencoder for nlp instead of bag of wards (or rather provide option)

### v0.5
* introduce labels to data
* infrastructure for supervised ml

### v0.6
* theanets rnns for regression/classification

## long-term ideas
* automatic data extraction based on sql schema
* intelligent application of ml techniques based on data structure
* auto-identify semantic entities and relationships from data structures
* (match natural language queries to ml-specific actions, i.e. non-ml specialist interface to data analysis)

## get started (to be shown in ipynb)
1. load data with dao
2. define data
3. define features
4. combine in extractor
5. compress features
6. load in KNN

## notes
subject to signifant changes until at least v1.0
