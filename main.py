# 此為Python基礎語法主要進入口，將所有的練習語法方式至各個PY中

import sys

# print ("查看Python版本", sys . version_info)
# print ("查看Python版本", sys . version)

# PYTHON 網路資源
# print("PYTHON 網路資源")
# PEP(Python Enhancement Proposals)) https://legacy.python.org/dev/peps/
# python 網路文件
# 官方文件: https://docs.python.org/3.8/library/string.html
# tutorialspoint --> https://www.tutorialspoint.com/python/python_strings.htm

# Python 的一些基本知識語法
# 加上#表示註解，所以這行為註解，程式並不會去執行，註解寫的愈好愈仔細，日後的維護會愈輕鬆
# Python的註解有兩種，單行註解跟多行註解。單行的這樣用：
# <-- 單行註解
"""
多行註解
"""

# print("\n") 
# \n : 換一行   \t : TAB   \b : backspace 指標往前一格
# TODO: 表示待做事項


# TODO:寫一個 input 可輸入值，然後用if else 去判斷要跑以下那一個 import 語法

LearnNumber = int(input("請選擇課程:\n[0]Python課程說明\n[1]基礎文字語法\n[2]基礎數字語法\n[3]boolean和條件判斷語法\n[4]迴圈語法\n[5]群集-List\n[6]群集-dictionary(字典)\n[7]群集-set\n[8]群集-Tuple\n[9]Import_Jieba(結巴)\n[10]檔案處理\n[11]自訂函數的架構\n[12]基本物件定義的方法\n請輸入課程數字代碼:"))
print("\n")
if LearnNumber == 0:
  print('--- Python ---','\n')
elif LearnNumber == 1:
  # Python 基礎數字語法
  import BasicText  
elif LearnNumber == 2:
  # Python 基礎數字語法
  import BasicDigital 
elif LearnNumber == 3:
  # Python boolean和條件判斷語法
  import Conditional 
elif LearnNumber == 4:
  # Python 迴圈語法
  import Loop   
elif LearnNumber == 5:
  # 群集-List
  import BasicList 
elif LearnNumber == 6:
  # dictionary(字典)
  import BasicDictionary 
elif LearnNumber == 7:
  # 群集-set
  import BasicSet   
elif LearnNumber == 8:
  # 群集-set
  import BasicTuple
elif LearnNumber == 9:
  # 群集-set
  import Basic_Import_Jieba  
elif LearnNumber == 10:
  # 檔案處理
  import BasicFileProcess    
elif LearnNumber == 11:
  # 自訂函數的架構
  import BasicDef     
elif LearnNumber == 12:
  # 自訂函數的架構
  import BasicClass     
elif LearnNumber == 13:
  print("敬請期待，請隨時關注哦!!!")
else:
  print("請輸入正確的課程代碼")




#print('[1]基礎語法')
#print('1. 加、減、乘、除\n2.文字的運用','\n')

#print('[2]基礎語法')
#print('1.boolean\n2.條件判斷語法','\n')

#print("Drag out the arrow on the left to show the filetree")
#from functions import greeting
#for x in range(10):
#  print(greeting())
#
#print("主要進入點，操作各種的功能")


#print('--- 呼叫文字的處理 start ---')
#word.backWord()
#print('--- 呼叫文字的處理 end ---')


