class Word:
    def __init__(self, text, part_of_speech):
        self.text = text
        self.part_of_speech = part_of_speech

class Sentence:
    def __init__(self):
        self.content = [2,1,0]

    def show(self, list1):
        result_string = ""
        for item in self.content:
            result_string = result_string +" "+ list1[item].text
        return result_string

    def show_parts(self, list1):
        result_string = ""
        for item in self.content:
            result_string = result_string + " " + list1[item].part_of_speech
        return result_string

a = Word("world", "Object")
b = Word("new", "Adjective")
c = Word("Brave", "Adjective")

list_words = []
list_words.append(a)
list_words.append(b)
list_words.append(c)

obj = Sentence()

print(obj.show(list_words))
print(obj.show_parts(list_words))

