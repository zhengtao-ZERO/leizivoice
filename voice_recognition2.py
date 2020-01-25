#!/usr/bin/env python
# -*- coding:utf-8 -*-

from aip import AipSpeech
import time

APP_ID = '***'
API_KEY = '***'
SECRET_KEY = '***'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
start_time = time.time()
ret = client.asr(get_file_content('voices/myvoices8.wav'), 'wav', 16000, {
    'dev_pid': 1537,
})
used_time = time.time() - start_time

print( "used time: {}s".format( round( time.time() - start_time, 2 ) ) )
print('ret:{}'.format(ret))
