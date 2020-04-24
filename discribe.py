import csv
import users

USER_LIMIT = -1
user_ids = []
user_names = []
with open('meme.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)

    print("Finding names")
    for row in csv_reader:
        id = row[0]
        name = row[1]
        if (id not in user_ids):
            user_ids.append(id)
            user_names.append(name)
        if USER_LIMIT != -1 and len(user_ids) == USER_LIMIT:
            print("Reached user limit of " + USER_LIMIT)
            break
    print("Names found")

    # Reset file reader
    file.seek(0)
    next(csv_reader)

    print("Creating user dictionaries")
    users = users.Users(user_ids, user_names)
    row_count = 0
    for row in csv_reader:
        message = row[3].split()
        msgID = row[0]
        for word in message:
            users.addWord(msgID, word)
        if row_count % 1000 == 0:
            print("Read " + str(row_count) + " lines")
        row_count += 1
    print("Done reading.")
    
    print("Now writing")
    f = open("output.txt", "w")
    f.write(str(users))
    f.close
print("Done")
