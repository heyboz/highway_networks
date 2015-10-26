import shapefile
mydbf = open('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine_FeatureVerticesToPo.dbf','rb')
dbf = shapefile.Reader(dbf = mydbf)
fields = dbf.fields
print fields
r = list(dbf.iterRecords())
'''creat dictionary of id:[indices]'''
did = {}
dxy = {}
for i in xrange(len(r)):
	r[i][5:] = [r[i][5] + ',' + r[i][6]]
	xy = r[i][5]
	oid = r[i][3]
	did.setdefault(oid, []).append(i)
	dxy.setdefault(xy, []).append(oid)
print dxy
