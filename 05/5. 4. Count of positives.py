def Count_of_positives(a):
    b = []
    c = 0
    if not a:
        print(a)
    else:
        for item in a:
            if (item >0 ):
                b.append(item)
            else:
                c += item
        
        ret = [len(b), c]

        print(ret)

Count_of_positives([])