import shapefile
mydbf = open('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine_FeatureVerticesToPo.dbf','rb')
dbf = shapefile.Reader(dbf = mydbf)
r = list(dbf.iterRecords())
'''creat dictionary of id:[indices] & pointXY:[id]'''
dxy = {}
did = {}
dix = {}
dkm = {}
didxy = {}
for i in xrange(len(r)):
	r[i][5:] = [r[i][5] + ',' + r[i][6]]
	oid = r[i][3]
	did.setdefault(oid, []).append(i)
	xy = r[i][5]
	dxy.setdefault(xy, []).append(oid)
	dkm.setdefault(oid, r[i][4])
	dix[i] = xy
	dxi.setdefault(xy, []).append(i)
'''start to delete false intersections'''
for j in iter(dxy):
	if len(dxy[j]) == 2:
		for k in [0,1]:
			pid = dxy[j][k]
			pi = did[pid]
			del pi[1]
			pxy = dix[pi[0]]
			pid2 = [].append(pid)
			pi2 = [].append(pi)
			pxy2 = [].append(pxy)
		print pid2
		print pi2
		print pxy2
		didxy[pid2[0]] = [pxy2[0], pxy2[1]]
		dkm[pid2[0]] = dkm[pid2[0]] + dkm[pid2[1]
		dxy[pxy2[1]].remove(pid2[1]).append(pid2[0])
		did[pid2[0]].remove(dxi[j]).append([pi2[0], pi2[1]])
print dxy
