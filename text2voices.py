#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import win32com.client

def speech(str):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(str)