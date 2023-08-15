a = int(input('enter number :'))
if a % 7 == 0 :
    print('yes multiple 7')
else :
    a +=1
    if a % 7 == 0 :
        print('no 7 but :' ,a)
    else :
        a += 1
        if a % 7 == 0 :
            print('no 7 but :' ,a)
        else :
            a += 1 
            if a % 7== 0 :
                print('no 7 but :' ,a)
            else :
                a += 1
                if a % 7== 0 :
                    print('no but 7 :' ,a)
                else : 
                    a += 1
                    if a % 7== 0 :
                        print('no but 7 :' ,a)
                    else :
                        a += 1
                        if a % 7== 0 :
                            print('no but 7 : ,a')