import shapefile
#from operator import itemgetter, attrgetter
mydbf = open('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine_FeatureVerticesToPo.dbf','rb')
dbf = shapefile.Reader(dbf = mydbf)
#fields = dbf.fields
r = list(dbf.records())
#print fields
#print r[:5]
#s = sorted(r, key = itemgetter(5))#sorted by x
#print s[:5]
d = {}
for i in xrange(len(r)):
	oid = r[i][3]
	#if oid not in d:
		#d[oid] = [i]
	#else:
		#d[oid].append(i)
	d.setdefault(oid, []).append(i)
