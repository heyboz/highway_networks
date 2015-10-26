###read data: NHPNLine->dic(IDi(km:, FacilityT:));
###read data: NHPNinersect/vertice_to_point->dic(TFIDi((Xi,Yi):IDi)
import xlrd
Line = xlrd.open_workbook('F:\\workspace\\arcgis\\nhpnv14-05shp\\for_python\\NHPNLine_100.xlsx')
sheetL = Line.sheets()[0]

IDL = sheetL.col_values(3, start_rowx = 1)
#KM = sheetL.col_values(4, start_rowx = 1)
#FT = sheetL.col_values(2, start_rowx = 1)

Intersect = xlrd.open_workbook('F:\\workspace\\arcgis\\nhpnv14-05shp\\for_python\\NHPNspatialjoin_100.xlsx')
sheetI = Intersect.sheets()[0]

TFID = sheetI.col_values(1, start_rowx = 1)
IDI = sheetI.col_values(3, start_rowx = 1)
X = sheetI.col_values(4, start_rowx = 1)
Y = sheetI.col_values(5, start_rowx = 1)
Coordinate = zip(X, Y)

###
def myfind(x,y):
	Indexlist = [a for a in range(len(y)) if y[a] == x]
	return (x, Indexlist)
Links = list()
Nodes = list()
for c in Coordinate[:10]:
    SameC = myfind(c,Coordinate)
    print 'the same coordinate: ',SameC
    print SameC
    Indexlist = SameC[1]
    ##get beginpoint & endpoint and remove the same coordinate
    Link = list()
    if len(Indexlist) == 2:
        for i in Indexlist:
            AnotherpointID = IDI[i]
            try:
                SameIdIndex = list(myfind(AnotherpointID, IDI))[1]
                Forremove = SameIdIndex[:]
                Forremove.remove(i)
                AnotherpointIndex = Forremove[0]
                Anotherpoint = Coordinate[AnotherpointIndex]
                Link.append(Anotherpoint)####FT
                #Nodes.append(Anotherpoint)
            except IndexError:
                #ErrorKM = list().append(KM[IDL.index(AnotherpointID)])
                ErrorID = list().append(AnotherpointID)
                print 'IndexError'
            except:
                print 'unknown error'
        if Link != []: Links.append(Link)
        print 'Add a new Link:', Link
        #print 'Now we have links:', Links
        #print 'Now we have nodes:', Nodes
        FordelID = [IDI[Indexlist[0]],IDI[Indexlist[1]]]
        FordelC = [Coordinate[Indexlist[0]],Coordinate[Indexlist[1]]]
        for dd in FordelID: IDI.remove(dd)
        for dc in FordelC: Coordinate.remove(dc)
    else: print 'the num of SameXY != 2'
#print ('ErrorID:',ErrorID, 'ErrorKM:',sum(ErrorKM))


####################################################################
print "I suddenly aware that I am too young too simple...so let's try again. "

