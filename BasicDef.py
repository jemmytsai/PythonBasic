# 自訂函數的架構與實作
# 預設值(所有右邊的參數都要有預設值)
# 可以做指定帶入

print('---  自訂函數的架構與實作 START ---\n')

# 宣告一個 add 的函數
# 值可以先帶好預設值，也可以等呼叫時再帶入，

print("自訂函數 : add(n1, n2, n3 = 3 , n4 = 4)")
def add(n1, n2, n3 = 3 , n4 = 4):
    print("呼叫者帶入 n1:", n1)
    print("呼叫者帶入 n2:", n2)
    print("預設值n3:", n3)
    print("預設值n4:", n4)
    return (n1 + n2) / n3 * n4

print("(n1 + n2) / n3 * n4 : ",add(1, 2),'\n')
print("(n1 + n2) / n3 * n4 : ",add(3, 5, 2),'\n')
print("(n1 + n2) / n3 * n4 : ",add(3, 5, n4=2),'\n')

# print(add("hello", "python"))
# 文字共能跟文字加
# print(add("hello", 3))
# 傳入值一定要依def定義，此次為一定要傳入二個參數，少傳也不行
# print(add(3))
# 傳入值一定要依def定義，此次為一定要傳入二個參數，多傳也不行
# add(3,5, 7,)


#放一個群集進去加總
def add_mutiple_old(nlist_old):
    result_old = 0
    for n in nlist_old:
        print("n:",n)
        result_old = result_old + n
    return result_old
    # 這是一個 list
print(add_mutiple_old([1, 2, 3]))




# TODO: 再多學習
# 放一個群集進去加總
# 在 nlist 前可以放一個 * , 就可以取代下方 add_mutiple(1, 2, 3)
# def add_mutiple(nlist):
def add_mutiple(*nlist):
    result = 0
    for n in nlist:
        result = result + n
    return result
# print(add_mutiple([1, 2, 3]))
print(add_mutiple(1, 2, 3))


print('---  自訂函數的架構與實作 END ---\n')