"""
Finds coordinates with respect to formula derived
"""
dim1 = 50
dim2 = 57
f = open("input_index_7_1.txt",'r')
w = open("output_coordinates_7_1.txt",'w')
w.write("x1\tx2\n")
for i in f.readlines():
    if len(i.strip())!=0:
        try:
            index = int(i.strip())
            w.write(str(index%dim1)+"\t"+str(index//dim1)+"\n")        
        except:
            pass    
f.close()
w.close()        