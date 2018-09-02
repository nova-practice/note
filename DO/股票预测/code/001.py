from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import  pandas as pd
import numpy as py
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score
from datetime import date

#导入数据
data = pd.read_csv('')
#将headlines合并起来，考虑所有的news
data['combined_news'] = data.filter(regex=('Top.*')).apply(lambda x:''.join(str(x.values)),axis = 1)
#分割测试/训练集
train = data[data['Date']<'2015-01-01']
test = data[data['Date']>'2014-12-31']
#提取特征
feature_extraction = TfidfVectorizer()
X_train = feature_extraction.fit_transform(train['combined_news'].values)
X_test = feature_extraction.transform(test['combined_news'].values)
y_train = train['label'].values
y_test = y_test['label'].values

#训练模型
clf = SVC(probability=True,kernel='rbf')
clf.fit(X_train,y_train)
predictions = clf.predict_proba(X_test)
print('ROC_AUC yieds'+str(roc_auc_score(y_test,predictions[:,1])))