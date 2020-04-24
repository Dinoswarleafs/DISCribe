class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.word_dict = {}
        self.sorted_dict = {}

    def __repr__(self):
        return str(self.word_dict)

    def addWord(self, word):
        count = self.word_dict.get(word)
        if count is None:
            count = 0
        count += 1
        self.word_dict[word] = count

    def sortDict(self):
        if not self.sorted_dict:
            self.sorted_dict = sorted(self.word_dict.items(), key=lambda x: x[1], reverse = True)
        return self.sorted_dict

    def getWord(self, word):
        return self.word_dict.get(word)

