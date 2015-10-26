import shapefile
mydbf = open('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine_FeatureVerticesToPo.dbf','rb')
dbf = shapefile.Reader(dbf = mydbf)
r = list(dbf.iterRecords())
'''creat dictionary of id:[indices] & pointXY:[id]'''
xy_id = {}
id_xy = {}
km = {}
for i in xrange(len(r)):
	r[i][5:] = [r[i][5] + ',' + r[i][6]]
	xy = r[i][5]
	oid = r[i][3]
	xy_id.setdefault(xy, []).append(oid)
	id_xy.setdefault(oid, []).append(xy)
	km.setdefault(oid, r[i][4])
'''start to delete false intersections'''
xys = xy_id.keys()
for j in xys:#j = p0
	if len(xy_id[j]) == 2:
		id1 = xy_id[j][0]#the one of id of p0(pathA)
		id2 = xy_id[j][1]#the other id of p0(pathB)
		xy1 = id_xy[id1]#points of pathA(p0,p1)
		xy1.remove(j)#the other point of pathA(p1), remove p0 in "[id1:p0,p1]"
		xy2 = id_xy[id2]#points of pathB(p0,p2)
		xy2.remove(j)#the other point of pathA(p2), remove p0 in "[id2:p0,p2]"
		del xy_id[j]#delete the records "j:[id1,id2]" in xy_id
		del id_xy[id2]#delete the records "id2:[p2]" in id_xy
		xy_id[xy2[0]].remove(id2)#replace the records "p2:[id2,idx]" 
		xy_id[xy2[0]].append(id1)#of "p2:[id1,idx]" ##xy2 is list
		try:
			id_xy[id1].append(xy2)#add p2 to "id1:[p1]"
		except KeyError:
			print id1
			break
print 'miaoji'
