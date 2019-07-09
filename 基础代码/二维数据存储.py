fo = open("data\\data.csv", "r")
ls = []

# for line in fo:
#     line = line.replace("\n","")
#     ls.append(line.split(","))
# print(ls)
# fo.close()

for line in fo:
    line = line.replace("\n", "")
    ls = line.split(",")
    lns = ""
    for s in ls:
        lns += "{}\t".format(s)
    print(lns)
fo.close()