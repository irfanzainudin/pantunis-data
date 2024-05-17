import os
import re

# idx = 0
for i in sorted(os.listdir(".")):
    # if idx == 20:
    #     break
    if i.endswith(".txt"):
        sp = i.split(".")
        with open(i) as f:
            text = f.read()
            m = re.findall(
                "<a href=\"/items/show/([0-9]+)\">(.*)</a>", text)
            print(sp[0])
            spaced = sp[0].split("+")
            spaced = " ".join(spaced)
            print(spaced)
            with open("specific_id.txt", "a") as x:
                for n in m:
                    if n[1] == spaced:
                        # print("same!")
                        x.write(n[0])
                        x.write("\n")
                        break
                    # else:
                    #     x.write(n[0])
                    #     x.write("\n")
                x.write("===\n")
    # idx += 1
