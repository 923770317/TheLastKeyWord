#coding=utf-8
import os

parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
screenPicturesDir = parentDirPath + '\\exceptionpictures\\'

print parentDirPath
print os.path.abspath(__file__)
print os.path.dirname(os.path.abspath(__file__))