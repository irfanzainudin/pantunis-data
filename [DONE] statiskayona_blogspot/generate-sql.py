count = 56000
query = f"INSERT INTO pantun (id, bayang1, bayang2, maksud1, maksud2, jenis, sumber) VALUES ({count},"
with open("formatted.txt", "r") as f:
    with open("add-1.sql", "a") as a:
        for line in f.readlines():
            line = line.strip()
            if line == "===":
                count = count + 1
                query = query + \
                    f" 4, 4);\nINSERT INTO pantun (id, bayang1, bayang2, maksud1, maksud2, jenis, sumber) VALUES ({count},"
            else:
                line = "'" + line
                query = query + line + "',"
        query = query + "4, 4);"
        a.write(query)
