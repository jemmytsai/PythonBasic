import jieba.analyse

"""
文字檔案的編碼格式與文字檔讀取方法
讀取檔案三部曲
1. 所有資源放在專案底下
2. 檔案路徑: 相對路徑
   r 指唯讀 W 指可寫
3. 檔案編碼: 最好使用 utf-8 ， 避免有難字、亂碼等情況出現
"""
print('--- 檔案的處理 START ---\n')

# 打開檔案

"""
1. open('檔名1.txt')
2. open('/data/檔名2.txt')
3. open('./data/檔名3.txt')
4. open('../data/檔名4.txt')
5. open('C:\\user\\檔名5.txt')
"""

BasicFile = open("./txtFile/BasicFileProcess.txt", "r", encoding="utf-8")
# 把檔案內容放置 變數內
article = BasicFile.read()
# 記得要關閉檔案
BasicFile.close()
# print(article)

# 設定一個 Dictionary 來做記錄
result = {}
for c in article:
    # 對: 我們第二次以上選到
    print("檔內字:", c)
    if c in result:
        result[c] = result[c] + 1
        print("第 N 次出現:", result)
    # 錯: 我們第一次遇到
    else:
        result[c] = 1
        print("第一次出現:", result)
print(result)


# Open a file
NewArticle =''
fo = open("./txtFile/NewBasicFileProcess.txt", "w+" , encoding="utf-8")
for c in result:
    if c in result:
        NewArticle = NewArticle + c  + ":" + str(result[c]) + "|"

print(NewArticle)
fo.write(NewArticle)
fo.close()

print('\n--- 檔案的處理 END ---\n')



