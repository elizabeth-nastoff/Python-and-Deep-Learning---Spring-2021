from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from sklearn.datasets import fetch_20newsgroups

# chose a couple categories out of the 20 files
categories = ["alt.atheism","sci.med"]
newsgroups_train = fetch_20newsgroups(subset='train', shuffle=True, categories = categories)
newsgroups_test = fetch_20newsgroups(subset='test', shuffle=True, categories = categories)
