import shapefile
mydbf = open('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine_FeatureVerticesToPo.dbf','rb')
dbf = shapefile.Reader(dbf = mydbf)
r = []
for a in dbf.iterRecords():
	a[5:] = [(a[5] + ',' + a[6])]
	r.append(a)
'''creat dictionary of id:[indices]'''
did = {}
dxy = {}
for i in xrange(len(r)):
	oid = r[i][3]
	xy = r[i][5]
	did.setdefault(oid, []).append(i)
	dxy.setdefault(xy, []).append(oid)
