def dic_func(para) :
    for k in para.keys():
        print("%s -> %d명입니다." %(k, para[k]))

grade= {'1st' : 178, '2nd' : 200, '3rd':198}
dic_func(grade)