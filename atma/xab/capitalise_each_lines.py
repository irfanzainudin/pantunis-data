with open("xab1.txt", "r") as r:
    new_text = ""
    with open("cleaned.pantun", "a") as a:
        for line in r.readlines():
            if line[0].islower():
                print(line)
                new_line = line.capitalize()
                new_text += new_line
                # print(line)
            else:
                new_text += line
                continue
        a.write(new_text)