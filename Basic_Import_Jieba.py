print('---  import START ---\n')
# 練習 import 寫法
# import jieba
# === 第一種 import 寫法 ===
import jieba.analyse
# 用法: jieba.analyse.extract_tags
# import jieba.analyse

# === 第二種 import 寫法 ===
# from jieba import analyse

# === 第三種 import 寫法 ===
from jieba.analyse import extract_tags

# 讀取檔案三部曲
# 1. 所有資源放在專案底下
# 2. 檔案路徑: 相對路徑
BasicFile = open("./txtFile/Basic_Import_Jieba.txt", "r", encoding="utf-8")
article = BasicFile.read()
BasicFile.close()
print(article)

# 靜態寫法(讀文字檔)(想要修改的文字可以寫在這個檔案上來做控管)
jieba.load_userdict("./txtFile/MyDictionary.txt")

# 動態寫法(寫在程式)
jieba.add_word("殖利率")
jieba.add_word("燦星旅")
# 字典中的詞(dict.txt) ["詞1" , "詞2" , "詞3"]
# 我中午吃牛排 --> 我 中午 吃 牛排
sep = " ".join(jieba.cut(article))
print(sep)

print('\n',"前10關鍵詞:", extract_tags(article, 10))


# 體驗一下 jieba
# import 要放在最上面
#keywords = jieba.analyse.extract_tags(article, 5)
#print("最關鑑詞:", keywords)

print('---  import END ---\n')