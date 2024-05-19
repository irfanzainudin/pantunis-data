count = 110974
query = "INSERT INTO pantun (id, bayang1, bayang2, maksud1, maksud2, jenis, sumber) VALUES ({count},".format(count = count)
with open("xab.txt", "r") as f:
    with open("add-1.sql", "a") as a:
        for line in f.readlines():
            line = line.strip()
            if line == "===":
                count = count + 1
                query = query + \
                    " 4, 6);\nINSERT INTO pantun (id, bayang1, bayang2, maksud1, maksud2, jenis, sumber) VALUES ({count},".format(count = count)
            else:
                line = "\"" + line
                query = query + line + "\","
        query = query + "4, 6);"
        a.write(query)
