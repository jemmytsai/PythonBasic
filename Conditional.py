# 比較運算子與邏輯運算子
print('--- 比較運算子與邏輯運算子 START ---\n')
print('# 比較運算子','\n')

# 1. Boolean(是/否) True , False(第一個字一定要大寫)  
# 2. 數字的比對、字串的比對、
# 3. 查詢(in)

print('# Boolean(是/否) True / False(第一個字一定要大寫)')
a = True
print("# 變數 a = True ， boolean值為:", a)

b = 2 == 2
print("# 變數 b = 2 == 2 ， boolean值為:", b)

#大寫和小寫是不一樣的
print("# 大寫和小寫(jemmy Jemmy)是不一樣的:", "jemmy" == "Jemmy")

print("# 使用 in 來看Key word 是不是在字串中:", "good" in "good morning")

# and or 的boolean
print("# 專門結合運算(True or False):", True or False)
print("# 專門結合運算(5 > 3 - 1 and True):", 5 > 3 - 1 and True,'\n')

print("# 邏輯運算子\n")
print("1. 單純的 if 判斷:\nif condition:\n\tstatement\n\t")
print("2. if else 判斷:\nif condition:\n\tstatement1 for True condition\nelse:\n\tstatement2 for False condition\n")
print("3. if-elif-elif-else 判斷:\nif condition1:\n\tstatement1 for True condition\nelif condition2 :\n\tstatement2 for True Condition2\nelif condition3 :\n\tstatement3 for True Condition3\nelse:\n\tstatements for Each Condition False")

print("\n===== 中間線 =====\n")
print('\nEXAMPLE: 使用input函式判斷輸入的值是否有超過60分\n')
#加入輸入方式
#float(轉成小數)
newscore = float(input("請輸入成績看是有超過60(可以整數也可以有小數): "))
if newscore >= 60:
    print("PASS")
else:
    print("FAIL\n")

print("\n===== 中間線 =====\n")

# 巢狀條件判斷語法的說明與實作
print('\nEXAMPLE: 巢狀條件判斷語法的說明與實作\n')
newscore = float(input("請輸入成績(60以上及格、以下不及格、A:高於90、B:80~80、C:70~80、D:70以下):"))
if newscore >= 60:
    print("PASS")
else:
    print("FAIL")

if newscore >= 90:
    print("RANK A")
elif newscore >= 80:
    print("Rank B")
elif newscore >= 70:
    print("RANK C")
else:
    print("RANK D")



# 1. 單純的 if 判斷
# if condition:
#    statement

# 2. if else 判斷
# if condition:
#     statement1 for True condition
# else:
#     statement2 for False condition

# 3. if-elif-else 判斷
# if condition1:
#     statement1 for True Condition1
# elif condition2 :
#     statement2 for True Condition2
# elif condition3 :
#     statement3 for True Condition3
# else:
#     statements for Each Condition False

print('--- 比較運算子與邏輯運算子 END ---\n')