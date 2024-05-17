import re

with open("xab.txt") as xab_file:
    text = xab_file.read()
    dict_matches = {}
    matches = re.findall("===\n(.*)\n===", text)
    plused = []
    for m in matches:
        splitted = m.split()
        joined = "+".join(splitted)
        plused.append(joined)
    with open("slxab.txt", "w") as w:
        w.write(str(plused))
