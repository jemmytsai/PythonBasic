# 此為Python基礎語法主要進入口，將所有的練習語法方式至各個PY中

import sys

# print ("查看Python版本", sys . version_info)
# print ("查看Python版本", sys . version)

# PYTHON 網路資源
# PEP(Python Enhancement Proposals)) https://legacy.python.org/dev/peps/

# Python 的一些基本知識語法
# 加上#表示註解，所以這行為註解，程式並不會去執行，註解寫的愈好愈仔細，日後的維護會愈輕鬆
# print("\n") 
# \n : 換一行   \t : TAB   \b : backspace 指標往前一格
# TODO: 表示待做事項


# TODO:寫一個 input 可輸入值，然後用if else 去判斷要跑以下那一個 import 語法

LearnNumber = int(input("請選擇課程:\n[0]Python課程說明\n[1]基礎文字語法\n[2]基礎數字語法\n[3]boolean和條件判斷語法\n[4]迴圈語法\n[5]群集-List\n請輸入課程數字代碼:"))
print("\n")
if LearnNumber == 0:
  print('--- Python ---','\n')
elif LearnNumber == 1:
  import BasicText  # Python 基礎數字語法
elif LearnNumber == 2:
  import BasicDigital # Python 基礎數字語法
elif LearnNumber == 3:
  import Conditional # Python boolean和條件判斷語法
elif LearnNumber == 4:
  import Loop # Python 迴圈語法  
elif LearnNumber == 5:
  import BasicList # 群集-List說明與實作
elif LearnNumber == 6:
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


