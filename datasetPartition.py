#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#coco
import os
import random
import shutil
 
def movefile(filedir,tardir):
    pathdir=os.listdir(filedir)# old filepath
    filenumber=len(pathdir)
    rate=0.3
    picknumber=int(filenumber*rate)# Get a certain number of files from the dataset according to the rate ratio 
    #print('picknumber:',picknumber)
    samples=random.sample(pathdir,picknumber)# choose picknumber file
    #print('samples:',samples)
 
    count=0
    for sample in samples:# current directory
        print('sample:',sample)
        if sample.endswith(".png"):#check whether png
            shutil.move(filedir+sample,tardir+sample)
            # shutil.move(filedir+os.path.splitext(sample)[0]+'.txt',tardir+os.path.splitext(sample)[0]+'.txt')
            count+=1
            #if(count/0.1>filenumber):#The moving image has exceeded 10% of the total data set
                #break
    print('count：',count)
    return
 
if __name__ == "__main__":
 
    filedir ='result\\'# old filepath
    tardir = 'test\\'# new filepath
    movefile(filedir,tardir)