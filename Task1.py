'''
1. Получите текст из файла.
2. Разбейте текст на предложения.
3. Найдите самую используемую форму слова, состоящую из 4 букв и более, на русском языке.
4. Отберите все ссылки.
5. Ссылки на страницы какого домена встречаются чаще всего?
6. Замените все ссылки на текст «Ссылка отобразится после регистрации».

'''
import re
from collections import Counter

#получаем текст из файла
f = open('text.txt', encoding = 'utf-8')
text = f.read()

#разбиваем на предложения
text1 = re.split("\. |\.\n", text)
#print(text1)

#самое часто встречающееся слово
words = re.findall('\w{4,}', text) #разделим по словам с длинной от 4 символов
res = Counter(words).most_common()
sorted_by_second = sorted(res, key=lambda x: x[1], reverse = True)
count = sorted_by_second [0][1]
print('Самые часто встречающиеся слова, длинной более 4 символов:')
for word in sorted_by_second:
    if word [1] == count:
        print(word)

#отбор ссылок
pattern = re.compile("[0-9a-z.//]+ru[0-9a-z.//]+")
a = re.findall(pattern,text)
print ('Список ссылок: ',a)

#Ссылки на страницы какого домена встречаются чаще всего?

domen_list = []
for item in a:
    b = re.findall("\.[a-z]+\.?[a-z]+", item)
    domen_list.append(b)

qty_most_common = 0
most_common = None

for item in domen_list:
    qty = domen_list.count(item)
    if qty > qty_most_common:
        qty_most_common = qty # то заменяем на него максимальное,
        most_common = item # запоминаем само значение

print('Наиболее часто встречаются ссылки на страницы домена: ', most_common)

#Замените все ссылки на текст «Ссылка отобразится после регистрации».
new_text = re.sub(pattern, "Ссылка отобразится после регистрации.", text)
print(new_text)