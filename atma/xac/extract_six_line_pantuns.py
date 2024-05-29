import re

with open("xac.txt") as xac_file:
    text = xac_file.read()
    dict_matches = {}
    matches = re.findall("===\n(.+\n){6}===", text)
    plused = []
    for m in matches:
        plused.append(m)
    with open("six-liners-xac.txt", "w") as w:
        w.write(str(plused))
