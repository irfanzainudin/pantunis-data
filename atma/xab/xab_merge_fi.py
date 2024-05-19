import re

with open("xab.txt") as xab_file:
    xab_txt = xab_file.read()
    split_xab_txt = xab_txt.split("\n")
    matches = re.findall("===\n(.*)\n===", xab_txt)
    with open("fi.txt") as fi_file:
        fi_txt = fi_file.read()
        split_fi_txt = fi_txt.split("\n")
        # print(split_fi_txt[0])
        # print(split_fi_txt[1])
        # print(split_fi_txt[2])
        # print(split_fi_txt[3])
        # print(split_fi_txt[4])
        # print("Length of split_fi_txt: {sft}".format(sft = len(split_fi_txt)))
        for m in matches:
            print("m: {m}".format(m = m))
            # print("index: {sfti}".format(sfti = split_fi_txt.index(m)))
            # print(split_fi_txt[split_fi_txt.index(m)])
            # print(split_fi_txt[split_fi_txt.index(m)+1])
            # print(split_fi_txt[split_fi_txt.index(m)+2])
            # print(split_fi_txt[split_fi_txt.index(m)+3])
            # print("Length of split_xab_txt: {sxt}".format(sxt = len(split_xab_txt)))
            if m in split_fi_txt:
                split_xab_txt.insert(split_xab_txt.index(m)+1, split_fi_txt[split_fi_txt.index(m)+1])
                split_xab_txt.insert(split_xab_txt.index(m)+2, split_fi_txt[split_fi_txt.index(m)+2])
                split_xab_txt.insert(split_xab_txt.index(m)+3, split_fi_txt[split_fi_txt.index(m)+3])
            # print(split_xab_txt[split_xab_txt.index(m)])
            # print(split_xab_txt[split_xab_txt.index(m)+1])
            # print(split_xab_txt[split_xab_txt.index(m)+2])
            # print(split_xab_txt[split_xab_txt.index(m)+3])
            # print("Length of split_xab_txt: {sxt}".format(sxt = len(split_xab_txt)))
            # break
    # with open("res-xab.txt", 'w') as w:
    with open("res-xab-1.txt", 'w') as w:
        joined = "\n".join(split_xab_txt)
        w.write(str(joined))
