import os, sys

# 当前路径
# path = os.getcwd()
path = r'c:\\Users\\\Wujun\\Documents\\High Purity Quartz\\简单几步-了解下您的石英矿适合做什么产品\\网页图片webp\\'
#获取文件名，存入列表
files = os.listdir(path)
# print(path,files)

n = 0
for i in files:
  #路径+文件名
  oldName = path+files[n]
  #加后缀 
  newName = oldName + '.webp'
  os.rename(oldName,newName)
  print(oldName,'--->>',newName)

  n += 1