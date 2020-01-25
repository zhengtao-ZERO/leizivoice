#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import record
import voices2text
import text2voices

record.startRecord()
str1 = voices2text.start2text()
str2 = str1
text2voices.speech(str2)


