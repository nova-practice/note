#-*- coding:utf-8 -*-

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage, LTChar
## 获取文档对象
fp = open("/data/Java开发工程师_张佺佺_吉林大学.pdf", "rb")

## 创建一个与文档关联的解释器
parser = PDFParser(fp)

## PDF文档的对象
doc = PDFDocument(parser)


parser.set_document(doc)

if doc.is_extractable:
	result = fn(doc, *args)

fp.close()