import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

spam = pd.read_csv('train.csv')
z = spam['Message_body']
y = spam["Label"]
z_train, z_test,y_train, y_test = train_test_split(z,y,test_size = 0.2)

cv = CountVectorizer()
features = cv.fit_transform(z_train)

model = svm.SVC()
model.fit(features,y_train)

features_test = cv.transform(z_test)
print(model.score(features_test,y_test))

test = pd.read_csv('test.csv')
ytest=test['Message_body']


features = cv.transform(ytest)
pred=model.predict(features)
test['Label']=pred

Submission = test[['Id','Label']]
Submission.to_csv("submission.csv", index=False)