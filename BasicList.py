print('---  群集-List START ---\n')
# 群集-List
# 清單[List] – “同類型” “隊伍”

# 1. [使用中括號，並以 ， 來做區隔 ] 2.[ 座號，也就是編號，從 0 開始 ]
# Example: name_list = [ "張三","李四","王五"]
# 取值[編號]
# Example: print(name_list[0])
# 取最後一個值
# print("name_list矩陣數量:", name_list[-1])

# 群集-List說明與實作
#print("群集-List: ["天一","小二","張三", "李四", "王五"] )
name_list = ["天一","小二","張三", "李四", "王五"]
print("群集-List name_list:", name_list,'\n')


print("取編號0，也就是第1筆 -- name_list[0]:", name_list[0])
print("取編號1，也就是第2筆 -- name_list[1]:", name_list[1])
print("取編號2，也就是第3筆 -- name_list[2]:", name_list[2])
print("取編號3，也就是第4筆 -- name_list[2]:", name_list[3])
print("取編號4，也就是第5筆 -- name_list[2]:", name_list[4])
print('\n')
print("# 取第幾個值到第幾個值 -- name_list[0:2]:", name_list[0:2],'\n') # :後的那個數字不算在內，所以這樣表示取0跟1

print("# List 加一個值進去，語法: List+[值]\n")
name_list = name_list + ["老六"]
print("# name_list + [值]: ", name_list,'\n')

print("# list矩陣數量，語法: len(name_list):", len(name_list),'\n')
print("# list矩陣最後一個值，語法:list[-1]:", name_list[-1],'\n')

print('# 使用 for in 來跑List的每一個值')
# for   in   用法  n 只是一個暫時的名字
count = 0
for n in name_list:
    print('List編號', count, "-", n)
    count = count +1
print('\n')

print("# List 的 Methods")
# List的專屬技能與del 關鍵字的運用
# list
name_list = ["A", "B", "C"]
print("name_list:", name_list)

# 插隊(insert))，插入至中間
# Return Value:This method does not return any value but it inserts the given element at the given index.
b = name_list.insert(1, "D")
print("# 插入至中間(list.insert(index, obj))， name_list:", name_list)

# Return Value :　This method does not return any value but it inserts the given element at the given index.
# 此方法不返回任何值，但會在給定索引處插入給定元素。
print("b:", b)
print("name_list:", name_list)

name_list = name_list.insert(1 , "E")
print(name_list)

# list 刪除
aname_list = ["A", "B", "C", "Ｄ"]
print("aname_list:", aname_list)
aname_list.insert(1, "Ｙ")
print("aname_list:", aname_list)
aname_list.remove("C")

print("aname_list(remove C):", aname_list)
del aname_list[1]

print(aname_list)


print('-\n---  群集-List END ---\n')