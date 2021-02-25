# 此為Python基礎語法主要進入口，將所有的練習語法方煩至各個PY中


# Python 的一些基本知識語法
# 加上#表示註解，所以這行為註解，程式並不會去執行，註解寫的愈好愈仔細，日後的維護會愈輕鬆
# print("\n") 
# \n : 換一行   \t : TAB   \b : backspace 指標往前一格
# TODO:


# TODO:寫一個 input 可輸入值，然後用if else 去判斷要跑以下那一個 import 語法

learnNumber = int(input("請選擇課程 [1]基礎語法 [2]boolean和條件判斷語法 :"))
print("\n")
if learnNumber == 1:
  print('--- \nPython基礎語法 start ---','\n')
  import basic #引用模組
  print('--- Python基礎語法 end ---','\n')
elif learnNumber == 2:
  print('--- Python boolean和條件判斷語法 start ---','\n')
  import Conditional #引用模組
  print('--- Python boolean和條件判斷語法 end ---','\n')
elif learnNumber == 3:
  print("敬請期待，請隨時關注哦!!!")
else:
  print("請輸入正確的課程代碼")



#print("Drag out the arrow on the left to show the filetree")
#from functions import greeting
#for x in range(10):
#  print(greeting())
#
#print("主要進入點，操作各種的功能")


#print('--- 呼叫文字的處理 start ---')
#word.backWord()
#print('--- 呼叫文字的處理 end ---')


