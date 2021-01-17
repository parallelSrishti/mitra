import nltk
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix,classification_report
import pickle
from sklearn import metrics
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix,classification_report
import joblib
def train_model_results():
    train = pd.read_csv("./train.txt", delimiter=';', header=None, names=['sentence','label'])
    test = pd.read_csv("./test.txt", delimiter=';', header=None, names=['sentence','label'])
    val = pd.read_csv("./val.txt", delimiter=';', header=None, names=['sentence','label'])
    df_data = pd.concat([train, test,val])
    df_data.to_csv (r'exportdata.txt', index=False)
    dt_data =  pd.read_csv("exportdata.txt")
    token = RegexpTokenizer(r'[a-zA-Z0-9]+')
    cv = CountVectorizer(stop_words='english', ngram_range=(1,1), tokenizer = token.tokenize)
    text = cv.fit_transform(dt_data['sentence'])

    # train test split
    X_train, X_test, y_train, y_test = train_test_split(text,dt_data['label'], test_size=0.30, random_state=5)

    # get the shape of train and test split.
    X_train.shape, X_test.shape, y_train.shape, y_test.shape
    mnb = MultinomialNB()
    mnb.fit(X_train, y_train)
    predicted = mnb.predict(X_test)

    acc_score = metrics.accuracy_score(predicted,y_test)
    prec_score = precision_score(y_test,predicted, average='macro')
    recall = recall_score(y_test, predicted,average='macro')
    f1 = f1_score(y_test,predicted,average='macro')
    matrix = confusion_matrix(y_test,predicted)

    print(str('Accuracy: '+'{:04.2f}'.format(acc_score*100))+'%')
    print(str('Precision: '+'{:04.2f}'.format(prec_score*100))+'%')
    print(str('Recall: '+'{:04.2f}'.format(recall*100))+'%')
    print('F1 Score: ',f1)
    print(matrix)
    #dummy test
    test_data = ['i feel sick','i am ecstatic my model works', 'i feel shitty', 'i feel lost', 'im petrified', 'i am worried']

    test_result = mnb.predict(cv.transform(test_data))

    print(test_result)
    joblib.dump(mnb, 'model.pkl')
    model = open('model.pkl','rb')
    mnb = joblib.load(model)