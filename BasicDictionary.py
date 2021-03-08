# 群集-dictionary(字典)說明與實作
"""
字典{Dictionary} – 聚集”不同” 類型，比較複雜
# 1. { : } 2.[“名字”]
Example: person = {"name":"jemmy" , "height":175 , "handsome":True}
取值方式[key值]  
Example: print("name:" , person["name"])
"""

print('--- 群集-dictionary(字典) START ---\n')

person = {"name": "jemmy", "height": 175, "handsome": True}
print("# person(dictionary):", person,'\n')

# 取出名字: List 的寫法 print(name)
print("# 取 dictionary 的 value ，語法:Dictionary[value]:", person["name"],'\n')

# 新增一個名字 : weight =75
person["weight"] = 75
print("# 新增一個名字(weight)，語法:person[key]] = value :", person,'\n')

# 更改名字背後的值: List 的寫法  height =177
person["height"] = 177
print("# 更改Key的值，語法:person[key]] = new value :", person,'\n')

# 取出來做完運算後設定回去:  List 的寫法 height = height +3
person["height"] = person["height"] + 3
print("# 取出來做完運算後設定回去:", person,'\n')

# 刪除一個名字
del person["weight"]
print("# 刪除一個名字(weight)，語法:del Dictionary[key] :", person,'\n')

print("# 使用 for 跑 dictionary 的 Key 和 value ")
# for 單個東西暫時名字 in 群集
# {名字:資料} -> 因為有兩個，做出取捨後，只丟名字給你
count = 0
for key in person:
    print("編號: ", count, "-", ":", person[key])
    count = count +1
print('\n')    

print("使用 while 跑 dictionary 的 Key 和 value ")

key=list(person.keys())
i=0
while i<len(key):
    print("編號:",i, "-", key[i],":",person[key[i]])
    i+=1


print('\n--- Example ---\n')     
# Example
# test dictionary
article = "Google地圖探索太空功能上線"
result = {}
for c in article:
    if c in result:
        result[c] = result[c] + 1
        print("result 已存在: ", result)
    else:
        result[c] = 1
        print("result 尚不存在: :", result)

print('\n--- 群集-dictionary(字典) END ---\n')        
