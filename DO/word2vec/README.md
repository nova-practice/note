### 下载数据
中文维基百科数据:

[https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2](https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2)
### 处理bz2文件
```
python process_wiki.py /home/zhangquanquan/Documents/data/zhwiki-latest-pages-articles.xml.bz2 /home/zhangquanquan/Documents/data/wiki.zh.text
```
> 大约20分钟

### 繁转简
opencc -i wiki.zh.text -o wiki.zh.text.jian -c t2s.json

> 大约半小时