import shapefile
from operator import itemgetter, attrgetter
import copy
mydbf = open('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine_FeatureVerticesToPo.dbf','rb')
dbf = shapefile.Reader(dbf = mydbf)
'''list the records, zip (x,y)'''
r = []
for a in dbf.iterRecords():
	a[5:] = [(a[5] + ',' + a[6])]
	r.append(a)
'''sort and copy'''
s = sorted(r, key = itemgetter(3,5))#sorted by x
c = copy.deepcopy(s)
'''find and remove the duplicates'''
l = len(r)
f = []
i = 0
while i+1 < l:
	if s[i][3] == s[i+1][3] and s[i][5] == s[i+1][5]:
		f.append(i)
	i += 1
print len(f)
for j in f:
	c.remove(s[j])
newl = len(s)
'''creat dictionaries of points to id, id to points, id to km'''
id_xy = {}
km = {}
for i in xrange(newl):
	xy = c[i][5]
	oid = c[i][3]
	xy_id.setdefault(xy, []).append(oid)
	id_xy.setdefault(oid, []).append(xy)
	km.setdefault(oid, c[i][4])
print id_xy[3400001925]
print xy_id['-7.46943780000e+001,4.06065980000e+001']

'''start to delete false intersections'''
xys = xy_id.keys()
for a in xys: #j = p0
	if len(xy_id[a]) == 2:
		(id1, id2) = xy_id[a]
		if id1==id2: print id_xy[id1]

		path1 = id_xy[id1] #points of pathA(p0,p1)
		path1.remove(a) #the other point of pathA(p1), remove p0 in "[id1:p0,p1]"
		path2 = id_xy[id2] #points of pathB(p0,p2)
		path2.remove(a) #the other point of pathA(p2), remove p0 in "[id2:p0,p2]"

		del xy_id[a] #delete the records "j:[id1,id2]" in xy_id
		del id_xy[id2] #delete the records "id2:[p2]" in id_xy

		xy_id[path2[0]].remove(id2) #replace the records "p2:[id2,idx]"
		xy_id[path2[0]].append(id1) #of "p2:[id1,idx]" ##xy2 is list
		id_xy[id1].append(path2) #add p2 to "id1:[p1]"
print 'miaoji'
