import shapefile
mydbf = open('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine_FeatureVerticesToPo.dbf','rb')
dbf = shapefile.Reader(dbf = mydbf)
r = list(dbf.iterRecords())
'''creat dictionary of id:[indices] & pointXY:[id]'''
xy_id = {}
id_xy = {}
solitude = []
for i in xrange(len(r)):
	r[i][5:] = [(round(float(r[i][5]), 6),round(float(r[i][6]), 6))]
	xy = r[i][5]
	oid = r[i][3]
	xy_id.setdefault(xy, []).append(oid)
	id_xy.setdefault(oid, []).append(xy)
'''start to delete false intersections'''
xys = xy_id.keys()
for j in xys:#j = p0
    if len(xy_id[j]) == 1:
    	print xy_id[j]
    	solitude.append(xy_id[j])
print solitude
print len(solitude)
