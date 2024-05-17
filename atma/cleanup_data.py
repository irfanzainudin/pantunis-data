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
                m = re.findall("<div class=\"element-text\">(.*)</div>", text)
                print(sp[0])
                # with open(sp[0] + ".pantun", "x") as x:
                #     x.write(str(m))
                with open("all.pantun", "x") as x:
                    for n in m[:4]:
                        x.write(n)
                        x.write("\n")
                    x.write("=====")
                break
