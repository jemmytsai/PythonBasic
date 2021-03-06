# Python基礎文字語法  
# 
#  

print('--- 文字的處理 START ---\n')
print('文字要用單引號或雙引號:','Hello Python 單引號') # 文字要用單引號或雙引號
print('文字要用單引號或雙引號:',"Hello Python 雙引號", "\n") # 文字要用單引號或雙引號


# 文字要用單引號或雙引號
# 字串
word = ("Hello")
print("文字輸出:",word)

# 字串相加
word = word + "Python"
print("文字串接輸出(使用 , ):",word)

# 同類型才能運算
# justword = word + 3
word = word + "789"
print("同類型才能運算(使用 + )",word)

# Len 長度
# print(len(word))
print("文字長度 (len(字串)):", len(word))

#取文字位於第幾位
print("文字:" + word)
print("取文字的第幾個字( [數值] ):",word[5])
print("取文字的最後一個字:",word[len(word) - 1])

#第二個數字不包含
print("取文字的第幾個字到第幾個字( [數值 : 數值] ):",word[5:11])
print("取文字的第幾個字開始到最後一個字:",word[5:], "\n")

# 取代字
# str.replace(old, new[, max])
# old − This is old substring to be replaced.
# new − This is new substring, which would replace old substring.
# max − If this optional argument max is given, only the first count occurrences are replaced.
print("取代字 replace:")
word = "hellopython"
replaceword = word.replace("python" , "jemmy")
print("原來的值:" , word)
print("新的變數後的值:" , replaceword)

print("轉成大寫 upper:")
upper_text = "jemmy"
print("文字變大寫_jemmy(upper)):" , upper_text.upper())



#def backWord():
#  return print("word py")

#from random import choice
#
#def greeting():
#  return choice(["Hi!", "Howdy!", "Hello!", "Salutations!"])
print('--- 文字的處理 END ---')