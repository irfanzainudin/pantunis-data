import os
import re

for i in os.listdir("."):
    if i.endswith(".txt"):
        sp = i.split(".")
        with open(i) as f:
            text = f.read()
            m = re.findall("<span>(.*)</span>", text)
            print(sp[0])
            with open("all.pantun", "a") as a:
                for n in m[:1]:
                    a.write(n)
                    a.write("\n")
                a.write("===\n")
