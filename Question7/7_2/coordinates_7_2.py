"""
Finds coordinates using the formula derived
"""
def product(l):
    """
    product of the input array
    params:
        l: input dimension array
    output: 
        p: product array    
    """
    p=1
    for i in l:
        p*=i
    return p    

dim = [4,8,5,9,6,7] 
p = [product(dim[:i]) for i in range(len(dim)-1,0,-1)]

f = open('input_index_7_2.txt','r')
w = open('output_coordinates_7_2.txt','w') 
w.write("x1\tx2\tx3\tx4\tx5\tx6\n")

for i in f.readlines():
    if len(i.strip())!=0:
        try:
            index = int(i.strip())
            l=[]
            prod=0
            for i in p:
                q = (index-prod)//i
                prod+= q*i
                l.insert(0,q) 
            q0 = index-prod
            l.insert(0,q0)
            s = ""
            for i in range(len(l)):
                if i==len(l)-1:
                    w.write(str(l[i])+"\n")
                else:
                    w.write(str(l[i])+"\t")   
            #break      
        except:
            pass    
f.close()
w.close()
#[4, 32, 160, 1440, 8640, 60480]
#58795

