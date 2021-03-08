# 群集-Tuple說明與實作 (簡化版字典)
"""
Tuple -- 簡化版字典
使用小刮號 ( )
取值方式[編號]
Example: person = ("Jemmy", 175, 75)
"""

# 群集-tuple說明與實作
person = ("Jemmy", 177, 66)
print("Tuple((Jemmy, 177, 66)):", person,'\n')

# 以下這個寫法不行，因為左右的型態不同 會出現 error --> TypeError: can only concatenate tuple (not "str") to tuple
# person + "Taipei"
# 以下的寫法，還是會被誤認為字串，會出現 error --> TypeError: can only concatenate tuple (not "str") to tuple
# person + ("Taipei")

# 正確的寫法，如果tuple是只要加一個的話，就在後面加個 , 如加二個以上的話就沒這個問題了
person = person + ("Taipei", )
print("Tuples 新增一個值，+ (值, ):", person,'\n')

person = person + ("工程師", "工兵")
print("Tuples 新增二個值，+ (值,值):", person,'\n')

# 取第三個值
print("Tuples取第三個值:", person[2])
# 取第幾個到第幾個，後面那個數字是不包含在內的哦
print("Tuples 取第幾個到第幾個:", person[:2],'\n')
# 如果值都不給的話，表示從第一個取到最後一個
# print("person:", person[:])

# tuple 刪除? Python不布望你做，所以沒定義
# 但如真的要做的話(不建議) 還是可以用繞彎達到
print("tuple用加的方式:", person[0:1] + person[2:],'\n')

print("用 for in 來跑 Tuple 迴圈") 
for man in person:
  print("person", man, '\n')

