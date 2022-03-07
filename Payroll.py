import pandas as pd
import csv


f1 = pd.read_csv("file_1.csv", delimiter=',')
f2 = pd.read_csv("file_2.csv", delimiter=',')
f3 = pd.read_csv("file_3.csv", delimiter=',')

f1_out = open("f1_out.csv", "w")
f2_out = open("f2_out.csv", "w")
f3_out = open("f3_out.csv", "w")

worker = pd.read_csv("Workers.csv")

in_list = [f1, f2, f3]
out_list = [f1_out, f2_out, f3_out]

def num_ppl(file, worker):
    """If there is more than one occurance
    of a person in a given file return True"""
    file_list = file.Name.to_list()
    output = False
    if file_list.count(worker) > 1:
            output = True
    return output

def ppl_pay(name, workers, userid, curr_file) -> float:
    """Returns the net pay of a given worker from the given file
    after deductions """

    if workers.Name.to_list().count(name) > 1:
        for user in workers.No.to_list():
            if userid in user:
                coor = workers.Name.to_list().index(name)
                if "Consulting 1" in workers.loc[coor, "Agency"]:
                    rate = workers.loc[coor, "Rate"] if workers.loc[coor, "Rate"][0] == "$" else workers.loc[coor, "Rate"]
                    return round(float(rate)/1.21, 2)

                elif "Consulting 2" in workers.loc[workers.No.to_list().index(userid), "Agency"]:
                    rate = workers.loc[coor, "Rate"] if workers.loc[coor, "Rate"][0] == "$" else workers.loc[coor, "Rate"]
                    return round(float(rate)/1.30, 2)

                elif isinstance(workers.loc[workers.No.to_list().index(userid), "Agency"], float):
                    rate = workers.loc[coor, "Rate"] if workers.loc[coor, "Rate"][0] == "$" else workers.loc[coor, "Rate"]
                    return round(float(rate)/1, 2)                                    
                else:
                    rate = workers.loc[coor, "Rate"][1:] if workers.loc[coor, "Rate"][0] == "$" else workers.loc[coor, "Rate"]
                    return round(float(rate)/1.28, 2)

    else:
        try:
            coor = workers.Name.to_list().index(name)
            if "Consulting 1" in workers.loc[workers.Name.to_list().index(name), "Agency"]:
                rate = workers.loc[coor, "Rate"] if workers.loc[coor, "Rate"][0] == "$" else workers.loc[coor, "Rate"]
                return round(float(rate)/1.21, 2)
        except:
            pass
        try:
            coor = workers.Name.to_list().index(name)
            if "Consulting 2" in workers.loc[workers.Name.to_list().index(name), "Agency"]:
                rate = workers.loc[coor, "Rate"] if workers.loc[coor, "Rate"][0] == "$" else workers.loc[coor, "Rate"]
                return round(float(rate)/1.30, 2)
        except: pass
        try:
            coor = workers.Name.to_list().index(name)
            if isinstance(workers.loc[workers.Name.to_list().index(name), "Agency"], float):
                rate = [coor, "Rate"] if workers.loc[coor, "Rate"][0] == "$" else workers.loc[coor, "Rate"]
                return round(float(rate), 2)                                    
            else:
                rate = workers.loc[coor, "Rate"] if workers.loc[coor, "Rate"][0] == "$" else workers.loc[coor, "Rate"]
                return round(float(rate)/1.28, 2)
        except Exception:
            try:
                coor = workers.Name.to_list().index(name)
                pay = curr_file.loc[curr_file.Name.to_list().index(name), "Supervisor"][1:]
                return pay
            except Exception:
                return Exception


def pay(in_list=in_list, worker=worker, out_list=out_list):
    """out_list is a list that contains paths to csv files
    that the function bill be populating and it will be 
    polulating with the net rates of every employee from all three
    files that have their paths contained in in_list"""
    for i in range(len(in_list)):
        file = in_list[i]
        output_file = out_list[i]
        csvfile = csv.writer(output_file)
        csvfile.writerow(list(file.columns.values))

        for name in file.Name.to_list():
            if "," not in name:
                list_name = name.split(" ")
                name_new = list_name[1]+ ", "+ list_name[0]
            try:
                rate = file.loc[file.Name.to_list().index(name), "Net Rate"][1:]
            except Exception:
                rate = ""

            try:
                if isinstance(float(rate), float):

                    csvfile.writerow(list(file.values[file.Name.to_list().index(name)]))
            except ValueError:
                raise Exception
                lister = list(file.values[file.Name.to_list().index(name)])
                pay = ppl_pay(name_new, worker, file.loc[file.Name.to_list().index(name), "No"], file)
                csvfile.writerow([lister[0], lister[1], lister[2], lister[3], lister[4], "${}".format(pay), lister[6], lister[7]])
                
    output_file.close()

print(pay())

