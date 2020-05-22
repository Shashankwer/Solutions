"""
Finds index using the formula derived 
"""
dim1 = 50
dim2 = 57
f = open("input_coordinates_7_1.txt")
w = open('output_index_7_1.txt','w')
w.write('index\n')
for i in f.readlines():
    if len(i.strip())!=0:
        try:
            d1,d2 = list(map(int,i.split('\t')))
            w.write(str((d2)*dim1+(d1))+"\n")
        except:
            pass    
f.close()
w.close()



