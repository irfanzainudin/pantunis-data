import os
import re

for i in sorted(os.listdir(".")):
    if i.endswith(".txt"):
        sp = i.split(".")
        with open(i) as f:
            text = f.read()
            m = re.findall(
                "<div class=\"element-text\">(.+)</div>", text)
            print(sp[0])
            # print(m)
            with open("all-1.pantun", "a") as x:
                for n in m[:4]:
                    x.write(n)
                    x.write("\n")
                x.write("===\n")
    # break
