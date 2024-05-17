import re

for i in reversed(range(159065, 159179)):
    with open(str(i) + ".txt", "r") as f:
        text = f.read()
        m_list = re.findall("<div class=\"element-text\">(.*)</div>", text)
        print(i)
        with open("all.pantun", "a") as x:
            for n in m_list:
                x.write(n)
                x.write("\n")
            x.write("===\n")
