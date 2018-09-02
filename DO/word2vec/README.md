### 一.下载数据
中文维基百科数据:

[https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2](https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2)
### 二.处理bz2文件
```
python process_wiki.py /home/zhangquanquan/Documents/data/zhwiki-latest-pages-articles.xml.bz2 /home/zhangquanquan/Documents/data/wiki.zh.text
```
> 大约20分钟

### 三.繁转简
opencc -i wiki.zh.text -o wiki.zh.text.jian -c t2s.json

> 大约半小时

### 四.训练
[中英文维基百科语料上的Word2Vec实验](http://www.52nlp.cn/%E4%B8%AD%E8%8B%B1%E6%96%87%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91%E8%AF%AD%E6%96%99%E4%B8%8A%E7%9A%84word2vec%E5%AE%9E%E9%AA%8C)

预料文件: wiki.zh.text.jian

```
python train_word2vec.py  ../../../data/wiki.zh.text.jian  ../../../data/wiki.text.model   ../../../data/wiki.text.vector

# out
 collected 26755795 word types from a corpus of 73306087 raw words and 321991 sentences
2018-09-02 15:05:07,421: INFO: Loading a fresh vocabulary
2018-09-02 15:06:02,323: INFO: effective_min_count=5 retains 1096047 unique words (4% of original 26755795, drops 25659748)
2018-09-02 15:06:02,323: INFO: effective_min_count=5 leaves 43312055 word corpus (59% of original 73306087, drops 29994032)
2018-09-02 15:06:04,895: INFO: deleting the raw counts dictionary of 26755795 items
2018-09-02 15:06:16,305: INFO: sample=0.001 downsamples 10 most-common words
2018-09-02 15:06:16,305: INFO: downsampling leaves estimated 42605188 word corpus (98.4% of prior 43312055)
2018-09-02 15:06:20,689: INFO: estimated required memory for 1096047 words and 400 dimensions: 4055373900 bytes
2018-09-02 15:06:20,689: INFO: resetting layer weights
training model with 4 workers on 1096047 vocabulary and 400 features, using sg=0 hs=0 sample=0.001 negative=5 window=5
saved ../../../data/wiki.text.model
storing 1096047x400 projection weights into ../../../data/wiki.text.vector
词典的大小为1096047

模型文件78M大小
```


#### 训练的流程和算法


### 五.预测
model = gensim.models.word2vec.Word2Vec.load(MODEL_PATH)
In [3]: model = gensim.models.Wor

### 六.问题
词向量表示

表示后用来做什么? 文本相似度\其他...

至于word2vec有什么用，目前除了用来来计算词语相似度外，业界更关注的是word2vec在具体的应用任务中的效果，这个才是更有意思的东东，也欢迎大家一起探讨。
