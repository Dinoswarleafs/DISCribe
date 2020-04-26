import datetime as dt
import math

class User:
    TOTAL_DICTS = 3
    WORD_STATS = 2
    
    # Individual Lists
    WORD_DICT = 0
    DATE_DICT = 1
    TIME_DICT = 2

    # Individual Word Stats
    WORD_AVG_LEN = 0
    WORD_STD = 1

    date_input_format = '%d-%b-%y'
    date_output_format = '%Y-%m-%d'

    time_input_format = '%I:%M %p'
    time_output_format = '%H:%M'

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.dicts = tuple({} for _ in range(User.TOTAL_DICTS))
        self.sorted_dicts = list({} for _ in range(User.TOTAL_DICTS))
        self.word_len_list = {}

    def __repr__(self):
        return str(self.dicts[User.WORD_DICT])

    def addWord(self, word):
        self.__incrementDict(self.dicts[User.WORD_DICT], word)
        self.__incrementDict(self.word_len_list, len(word))

    def sortDicts(self):
        for i in range(User.TOTAL_DICTS):
            if not self.sorted_dicts[i]:
                self.sorted_dicts[i] = sorted(self.dicts[i].items(), key=lambda x: x[1], reverse = True)

    def addMessage(self, date):
        output_date = dt.datetime.strptime(date[:9], User.date_input_format).strftime(User.date_output_format)
        output_time = dt.datetime.strptime(date[10:], User.time_input_format).strftime(User.time_output_format)
        self.__incrementDict(self.dicts[User.DATE_DICT], output_date)
        self.__incrementDict(self.dicts[User.TIME_DICT], output_time)

    def getWord(self, word):
        return self.dicts[User.WORD_DICT].get(word)

    def calcStats(self):
        mu = 0
        total_words = 0
        for num in list(self.word_len_list.keys()):
            mu += num * self.word_len_list[num]
            total_words += self.word_len_list[num]
        mu /= total_words
        std = 0
        div = 0
        total_weights = len(self.word_len_list)
        for num in list(self.word_len_list.keys()):
            std += self.word_len_list[num] * (num - mu)**2
            div += self.word_len_list[num]
        div *= (total_weights - 1) / total_weights
        std = math.sqrt(std/div)
        self.word_stats = (mu, std)

    def __incrementDict(self, dict, key):
        count = dict.get(key)
        if count is None:
            count = 0
        count += 1
        dict[key] = count

