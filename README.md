# Author: Meng Fang
# Date: 10 Nov 2015

There are three different parts: multi-tracker, uwb and miband. 

Before runing. Please make sure that you have installed scikit-learn.

## 1, multi-tracker: it is implemented for presence tracking for multiple residents (here, we have 2 residents).

### How to run?
```sh
$ python multiTracker_NB.py
```

It is used for runing trackers implemented by NB.
```sh
$ python multiTracker_HMM.py
```
It is used for running trackers implemented by HMM.


## 2, uwb: it is used for testing uwb data.

### How to run?
If you have train data and test data then use
```sh
$ python classification4uwb.py train test
```
train is the file name of the train data. test is the file name of the test data.

If you have a dataset and want to do CV (here, we use 3 folds cv) then use
```sh
$ python classification_CV4uwb.py data
```

data is the file name of input data.

If you have a dataset and want to do PCA for selecting features then use
```sh
$ python classification_PCA4uwb.py data 3
```

data is file name of the input data. 3 is the number of selected features. Here, we also use 3 folds cv.


## 3, miband: it is used for testing miband data.
It contains three precedures: download data from remote mysql server, format the raw data and test the data.

To download data from remote mysql server, please use
```sh
$ python getDataFromDB.py "select .. where .. " rawdata
```

The "select .. where .. " should be replaced by your query string according to your requirements. rawdata is the file name of output file.

To format the raw data, please use
```sh
$ python preprocessData.py labels rawdata newdata
```

labels is the file name of labels. rawdata is the file name of rawdata (from mysql). newdata is the file name of output file.

To test the data, please use
```sh
$ python test4miband.py data
```
data is the file name of the input data. 

In this testing, there are two algorithms implemented: one is maximal value and another one is nb-histogram.
 