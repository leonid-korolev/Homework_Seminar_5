# Задача_1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"
def changing_text(text):
    path = 'abv.txt'
    f = open(path, 'r', encoding = 'utf-8')
    my_text = f.read() 
    f.close
    print(my_text)

    my_text = [i.lower() for i in my_text.split() ]
    text = 'абв'
    res = list(filter(lambda i: not text in i, my_text))
    return ' '.join(res)
text = changing_text(list)
print(text)  

