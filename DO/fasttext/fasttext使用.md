## fasttext使用

fasttext  


词15个,字符 38个,包含空格

遍历每一个词,   




目前的招聘, 就拿两个群体说.国企事业单位人员,对于一些职称证书看重.对于类似互联网行业的白领,则更看重技能,看能否胜任.随着发展趋势,体制内的可能会更加看重实际技能,不仅仅是偏差可能比较大的考试考核.
互联网行业会更加全方位的获取一个人的各种能力,不仅仅一张简历和3场面试.而是构建求职者的人物画像,以达到精确匹配.所以当然也不是流程会更繁琐,而是更加快速


charMatches method invoke by computeSubwords . char in java has 2 byte, i think this wil skip over some chinese word , because char use unicode characters in java , include chinese word . so i think

protected boolean charMatches(char c) { 
    return (c & 0xC0) == 0x80; 
}
should be

protected boolean charMatches(char c) { 
    return c >=128 && c <=191; 
}