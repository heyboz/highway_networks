import shapefile
dbf = shapefile.Reader('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine.shp')
r = dbf.records()
l1 = len(r)
recid = []
for i in r:
	recid.append(i[2])
recid1 = list(set(recid))
l2 = len(recid1)
print l1-l2