for i in range(7):
    
    if i < 6:
        num = 2*i-1 # 홀수개, 1, 3, 5, 7, 9
        print(' '*int((9-num)/2), '*'*num, ' '*int((9-num)/2))
    else:
        
        for j in range(5):
            if j == 0:
                continue
            else:
                num = 9 - 2*j
                print(' '*j, '*'*num, ' '*j)
 