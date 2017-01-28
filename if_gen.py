if __name__ == '__main__':
    #a = raw_input("Cell of req: ")
    #b = raw_input("Cell of units: ")
    #c = raw_input("Classifier: ")
    res = '='
    reqs = ['C','F','I','N','Q','T']
    reqs_ind = [4,5,6,7,8,9,10,16,17,18,19,20,21,22]
    with open('if.txt','w') as f:
        for c in range(7,27):
            res = '='
            for el in reqs:
                for ell in reqs_ind:
                    a = el + str(ell)
                    b = chr(ord(el)+1) + str(ell)
                    res += 'IF(%s=W%s,%s,0)+' %(a,str(c),b)
            f.write(res[:len(res)-1]+'\n')
            f.write('\n')
    #with open('if.txt','w') as f:
    #    f.write(res[:len(res)-1])
