word_book = {"restaurant":"饭馆","bank":"银行","smart":"聪明","bird":"鸟","elephant":"大象"}
flag = 'yes'
"""
yes表示没复习完;
no表示复习完了。
"""

while flag == 'yes':
    print('*'*55)
    book_copy = word_book.copy()
    for i in book_copy.keys():
            print(i + "是啥意思？")
            your_answer = input("回答：")
            if your_answer == word_book[i]:
                print('yes')
                del word_book[i]
            else:
                print("no")
        if len(word_book.keys()) == 0:
            print('恭喜你，复习完了！')
            flag = 'no'
        else:
            flag = 'yes'
#老师，对不起！小横线什么意思？运行后错的原因是什么？


