# Python基礎語法  
# 1.加/減/乘/除
# 2.文字的處理 

print('文字要用單引號或雙引號:','Hello Python 單引號') # 文字要用單引號或雙引號
print('文字要用單引號或雙引號:',"Hello Python 雙引號", "\n") # 文字要用單引號或雙引號

print('# 基本的 加法 - 使用 + --')
# 使用 + 來做數字的相加 (+的前後加上空白比較好看)
a = 3 + 3.14
print("ａ(3 + 3.14=)：", a, "\n")

print('# 基本的 減法 - 使用 - --')
#　基本的乘法 (使用 - 來做數字的除法)
print("10-3=：", 10-3, "\n")

print('# 基本的 乘法 - 使用 *  --')
#　基本的乘法 (使用 * 來做數字的相加)
b = a * 2
print("b=(a * 2):", b)
c = a * 3
print("a=(a * 3)：", c, "\n")

print('# 基本的 除法 - 使用 / --') 
#　基本的乘法 (使用 / 來做數字的除法)
print("6/3=：", 6/3, "\n")


#絕對值(abs)
print('# 絕對值 -- 用來表示一個數至原點的距離之大小。 一個數的絕對值永遠非負，沒有負號-')
print("ａ：", a)
p = -2 * a
Q = abs(-2 * a)
print("原來值 乘 -2=", p)
print("絕對值=", Q, "\n")

print("# 次方(pow) 返回x y（x的y次方）的值")
#次方(pow) 返回x y（x的y次方）的值
Y = 2
Z = pow(Y, 5)
print("Z(2的5次方)：", Z, "\n")

print("# BMI值計算公式: BMI = 體重(公斤) / 身高平方(公尺平方)")
# BMI值計算公式:   BMI = 體重(公斤) / 身高2(公尺2)
# 體重正常範圍為  BMI=18.5～24
#引入math模塊
#import math
weight = 82
length  = 1.66
bmi = weight / pow(length , 2)
print("bmi：", bmi, "\n")

print('------------------ 中間線 ------------------', "\n")

print('--- 文字的處理 ---')
# 文字要用單引號或雙引號
# 字串
word = ("Hello")
print("文字輸出:",word)

# 字串相加
word = word + "Python"
print("文字串接輸出:",word)

# 同類型才能運算
# justword = word + 3
word = word + "789"
print("同類型才能運算",word)

# Len 長度
# print(len(word))
print("文字長度 (len):", len(word))

#取文字位於第幾位
print("文字:" + word)
print("取文字的第幾個字:",word[5])
print("取文字的最後一個字:",word[len(word) - 1])

#第二個數字不包含
print("取文字的第幾個字到第幾個字:",word[5:11])
print("取文字的第幾個字開始到最後一個字:",word[5:], "\n")

#def backWord():
#  return print("word py")

#from random import choice
#
#def greeting():
#  return choice(["Hi!", "Howdy!", "Hello!", "Salutations!"])