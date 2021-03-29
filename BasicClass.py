# 物件導向-基本物件定義的方法

print('---  物件導向 START ---\n')

def bmi(height, weight):
    return weight / (height / 100) ** 2

# class 指的是設計圖，命名的第一個字一定要大寫，沒有要給值 None 的 N 一定要大寫
class Person:
# name = None
# height = None
# weight = None
    # 每次都會自動做一次
    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def return_bmi(self):
        return self.weight / (self.height / 100) ** 2

    def isoverweight(self):
        if self.weight >= 100:
            return True
        else:
            return False

p1 = Person("Jemmy", 175 , 75)
# p1.name = "Elwing"
# p1.height = 175
# p1.weight = 75
# b = p1.weight / (p1.height / 100) ** 2
print("姓名:",p1.name," BMI:", p1.return_bmi())
print("p1過重與否", p1.isoverweight(),"\n")

p2 = Person("jimmy", 180, 100)
# p2.name = "Bob"
# p2.height = 180
# p2.weight = 80
# b = p1.weight / (p1.height / 100) ** 2
print("姓名:",p2.name," BMI:",  p2.return_bmi())
print("p2過重與否", p2.isoverweight(),"\n")

print('---  物件導向 END ---\n')