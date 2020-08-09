def existanceTest(MSlistOrd):
    ms1,ms2,ms3,ms4,ms5=MSlistOrd[0][5],MSlistOrd[1][5],MSlistOrd[2][5],MSlistOrd[3][5],MSlistOrd[4][5]
    moyemMS=(ms1+ ms2+ ms3+ ms4 + ms5)/500
    print("mmmmoooyen ms",moyemMS)
    if (ms1 > 25):

    #if (moyemMS > 100/500):
        exist=True
        Mscor=MSlistOrd[0][5]
        FullName = MSlistOrd[0][1]
    #if (MSlistOrd[0][5]!= 0 ):
        print("  exist",exist,FullName, Mscor)
    else:
        exist = False
        print("Not exist",exist)
        Mscor = MSlistOrd[0][5]
        FullName = MSlistOrd[0][1]
        print("similar to ", FullName )
    return exist,Mscor,FullName,moyemMS
'''MSlistOrd=[(100,'najah',28,100,0)]

exi=existanceTest(MSlistOrd)'''