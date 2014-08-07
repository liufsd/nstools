#!/usr/bin/python
#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import re
import os
from langconv import *
rootPath = '/Users/liupeng/work/Eudic_ting_iOS/Eudic_ting_iOS/Eudic_ting_iOS/'
lang_full_path = rootPath +"zh-Hans.lproj/"+ 'copy_Localizable.strings'
lang_full_tempPath = rootPath +"zh-Hant.lproj/"+ 'temp_Localizable.strings'
infile = open(lang_full_path)
outfile = open(lang_full_tempPath, 'w')
print "start"
for s in infile.readlines():
    # print s
    index = s.find('=')
    print index
    if index ==-1:
        print "not found"
    else:
        print s
        leftstr = s[0:index+1]
        print leftstr
        rightstr =  s[index + 1:]
        print rightstr
        rightstr = Converter('zh-hant').convert(rightstr.decode('utf-8'));
        s = leftstr + rightstr
        # print "got here"
        # print s
    print "============"
    outfile.write(str(s))
print "end"
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