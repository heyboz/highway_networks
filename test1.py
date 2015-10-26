import shapefile
from operator import itemgetter, attrgetter
mydbf = open('F:/workspace/arcgis/nhpnv14-05shp/vertice_to_point/NHPNLine_FeatureVerticesToPo.dbf','rb')
dbf = shapefile.Reader(dbf = mydbf)

r = []
for a in dbf.iterRecords():
	a[5:] = [(a[5] + ',' + a[6])]
	r.append(a)

l = len(r)
s = sorted(r, key = itemgetter(3,5))#sorted by x
print s[:5]
f = []
i = 0
while i+1 < l:
	if s[i][3] == s[i+1][3] and s[i][5] == s[i+1][5] and s[i] != s[i+1]:
		f.append(zip(s[i],s[i+1]))
	i += 1
print f