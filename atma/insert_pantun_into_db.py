import os

count = 1254
query = f"INSERT INTO pantun (id, bayang1, bayang2, maksud1, maksud2) VALUES ({count},"
with open("data.txt", "r") as f:
    with open("add-1.sql", "a") as a:
        for line in f.readlines():
            line = line.strip()
            if line == "===":
                count = count + 1
                query = query + \
                    f");\nINSERT INTO pantun (id, bayang1, bayang2, maksud1, maksud2) VALUES ({count},"
            else:
                line = "'" + line
                query = query + line + "',"
        query = query + ");"
        a.write(query)
