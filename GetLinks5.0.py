import shapefile
from operator import itemgetter, attrgetter
from compiler.ast import flatten
import copy
dbf = shapefile.Reader('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine_FeatureVerticesToPo1.dbf')

def newdic(d, key, value):
	if key not in d:
		d[key] = [value]
	else:
		if value not in d[key]:
			d[key].append(value)
	return d

'''list the records, zip (x,y)'''
r = []
for ir in dbf.iterRecords():
	ir[6:] = [(round(float(ir[6]),6),round(float(ir[7]),6))]
	ir[5] = str(ir[5])
	r.append(ir)
l = len(r)

'''creat dictionaries of points to id, id to points, id to km'''
xy_id = {}
id_xy = {}
km = {}
for i in xrange(l):
	xy = r[i][6]
	oid = r[i][5]
	newdic(d=xy_id, key=xy, value=oid)
	newdic(d=id_xy, key=oid, value=xy)
	km.setdefault(oid, float(r[i][4]))#values is not list
ids = id_xy.keys()
for idi in ids:
	if len(id_xy[idi]) == 1:
		v = id_xy[idi]
		del id_xy[idi]
		xy_id[v[0]].remove(idi)
print len(id_xy)

'''start to delete false intersections'''
f = []
xys = xy_id.keys()
for a in xys:
	if len(xy_id[a]) == 2:
		(id1, id2) = xy_id[a]

		path1 = id_xy[id1] #a,p1
		path1.remove(a) #p1
		path2 = id_xy[id2] #a,p2
		path2.remove(a) #p2

		f.append(a)
		#del xy_id[a] #delete "j:[id1,id2]"
		#del id_xy[id2] #delete "id2:[p2]"

		newid = id1+'_'+id2
		xy_id[path1[0]].remove(id1) #replace "p2:[id2,idx]"
		if newid not in xy_id[path1[0]]:
			xy_id[path1[0]].append(newid)
		xy_id[path2[0]].remove(id2) #replace "p2:[id2,idx]"
		if newid not in xy_id[path2[0]]:
			xy_id[path2[0]].append(newid)
		id_xy[newid] = [path1[0], path2[0]]
		km[newid] = km[id1] + km[id2]
for a in f:
	del xy_id[a]

		#if id1+0.1 not in xy_id[path2[0]]:
		#	xy_id[path2[0]].append(id1) #of "p2:[id1,idx]"
		#if path2[0] not in id_xy[id1]:
		#	id_xy[id1].extend(path2) #add p2 to "id1:[p1]"
vid = set(flatten(xy_id.values()))
kid = id_xy.keys()
n = 0
for kidi in kid:
	if kidi not in vid:
		del id_xy[kidi]
##get xy_id(vertice), id_xy(edge)
print n
print len(xy_id)
print len(id_xy)
print id_xy['375600']
print xy_id[(-78.837592, 35.949125)]
print id_xy['367240_367244']
print xy_id[(-79.693157, 40.491189)]
