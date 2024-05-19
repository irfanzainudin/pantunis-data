import re

with open("res-xab.txt") as xab_file:
    xab_txt = xab_file.read()
    split_xab_txt = xab_txt.split("\n")
    matches = re.findall("===\n(.*)\n===", xab_txt)
    with open("other-lines/specific-id-html/all.pantun") as fi_file:
        fi_txt = fi_file.read()
        split_fi_txt = fi_txt.split("\n")
        for m in matches:
            print("m: {m}".format(m = m))
            if m in split_fi_txt:
                split_xab_txt.insert(split_xab_txt.index(m)+1, split_fi_txt[split_fi_txt.index(m)+1])
                split_xab_txt.insert(split_xab_txt.index(m)+2, split_fi_txt[split_fi_txt.index(m)+2])
                split_xab_txt.insert(split_xab_txt.index(m)+3, split_fi_txt[split_fi_txt.index(m)+3])
    with open("res-xab-1.txt", 'w') as w:
        joined = "\n".join(split_xab_txt)
        w.write(str(joined))
