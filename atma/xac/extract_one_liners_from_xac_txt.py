import re

with open("xac.txt") as xac_file:
    text = xac_file.read()
    dict_matches = {}
    matches = re.findall("===\n(.*)\n===", text)
    plused = []
    for m in matches:
        splitted = m.split()
        joined = "+".join(splitted)
        plused.append(joined)
    with open("slxac.txt", "w") as w:
        w.write(str(plused))
