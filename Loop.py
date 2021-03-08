# 迴圈
print('--- 迴圈 START ---\n')

print('# 固定次數迴圈 ---\n')
# 固定次數迴圈說明與實作
# 秀Hello 10 次
# 1. 初始，計數器
times = 0
# 2. 判斷跑10次就停下來
while times < 10:
    print(times + 1, ": hello")
# 3. 更新，跑完要把計數器加1
    times = times + 1

print('\n# 數字累加次數迴圈說明與實作(畫一顆樹) ---\n')
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
#counts = 0
# 一個記憶區
#result = 0
#while counts < 10:
#    result = result + (counts + 1)
#    counts = counts + 1
#print("結果:", result)


# 固定次數迴圈與無法預知迴圈數的說明與應用
# for-loop 比較適用在「已知迴圈數」的問題，而 while-loop 則適用在「無法預知迴圈數」


# 使用 range 和 for in 來做 1加到10 加法
# range(start, stop[, step])的start為序列的起始值（含）；stop為結束值（不含）；step為遞增值。
print('\n# for in 數值累加實作(1加到10) ---\n')
result = 0
for times in range(0, 10, 1):
    result = result + (times + 1)
    print("times:", (times + 1),'result:',result)
print("加總:", result,'\n')


# 使用 while 來做加法
counts = 0  # 算次數
result = 0  # 算結果
print("=== 使用 while (不固定次數) 加總 ===")
while counts < 10:
     result = result + (counts + 1)
     counts = counts + 1
     print("count:", counts, "result:", result)
print("加總:", result)

print('\n--- 迴圈 END ---\n')