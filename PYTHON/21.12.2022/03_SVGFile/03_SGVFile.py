import os

def nobel_by_country(filename,country):
    nobels = []

    for line in open(filename, encoding="UTF-8"):
        print(line)
    return nobels


filename = os.path.join("csv","nobel.csv")
nobels = nobel_by_country(filename, "Italy")

print(nobels)
