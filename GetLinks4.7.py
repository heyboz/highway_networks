import shapefile
from operator import itemgetter, attrgetter
import copy
mydbf = open('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine_FeatureVerticesToPo1.dbf','rb')
dbf = shapefile.Reader(dbf = mydbf)

'''list the records, zip (x,y)'''
r = []
for ir in dbf.iterRecords():
	ir[6:] = [(round(float(ir[6]),6),round(float(ir[7]),6))]
	r.append(ir)
print r[:5]

'''sort and copy'''
s = sorted(r, key = itemgetter(2,6))#sorted by x
c = copy.deepcopy(s)

'''find and remove the duplicates'''
l = len(r)
f = []
i = 0
while i+1 < l:
	if s[i][3] == s[i+1][3] and s[i][5] == s[i+1][5]:
		f.append(i)
	i += 1
for j in f:
	c.remove(s[j])
newl = len(c)
#m = 0
#for ix in xrange(newl):
#	if isinstance(c[ix][5],list):
#		print c[ix][5]
#	if type(c[ix][5]) is tuple:
#		m+=1
#print m
#exit()
##no r[ix][5] was printed. [(x,y),(x,y)] is not from here

'''creat dictionaries of points to id, id to points, id to km'''
xy_id = {}
id_xy = {}
km = {}
for i in xrange(newl):
	xy = c[i][6]
	oid = c[i][2]
	xy_id.setdefault(xy, []).append(oid)#values is list
	id_xy.setdefault(oid, []).append(xy)#values is list
	km.setdefault(oid, c[i][4])#values is not list
print len(id_xy)
p = 0
q = 0
ids = id_xy.keys()
for idi in ids:
	if len(id_xy[idi]) == 1:
		p+=1
		del id_xy[idi]
	if len(id_xy[idi]) > 2:
		q+=1
print (p,q)
exit()

'''start to delete false intersections'''
xys = xy_id.keys()
for a in xys: #j = p0
	if len(xy_id[a]) == 2:
		(id1, id2) = xy_id[a]

		path1 = id_xy[id1] #points of pathA(p0,p1)
		#path1 = [s for i in path1 for s in i]
		path1.remove(a) #the other point of pathA(p1), remove p0 in "[id1:p0,p1]"
		try:
			path2 = id_xy[id2] #points of pathB(p0,p2)
		except KeyError: print (id2, [xy_id[a]], a)
		#path2 = [s for i in path2 for s in i]
		path2.remove(a) #the other point of pathA(p2), remove p0 in "[id2:p0,p2]"

		del xy_id[a] #delete the records "j:[id1,id2]" in xy_id
		del id_xy[id2] #delete the records "id2:[p2]" in id_xy

		xy_id[path2[0]].remove(id2) #replace the records "p2:[id2,idx]"
		xy_id[path2[0]].append(id1) #of "p2:[id1,idx]" ##xy2 is list
		id_xy[id1].append(path2[0]) #add p2 to "id1:[p1]"
		####append add list as list but not element! error is from here
print id_xy[3400001925]
