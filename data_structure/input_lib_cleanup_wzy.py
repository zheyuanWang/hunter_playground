with open('inputku.txt', encoding="utf-16") as f:
    with open('outku.txt', "w+", encoding="utf-16") as out:
        for line in f:
            if len(line)<50:
                out.write(line)