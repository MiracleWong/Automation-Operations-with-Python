#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import os, sys
import filecmp
import re
import shutil
import re,sys,os
import time,httplib,urlparse
import traceback
import linecache
## TSDB info
TsdbHost = '172.20.3.15'
TsdbPort = '4242'
TsdbUrl = '/api/put'
## modify the system default encoding
reload(sys)
sys.setdefaultencoding('utf-8')
## log
aoti_log_path="/tmp/aoti.log"
def stat_file(log_path):
    return linecache.getline(log_path, 1)

holderlist=[]

## compare the directories
def compareme(dir1, dir2):
    dircomp=filecmp.dircmp(dir1,dir2)
    only_in_one=dircomp.left_only       ## 源目录新增加的文件
    diff_in_one=dircomp.diff_files      ## 备份目录新增加的文件
    dirpath=os.path.abspath(dir1)       ## 源目录的绝对路径
    ## 将更新的文件名追加到holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in diff_in_one]
    ## 递归子目录
    if len(dircomp.common_dirs) > 0:
        for item in dircomp.common_dirs:
            compareme(os.path.abspath(os.path.join(dir1,item)), \
            os.path.abspath(os.path.join(dir2,item)))
        return holderlist
 
def main():
    timefile=int(time.time())
    # 输入源目录和备份目录
    if len(sys.argv) > 2:
        dir1=sys.argv[1]
        dir2=sys.argv[2]
        site=sys.argv[3]
    else:
        print "Usage: ", sys.argv[0], "datadir backupdir"
        sys.exit()
    ## 源目录和备份目录对比
    source_files=compareme(dir1,dir2)
    source_files1=compareme(dir1,dir2)
    dir1=os.path.abspath(dir1)
 
    if not dir2.endswith('/'): dir2=dir2+'/'   # 加路径符/
    dir2=os.path.abspath(dir2)
    destination_files=[]
    createdir_bool=False

    for item in source_files:           # 遍历返回的差异文件和目录
        destination_dir=re.sub(dir1, dir2, item)    # 源目录差异路径对应替换成差异目录
        destination_files.append(destination_dir)
        if os.path.isdir(item): # 差异路径是目录且不存在，则进行创建
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool=True                   # 函数标记设为True
 
    if createdir_bool:
        destination_files=[]
        source_files=[]
        source_files=compareme(dir1,dir2)
        for item in source_files:
            destination_dir=re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)
 
    fixed_file = []
    # 将源目录差异路径清单，拆分成元组
    copy_pair=zip(source_files,destination_files)
    for item in copy_pair:
        print item
        if os.path.isfile(item[0]):
            print item[0]
            if not os.path.exists('service/backup/cuangai/' + site + str(timefile)):
                os.makedirs('service/backup/cuangai/' + site + str(timefile))
                ofile='service/backup/cuangai/' + site + str(timefile) + '/' + item[0].split('/')[-1]
                shutil.copyfile(item[0], ofile)
            shutil.copyfile(item[1], item[0])
    if copy_pair:
        fixed_file.append ("OK")
    if len(copy_pair):
        return 3,site
    if len(source_files1):
        return 1,site
    else:
        return 2,site
 
if __name__ == '__main__':
    for j in range(0, 3):
        aoti,site = main()
        timestamp=int(time.time())
        time.sleep(20)
        
