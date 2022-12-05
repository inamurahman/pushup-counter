with open("lb.txt") as f:
    content_list = f.readlines()

content_list = [x.strip() for x in content_list]
lb=[]
lbb=[]
for i in content_list:
    l=list(map(str,i.split(" ")))
    lb.append(l)
def leader(hs):
    if (int(int(hs[1])) > int(lb[4][1])):
        lb[4] = hs   
        def Sort(sub_li):
            sub_li.sort(key = lambda x: int(x[1]), reverse = True)
            return sub_li
        lbb = Sort(lb)
        print(lbb)
        with open('lb.txt', 'w') as fp:
            for item in lbb:
                for i in item:
                    fp.write("%s " %str(i))
                fp.write("\n")
leader(['MR','70'])