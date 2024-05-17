import os
import re

for i in os.listdir("."):
    if i.endswith(".txt"):
        sp = i.split(".")
        with open(i) as f:
            text = f.read()
            m = re.findall("<span>(.*)</span>", text)
            print(sp[0])
            # print(len(m))
            with open("all.pantun", "a") as x:
                for n in m[:1]:
                    x.write(n)
                    x.write("\n")
                x.write("===\n")
