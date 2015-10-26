import shapefile
mydbf = open('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine_FeatureVerticesToPo.dbf','rb')
dbf = shapefile.Reader(dbf = mydbf)
r = list(dbf.iterRecords())
t = []
f = []
for a in xrange(len(r)):
	p = [str(r[a][3]) + ':' + r[a][5] + ',' + r[a][6]]
	if p in t:
		r.remove(p)
	else: t.append(p)
print f
print len(t)