from operator import itemgetter, attrgetter
'''Matching_MS_Ids = [
(50	, 0.463, 50,'TOUANSSA Insaf'),
(51	, 0.085, 100,'EIMIRAT Meriem'),
(1, 0.06, 25,'Abdelkader gitoubi'),
(13	, 0.056, 75,'Nouajea mouhammed arbi'),
(3	, 0.055, 25,'BEGGAS soumaiya')
]'''
'''print (Matching_MS_Ids)
Matching_MS_Ids.sort(reverse=True, key=lambda Matching_MS_Ids: Matching_MS_Ids[2])
print("Sorted Matching List", Matching_MS_Ids)
#sorted(Matching_MS_Ids, key=lambda Matching_MS_Ids: Matching_MS_Ids[2],reverse=True)
#print("sorted", sorted(Matching_MS_Ids, key=lambda Matching_MS_Ids: Matching_MS_Ids[2]))


sorted(Matching_MS_Ids, key=itemgetter(2,1),reverse=True)#sort list MS first then Prob id predictions
print("goal achived", Matching_MS_Ids)'''
def sortFinalMachingList(MSlist):
    print("MSlist befor",MSlist)

    MSlist.sort(reverse=True, key=lambda MSlist: MSlist[6])
    #sorted(MSlist, key=itemgetter(2, 1), reverse=True)  # sort list MS first then Prob id predictions
    MSlist_=sorted(MSlist, key=itemgetter(5, 6), reverse=True)  # sort list MS first then Prob id predictions
    print("sortFinalMachingList goal achived",MSlist_)
    return MSlist_
'''MSlist_11 = [
(50, 0.763	,50 	,'TOUANSSA Insaf'),
(1	,0.078	,25 	,'EIMIRAT Meriem'),
(8	,0.044	,50 	,'Abdelkader gitoubi'	),
(9	,0.036	,25	,'Nouajea mouhammed arbi'),
(48	,0.028	,25 	,'BEGGAS soumaiya'	)
]
MSlist_ = [
(50, 'TOUANSSA Insaf', 23, 1.78, 85, 75, 0.763),
(1, 'EIMIRAT Meriem ', 22, 1.65, 50, 100, 0.078),
(48, 'BEGGAS soumaiya', 20, 1.6, 47, 50, 0.028),
(9, 'Nouajea mouhammed arbi', 19, 1.7, 68, 50, 0.036),
(8, 'Abdelkader gitoubi', 19, 1.82, 61, 50, 0.044)]
MSlist=sortFinalMachingList(MSlist_)
print("goooooooooood job  najah MS list sorted",MSlist)'''