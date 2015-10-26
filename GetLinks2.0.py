###read data
import xlrd

#line = xlrd.open_workbook('F:\\workspace\\arcgis\\nhpnv14-05shp\\for_python\\NHPNLine_100.xlsx')
#sheetl = line.sheets()[0]
#idl = sheetl.col_values(3, start_rowx = 1)
#km = sheetl.col_values(4, start_rowx = 1)
#ft = sheetl.col_values(2, start_rowx = 1)

intersect = xlrd.open_workbook('F:\\workspace\\arcgis\\nhpnv14-05shp\\for_python\\NHPNspatialjoin_100.xlsx')
sheeti = intersect.sheets()[0]

idi = sheeti.col_values(3, start_rowx = 1)
x = sheeti.col_values(4, start_rowx = 1)
y = sheeti.col_values(5, start_rowx = 1)
coordinate = zip(x, y)

###define functions
#to find the indexs of all the points shared same coordinate
def myfind(x,y):
	Indexlist = [a for a in range(len(y)) if y[a] == x]
	return (x, Indexlist)
    
#to find the other point shared the same id
def anotherpoint(c):
    c12index = list(myfind(idi[c], idi))[1]
    forremove = c12index[:]
    forremove.remove(c)
    c2index = forremove[0]
    return c2index
    
#calulate distance with haversine formula    
from math import radians, cos, sin, asin, sqrt  
def haversine(x1, y1, x2, y2):  
    x1, y1, x2, y2 = map(radians, [x1, y1, x2, y2])
    dx = x2 - x1   
    dy = y2 - y1
    r = 6371.004 #radius(km)
    d = 2*r*asin(sqrt(sin(dx/2)**2 + cos(x1) * cos(x2) * sin(dy/2)**2))  
    return d 

print "I'm ready!"

km = {}
c = 0
a = len(coordinate)
while c+2 < a:
    if coordinate[c] == coordinate[c+1] and coordinate[c] != coordinate[c+2]:
        #find related point: c2, c1(twice), c3
        try:
            c2index = anotherpoint(c)
            c3index = anotherpoint(c+1)
            print c2index, c3index
        except IndexError:
            print 'indexerror'
            c = c+2
            continue
        c1 = coordinate[c]
        c2 = coordinate[c2index]
        c3 = coordinate[c3index]
        #set new point
        idi[c2index] == idi[c]
        idi[c3index] == idi[c]
        #calulate distance
        d21 = haversine(c2[0],c2[1],c1[0],c1[1])
        d13 = haversine(c1[0],c1[1],c3[0],c3[1])
        d23 = d21 + d13
        km[idi[c2index]] = d23
        #delete c1
        coordinate[c] = 'none'
        coordinate[c+1] = 'none'
        idi[c] = 'none'
        idi[c+1] = 'none'
        print km
        c = c+2
    else:
        print 'continue'
        c = c+1
