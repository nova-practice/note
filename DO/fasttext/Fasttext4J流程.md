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

### 1. 获取句子的特征
(List<Integer> lineWords)   wid

1. 先获取句子的token字符数组
2. 然后获取特征,有以下几种

- substring ,其中包含自己
- ngram

> 默认参数ngram n=1 ,也就是不取ngram 特征.

> minn\maxn 为0, 也就是说也不取子字作为特征.

dim 默认为100.
> 问题: 子字,是指 子串字在词典中存在,还是说只要是词语的子串就行??? 比如交易- 交\易\交易

### 2. lineWords作为输入,预测
int[] input = lineWords;
初始化:Vector hidden,Vector output

- computeHidden  算出hidden.

然后根据loss类型选择最后处理,默认类型是SOFTMAX.

- computeOutputSoftmax(hidden, output)

- 把结果放到 MinMaxPriorityQueue<Pair<Float, Integer>> heap

- 取k个结果返回.

> 问题:1. input数组 作为输入,在隐层,输出的计算过程. 2. softmax回归过程.


