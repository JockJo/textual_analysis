# -*- coding: utf-8 -*-

import time


class Log():
    f = None
    filename = ''
    filepath = ''

    def __init__(self, filename, filepath):
        store_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.filename = filename
        self.filepath = filepath
        try:
            self.f = open(self.filepath+self.filename+store_time, 'a', encoding='utf-8')
            self.filepath=self.filepath+self.filename+store_time
            self.f.close()
        except Exception as e:
            print(e)

    def print_log(self, data):
        self.f = open(self.filepath, 'a', encoding='utf-8')
        store_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print('[{}]'.format(store_time),data, file=self.f)
#        print('[{}]'.format(store_time),data)
        self.close_log()

    def close_log(self):
        self.f.close()
