import user

class Users:
    def __init__(self, ids, names):
       self.user_list = tuple(user.User(id, name) for id, name in zip(ids, names))
    
    def __str__(self):
        res = ""
        for user in self.user_list:
            user.sortDicts()
            user.calcStats()
            nameStr = "Name: " + user.name
            idStr = "ID: " + user.id
            statsStr = "Stats: \n\tAvg Word Len: " + str(user.word_stats[user.WORD_AVG_LEN]) + "\n\tWord Standard Dev: " + str(user.word_stats[user.WORD_STD])
            res +=  "{}\n{}\n{}\nDict:\n{}".format(nameStr, idStr, statsStr, user.sorted_dicts[user.WORD_DICT])
        return res

    def addWord(self, id, word):
        self.user_list[self.__getIndex(id)].addWord(word)

    def getWord(self, id, word):
        return self.user_list[self.__getIndex(id)].getWord(word)

    def addMessage(self, id, date):
        self.user_list[self.__getIndex(id)].addMessage(date)

    def __getIndex(self, refID):
        index = 0
        for user in self.user_list:
            id = user.id
            if id == refID:
                return index
            index += 1
        return None