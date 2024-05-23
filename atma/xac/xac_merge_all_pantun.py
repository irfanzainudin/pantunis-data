import re

with open("test-xac.txt") as xac_file:
    xac_txt = xac_file.read()
    split_xac_txt = xac_txt.split("\n")
    matches = re.findall("===\n(.*)\n===", xac_txt)
    with open("other-lines/specific-id-html/all.pantun") as fi_file:
        fi_txt = fi_file.read()
        split_fi_txt = fi_txt.split("\n")
        for m in matches:
            print("m: {m}".format(m=m))
            if m in split_fi_txt:
                split_xac_txt.insert(split_xac_txt.index(
                    m)+1, split_fi_txt[split_fi_txt.index(m)+1])
                split_xac_txt.insert(split_xac_txt.index(
                    m)+2, split_fi_txt[split_fi_txt.index(m)+2])
                split_xac_txt.insert(split_xac_txt.index(
                    m)+3, split_fi_txt[split_fi_txt.index(m)+3])
    with open("res-xac.txt", 'w') as w:
        joined = "\n".join(split_xac_txt)
        w.write(str(joined))
