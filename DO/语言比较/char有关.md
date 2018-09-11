## java和C++ 中的char 

java中的char 只针对java使用, 表示一个字符, 是String的组成. 在java内部(JVM运算),都是用unicode 表示.也就是两个字节.

> ps : 打印日志的编码怎么算


如果转换成byte,落地,比如打印日志, 就和文件编码有关.  
如果文件编码是UTF-8,那就是3个字节.
如果是GBK,那就是2个字节

