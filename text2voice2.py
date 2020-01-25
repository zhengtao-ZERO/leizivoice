#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Hello, it works,anymore! 我在北京科技馆")