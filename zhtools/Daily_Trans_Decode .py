#!/usr/bin/python
#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import re
import os
from langconv import *
rootPath = '/Users/liupeng/work/daily_android/'
lang_path = [ 'Daily_Lib', 'Daily_Fr', 'Daily_Es', 'Daily_De']
for pathItem in lang_path:
    print pathItem + ' start '
    lang_full_path = rootPath + pathItem + '/res/values/strings.xml'
    tempTargetDictPath =  rootPath + pathItem + '/res/values-zh-rTW/'
    if not os.path.exists(tempTargetDictPath):
        os.makedirs(tempTargetDictPath)
    lang_full_tempPath = tempTargetDictPath + 'strings.xml'
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