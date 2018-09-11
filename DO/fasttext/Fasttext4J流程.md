1. 从词典中获取 输入词 的 word2int 值. lineWords,  



获取这句话的所有单词(word) 
> tokenList
遍历 tokenList


由word & hash(word)  得到 wid 
如果wid大于0 的wid ,放到 lineWords
否则: 不会放到 lineWords.    [过滤掉一些没有用的特征]

上一步会生成每个word 的 hash(word), 大小和tokenList的大小一致.


根据  wordHashes, ngram的个数(2)  .  addWordNGrams.
通过addWordNGrams  向 lineWords 加如一些特征.     新加的个数为 tokenList 的大小.


用特征List去预测.
> lineWords

hidden 向量大小为 指定 dim大小
output 向量大小为 label个数大小

构造MinMaxPriorityQueue

computeHidden(input, hidden);  // 根据 输入(lineWords) 得到hidden 层向量

computeOutputSoftmax(hidden, output);  // 根据 hidden层向量,得到 output