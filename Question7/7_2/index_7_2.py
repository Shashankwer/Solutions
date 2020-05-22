"""
Finds index with respect to formula derived


"""
def product(l):
    """
    calculates l1*l2*l3..ln
    params:
        l: array of dimensions
    returns:
        product    
    """
    p=1
    for i in l:
        p*=i
    return p   

dim = [4,8,5,9,6,7] 
p = [product(dim[:i]) for i in range(1,len(dim)+1)]

f = open('input_coordinates_7_2.txt','r')
w = open('output_index_7_2.txt','w')
w.write("index\n")

for i in f.readlines():
    if len(i.strip())!=0:
        try:
            l = list(map(int,i.split('\t')))
            index=0
            for j in range(len(l)):
                if j>0:
                    index+=l[j]*p[j-1]
                else:
                    index+=l[j]
            w.write(str(index)+"\n")                   
        except:
            pass    
f.close()
w.close()        


