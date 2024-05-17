import os
import re

for i in sorted(os.listdir(".")):
    if i == "data.txt":
        pass
    else:
        if i.endswith(".txt"):
            sp = i.split(".")
            with open(i) as f:
                text = f.read()
                m = re.findall("<span[\sa-z_\"=]*>(.*?)</span>", text)
                print(sp[0])
                with open("all.pantun", "a") as x:
                    for n in m:
                        x.write(n)
                        x.write("\n")
                    x.write("===\n")
