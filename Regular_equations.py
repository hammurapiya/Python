import re

with open("HTML_Code.html", encoding="utf-8") as f:
    s = f.read()


result = re.findall("Нас уже ([0-9 ]+) человек", s)
print(result)