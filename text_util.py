# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 9:10:00 2018

@author: JockJo
"""

import os
import log_util
import shutil
import re
import nltk
from nltk.corpus import stopwords

class TEXTUTIL():
    log_filename = 'text_log'
    log_filepath = './'
    l = log_util.Log(log_filename,log_filepath)

    def __init__(self, rootdir=None, target_path=None, finish_path=None):
        if rootdir is None:
            print('[dir error] text root is none')
        if finish_path is None:
            print('[dir error] text finish path is none')
        self.target_path = r'/media/jockjo/data/parser' if target_path is None else target_path
        self.rootdir = rootdir
        self.finish_path = finish_path

    def parse_single_text(self, text_path, target_path, filename):
        try:
            f = open(text_path, 'r+')
            text_str = f.read()

            #全部转小写
            text_str = text_str.lower()
            #去除非英文字母
            text_str = re.sub(r'[^a-zA-Z ]*', '', text_str)
            #去除非单词
            text_str = re.sub(r' [a-zA-Z] ', ' ', text_str)
            #英文分词
            text_list = nltk.word_tokenize(text_str)
            #词形还原
            filtered = nltk.stem.WordNetLemmatizer()
            text_list = [filtered.lemmatize(w) for w in text_list]
            #词根还原
            filtered = nltk.PorterStemmer()
            text_list = [filtered.stem(w) for w in text_list]
            #去除停用词
            text_list = [w for w in text_list if (w not in stopwords.words('english'))]

            text_fdlist = nltk.FreqDist(text_list)
            #画出前30词频
            text_fdlist.plot(100)

            #清洗后的数据输出到制定目录
            f = open(target_path, 'w+')
            print(text_list,file=f)
        except Exception as e:
            print(e)


    def parse_texts(self):
        try:
            for parent,dirnames,filenames in os.walk(self.rootdir):
                for filename in filenames:
                    #filename包含文件后缀
                    text_path = self.rootdir + "//" + filename
                    text_finish_path = self.finish_path + "//" + filename
                    target_path = self.target_path + "//" + filename
                    self.parse_single_text(text_path, target_path, filename)
                    shutil.move(text_path, text_finish_path)
                    print('success parser {}'.format(filename))
        except Exception as e:
            self.l.print_log(e)


if __name__=='__main__':
    rootdir = '/home/jockjo/Desktop/parser/text'
    finish_path = '/home/jockjo/Desktop/parser/finish'
    target_path = '/home/jockjo/Desktop/parser/target'

    t = TEXTUTIL(rootdir, target_path, finish_path)
    t.parse_texts()
