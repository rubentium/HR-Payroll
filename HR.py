import pandas as pd

def hr(f1, f2, f3):
    """Checking for repeating
    data inputs in different files"""
    f1 = pd.read_csv(f1)
    f2 = pd.read_csv(f2)
    f3 = pd.read_csv(f3)
    out = {}
    f1_list = f1.Name.to_list()
    f2_list = f2.Name.to_list()
    f3_list = f3.Name.to_list()

    for e in f1_list:

        if f1_list.count(e) != 1 or f2_list.count(e) != 0 or f3_list.count(e) != 0:
            out[e] = [f1_list.count(e), f2_list.count(e), f3_list.count(e)]

    for i in f2_list:

        if f1_list.count(i) != 0 or f2_list.count(i) != 1 or f3_list.count(i) != 0:
            out[i] = [f1_list.count(i), f2_list.count(i), f3_list.count(i)]

    for j in f3_list:

        if f1_list.count(j) != 0 or f2_list.count(j) != 0 or f3_list.count(j) != 1:
            out[j] = [f1_list.count(j), f2_list.count(j), f3_list.count(j)]
    return out


print(hr("file_1.csv", "file_2.csv", "file_3.csv"))
