# -*- encoding: utf-8 -*-

from pyfasttext import FastText
classifier = FastText('/opt/app/fasttext/geek-model-v1.bin') 

texts = ['我 是 温涛 发   温总 ， 最近 招聘 有 什么 新 的 进展 吗 ？', '我 新建 个 QQ 工作 群 ， 以后 工作 的 事情 可以 在 群里 讨论 ， 你加 一下']

#classifier = fasttext.load_model('/opt/app/fasttext/geek-model-v1.bin')

print 'load model success.'

labels = classifier.predict_proba(texts, 1)

print labels


中文输入哈哈哈