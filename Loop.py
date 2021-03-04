# 迴圈
print('--- 迴圈 START ---\n')

print('# 固定次數迴圈說明與實作 ---\n')
# 固定次數迴圈說明與實作
# 秀Hello 10 次
# 1. 初始，計數器
times = 0
# 2. 判斷跑10次就停下來
while times < 10:
    print(times + 1, ": hello")
# 3. 更新，跑完要把計數器加1
    times = times + 1

print('\n# 數字累加次數迴圈說明與實作(畫一個金字塔) ---\n')
# Hello 10 次
# 1. 初始
times = 0
count = 10
# 2. 判斷
while times < 10:
    print(' ' * count , '*' * 2 * times )
# 3. 更新
    times = times + 1
    count = count - 1

root = 0
while root < 5:
  print("\t\t*******\t\t")
  root = root + 1
print("***********************")

print('\n# 數值累加實作(1加到10) ---\n')
# 數值累加實作
# 1加到10
counts = 0
# 一個記憶區
result = 0
while counts < 10:
    result = result + (counts + 1)
    counts = counts + 1
print("結果:", result)

print('\n--- 迴圈 END ---\n')