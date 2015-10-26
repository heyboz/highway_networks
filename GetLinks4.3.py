import shapefile
mydbf = open('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine_FeatureVerticesToPo.dbf','rb')
dbf = shapefile.Reader(dbf = mydbf)
r = list(dbf.iterRecords())
'''creat dictionary of id:[indices] & pointXY:[id]'''
dxy = {}
did = {}
dix = {}
dkm = {}
fxy = []
for i in xrange(len(r)):
	r[i][5:] = [r[i][5] + ',' + r[i][6]]
	oid = r[i][3]
	did.setdefault(oid, []).append(i)
	xy = r[i][5]
	dxy.setdefault(xy, []).append(oid)
	dkm.setdefault(oid, r[i][4])
	dix[i] = xy
'''start to delete false intersections'''
for j in iter(dxy):
	if len(dxy[j]) == 2:
		print dxy[j]
		p1id = dxy[j][0]
		p2id = dxy[j][1]
		p2i = did[p2id]
		del p2i[1]
		p2xy = dix[p2i[0]]
		dxy[p2xy] = p1id
		dkm[p1id] = dkm[p1id] + dkm[p2id]
		fxy.append(j)
for k in fxy:
	del dxy[k]
print dxy
