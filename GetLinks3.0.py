###read data
import xlrd
import xlwt
intersect = xlrd.open_workbook('F:\\workspace\\arcgis\\nhpnv14-05shp\\for_python\\NHPNLine_FeatureVerticesToPo1bothends_500.xlsx')
sheeti = intersect.sheets()[0]
idi = sheeti.col_values(3, start_rowx = 1)
x = sheeti.col_values(4, start_rowx = 1)
y = sheeti.col_values(5, start_rowx = 1)
coordinate = zip(x, y)

###define functions
def myfind(x,y):
    ''' to find the indexs of all the points shared same coordinate'''
    Indexlist = [a for a in range(len(y)) if y[a] == x]
    return Indexlist

def anotherpoint(c):
    ''' to find the other point shared the same id.'''
    c12index = myfind(idi[c], idi)
    forremove = c12index[:]
    if len(c12index)>2: print '>2'
    if len(c12index)==1: print '=1'
    forremove.remove(c)
    c2index = forremove[0]
    return c2index

from math import radians, cos, sin, asin, sqrt  
def haversine(x1, y1, x2, y2):
    ''' to calulate distance with haversine formula'''
    x1, y1, x2, y2 = map(radians, [x1, y1, x2, y2])
    dx = x2 - x1   
    dy = y2 - y1
    r = 6371.004 #radius(km)
    
    distance = 2*r*asin(sqrt(sin(dy/2)**2 + cos(y1) * cos(y2) * sin(dx/2)**2))  
    return distance

print "I'm ready!"

###delete false intersections
km = {}
c = 0
while c+2 < 20:#len(coordinate):
    if coordinate[c] == coordinate[c+1] and coordinate[c] != coordinate[c+2]:
        #find related point: c2, c1(twice), c3
        try: 
            c2index = anotherpoint(c)
            c3index = anotherpoint(c+1)
        except IndexError:
            print "missing anotherpoint, miaoji! id = %f"%idi[c]
            c += 2
            continue
        print c2index, c3index
        c1 = coordinate[c]
        c2 = coordinate[c2index]
        c3 = coordinate[c3index]
        #calulate distance, add km between c2 and c3 with id: idi[c]
        d21 = haversine(c2[0],c2[1],c1[0],c1[1])
        d13 = haversine(c1[0],c1[1],c3[0],c3[1])
        d23 = d21 + d13
        km[idi[c2index]] = d23
        print km
        #set the corresponding id of c2,c3 as idi[c] and clear the data of c1
        idi[c3index] == idi[c]
        del coordinate[c:c+2]
        del idi[c:c+2]
    else:
        while coordinate[c] == coordinate[c+1]:
                c = c+1
        print 'continue'
        c = c+1
kmitems = km.items()
for k in kmitems:
        if k[1] == 4:
                del d[k[0]]
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
for i in range(len(coordinate)):
        worksheet.write(i,0,idi[i])
        worksheet.write(i,1,coordinate[i][0])
        worksheet.write(i,2,coordinate[i][1])
        worksheet.write(i,3,km.get(idi[i]))
workbook.save('DelC1.xls')
