# plugml
easy-to-use and highly modular machine learning framework based on scikit-learn with postgresql data bindings

## why plugml
* focus on the main problems, i.e. the machine learning, not the data munging
* supports many use cases out of the box, e.g. document retrieval, document similarity
* simply define the structure of your SQL table and automatically get your data
* no boilerplate code anymore for handling your numerical, categorical and text features
* high modularity allows to easily plug your custom algorithms; no fighting against the framework
* decouple your production code from the utilized machine learning techniques with SQL as loose interface

## features
* directly load data from a SQL table, no more boilerplate code
* easy data preprocessing and filtering with user-defined functions
* out-of-the-box support for numerical, categorical and text features
* high performance as it utilizes scikit-learn, sparse scipy matrices, ...
* plug your custom feature extractors with minimal effort
* automatic feature scaling and imputation
* dimensionality reduction supporting very large features
* kNN queries

## planned
* feature weights
* unit tests
* documentation
* dao write
* supervised ml
* autoencoders
* ...

## get started (to be improved)
1. load data with dao
2. define data
3. define features
4. combine in extractor
5. compress features
6. load in KNN

## notes
currently still under heavy development
