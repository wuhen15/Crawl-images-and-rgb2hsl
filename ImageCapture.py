import requests
import os
from selenium import webdriver
import string

def save_photo(root,url):
   if not os.path.exists(root):
       os.makedirs(root) #若没有街景图片文件夹则自动创建
   m = url.split("&")[3] + " + " + url.split("&")[5] + ".jpeg" #把经纬度和方向作为街景的名称
   name = root + m
   r = requests.get(url)
   print(name)
   with open(name, "wb") as f:
       f.write(r.content)
       f.close()
       print("您选择的街景已经成功保存至E盘街景图片文件夹！感谢您的使用！nnn")

#if __name__=='_main_':
tmp,num_str1,num_str2=[],[],[]
x,y='',''
with open("test.txt") as A:
 for eachline in A:
  eachline=eachline.strip('\n')
  tmp = eachline.split(",")
  print(tmp)
  ak='5Xa4IF3PXzrOXMpvk0fZ7CFmeOp2SaZq'
        #num_str1=tmp[0]
  x = "".join(tmp[0])
       # num_str2=tmp[1]
  y = "".join(tmp[1])
  url = "http://api.map.baidu.com/panorama/v2?ak=" + ak + "&width=1024&height=512&location="+x+","+y+"&fov=120&heading=90"
  root = "E://街景图片//"  # 文件保存位置

  save_photo(root,url)

