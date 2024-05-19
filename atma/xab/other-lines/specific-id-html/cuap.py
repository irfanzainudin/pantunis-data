# CUAP = CleanUp All.Pantun
import re


with open("all.pantun") as ap_file:
    ap_txt = ap_file.read()
    split_ap_txt = ap_txt.split("===")
    # print(split_ap_txt[0])
    for para in split_ap_txt:
        split_para = para.split("\n")
        print(split_para[0])
        break
