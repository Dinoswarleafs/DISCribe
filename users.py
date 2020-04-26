import user

class Users:
    def __init__(self, ids, names):
       self.user_list = tuple(user.User(id, name) for id, name in zip(ids, names))
    
    def __str__(self):
        res = ""
        for user in self.user_list:
            user.sortDict()
            res += "Name: " + user.name + "\nID: " + user.id + "\nDict: " + str(user.sorted_dict) + "\n\n\n"
        return res

    def addWord(self, id, word):
        self.user_list[self.__getIndex(id)].addWord(word)

    def getWord(self, id, word):
        return self.user_list[self.__getIndex(id)].getWord(word)

    def addMessage(self, id, date):
        

    def __getIndex(self, refID):
        index = 0
        for user in self.user_list:
            id = user.id
            if id == refID:
                return index
            index += 1
        return None