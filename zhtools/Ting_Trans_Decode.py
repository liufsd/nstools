#!/usr/bin/python
#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import re
import os
from langconv import *
rootPath = '/Users/liupeng/work/ting_android/'
lang_path = [ 'Eudict_Ting_Lib', 'Eudict_Ting_French', 'Eudict_Ting_German', 'Eudict_Ting_Spanish']
for pathItem in lang_path:
    print pathItem + ' start '
    lang_full_path = rootPath + pathItem + '/res/values/strings.xml'
    lang_full_tempPath = rootPath + pathItem + '/res/values-zh-rTW/strings.xml'
    infile = open(lang_full_path)
    outfile = open(lang_full_tempPath, 'w')
    for s in infile.readlines():
        s = Converter('zh-hant').convert(s.decode('utf-8'))
        outfile.write(str(s)) 
        # print s
    print pathItem + ' end '

# # 转换繁体到简体
# line = '设置繁体字'
# line = Converter('zh-hans').convert(line.decode('utf-8'))
# line = line.encode('utf-8')
# print line
# 
# 
# # 转换简体到繁体
# line = Converter('zh-hant').convert(line.decode('utf-8'))
# line = line.encode('utf-8')
# print line