# 群集-set說明與實作 (set 是不會有重複的值，如果有重複的值，不知道他是會拿掉那一個)
"""
Set {Set} – “不重複” “同類型”(不重複的List)
1.用 { }包起來，沒有 :  2. 資料不重複  3. [座號] 沒有順序性
"""

print('--- 群集-dictionary(字典) START ---\n')

name_set = {"蔡", "林", "黄", "周", "王"}
print("# name_set (set 每次呈現都沒有一定的順序):", name_set)
# 改舊，不回傳新
b = name_set.add("余")
print("# name_set 用 set.add(值) 新增(余):", name_set)
# 直接改舊的，不會回傳新的
print("# 直接改舊的，不會回傳新的:", b)
print("# 新增一個值後，原來的set值:", name_set)

print("新增一個已存在的值(蔡)和一個不存在的值(陳):\n")
name_set.add("蔡")
name_set.add("陳")
print("# 新增一個已存在的值(蔡)和一個不存在的值(陳)後結果，name_set_add:", name_set,'\n')

name_set.discard("陳")
print("name_set_刪除存在的值(陳):", name_set,'\n')

name_set.discard("謝")
print("name_set_刪除不存在的值(謝):", name_set,'\n')

# 回傳新的
name_set = name_set.union("大", "小")
print("name_set_聯集一個set:", name_set,'\n')

print("用 for in 來跑 Set 迴圈") 
for n in name_set:
    print("-", n)

print('--- 群集-dictionary(字典) END ---\n')    