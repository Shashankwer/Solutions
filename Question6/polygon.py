"""
The point in polygon problem finds solution using an extension of Ray Casting algorithm (Odd Even rule).

Here the solution space is divided into set of trigangle starting from the first point of the polygon. 
a. If a point is in even number of sub traingles then the point is outside polygon
b. If a point is in odd number of sub traingles then the point is inside the polygon. 
This is owning to the fact that each triangle divides the polygon uniquely into set of subspaces for a convex polygon. Thus if a point is inside a convex polygon then it must lie inside only one triangle
In case of the concave polygon the triangle divide the edges into sub problem space. Thus should follow the ray casting or even/odd principle
"""
from itertools import combinations #Used for taking combination of points for subtriangle formation
import math

class Points():
    """
    Class defines Point in 2D geometric space with properties
    a. Distance: euclidean distance between the 2 points
    b. slope: given 2 points finds the slope
    c. toString: string representation of x and y coordinates
    """
    def __init__(self,pt):
        self.x = pt[0]
        self.y = pt[1]
    def distance(self,pt):
        return ((self.x-pt.x)**2 + (self.y-pt.y)**2)**0.5    
    def __str__(self):
        return str(self.x)+" "+str(self.y)
    def toString(self):
        return str(self.x)+" "+str(self.y)    
    def slope(self,pt):
        if (pt.x-self.x)==0:
            return math.inf
        else:
            return (pt.y-self.y)/(pt.x-self.x)        


def areaTriangle(p):
    """
    Finds the area of the triangle using Heron's formula area = sqrt(s(s-a)(s-b)(s-c)) where s is the semiperimeter
    params:
    p   Coordinates of a triangle
    return
        area: area given by herons formula
    """
    dist = []
    for i in combinations(p,2):
        dist.append(i[0].distance(i[1]))
    s = sum(dist)/2
    return round((s*(s-dist[0])*(s-dist[1])*(s-dist[2]))**0.5,2)    

def inoutTriangle(p,pt):
    """
    Given a triangle and a point finds if the point is inside a triangle or not. 
    If the point is inside a triangle then it divides the triangle into 3 subparts suvh that the sum of the area of each subpart is the area of the triangle as a whole
    params:
        p : traingle points
        pt: point to check if it is inside or outside a triangle
    returns:
        True if point is inside 
        False otherwise    
    """
    for i in p.keys():
        for j in p.keys():
            if i!=j:
               # if the point is on the edge of either of the side 
               if p[i].slope(pt)==p[i].slope(p[j]) and p[i].distance(pt)<=p[i].distance(p[j]):
                    return True
    pts=list(p.values())
    pts.append(pt)
    area=[]
    for i in combinations(pts,3):
        area.append(areaTriangle(i))
   #area of base triangle == sum of area of 3 sub triangles
    maxarea = area.pop(0)
    if sum(area)==maxarea:
        return True
    else:            
        return False            

def inoutPolygon(p,pt):
    """
    Finds if a point is inside a polygon or not. It divides the problem into a space of subtraingles. 
    If the point is in odd number of triangle then the point is in polygon False otherwise
    params:
        p: set of points of the ploygon
        pt: Point to check if it is inside or outside of a polygon
    returns:
        True: if the point is inside 
        False: otherwise
    """
    count=0
    #Dividing polygon into triangles
    for i in range(1,len(p)-1):
        triangle={}
        triangle[0] = p[0]
        triangle[1] = p[i]
        triangle[2] = p[i+1]
        if inoutTriangle(triangle,pt):
            count+=1   
    if count%2==1:
        return True
    else:
        return False             

p = {} # polygon points
input_polygon = "input_question_6_polygon"
f = open(input_polygon,'r')
pts =0
for i in f.readlines():
    p[pts]= Points(tuple(map(int,i.split())))
    pts +=1
f.close()
pts = 0
input_points = "input_question_6_points"
f = open(input_points,'r')
l=[]
for i in f.readlines():
    if len(i.split())!=0:
        point = Points(tuple(map(int,i.split())))
        l.append(point)
f.close()


w = open("output_question_6",'w')
for i in l:
    if inoutPolygon(p,i):
        w.write(i.toString()+" inside\n")
    else:     
        w.write(i.toString()+" outside\n")
w.close()
#closest points in the area needs to be found out... 

