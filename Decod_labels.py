from typing import List

import Models_Predections as mp
listW, listB = [], []
listPredW = [0, 0, -1, -1, -1]
listPredB = [0, 0, -1, -1, -1]
ListPredicted_W = ['WearingShoes', 'W_Teenagers','W_T_M_X(OT)','29']
#ListPredicted_W = ['WearingShoes', 'W_Teenagers','29']

ListPredicted_B = ['Barefoot', 'B_Teenagers','B_T_M_I(S)','55']
#ListPredicted_B = ['Barefoot', 'B_Kids','45']
# decoder list nadjah
#listW=[0,1,2,1,39]
def decod_list_W(ListPredicted_W):
    # ----------------Barefoot/Wearing---------------
    listPredW[1] = 1
    # ----------------Kids/Teenagers/Adults---------------
    if ListPredicted_W[1] == mp.l_W_AgeG[0]:
        listPredW[2] = 2
    elif ListPredicted_W[1] == mp.l_W_AgeG[1]:
        listPredW[2] = 0
    else:
        listPredW[2] = 1
    # ----------------X/O/II---------------------------
    # -----W----Adults--XOII------#
    if len(ListPredicted_W) == 4:
        if ListPredicted_W[2] == mp.l_W_A_M_X[0]:
            listPredW[3] = 1
        elif ListPredicted_W[2] == mp.l_W_A_M_X[1]:
            listPredW[3] = 0
        else:
            listPredW[3] = 2
            # -----W--- Kids-XOII----------#
        if ListPredicted_W[2] == mp.l_W_K_M_X[0]:
            listPredW[3] = 1
        elif ListPredicted_W[2] == mp.l_W_K_M_X[1]:
            listPredW[3] = 0
        else:
            listPredW[3] = 2
            # -----W----Teenagers--XOII------#
        if ListPredicted_W[2] == mp.l_W_T_M_X[0]:
            listPredW[3] = 1
        elif ListPredicted_W[2] == mp.l_W_T_M_X[1]:
            listPredW[3] = 0
        else:
            listPredW[3] = 2

    lastIndex_W = len(ListPredicted_W) - 1
    listPredW[4] = int(ListPredicted_W[(lastIndex_W)])
    listW=listPredW
    print("listW------",listW)
    return listW
def decod_list_B(ListPredicted_B):
    # ----------------Barefoot/Wearing---------------
    listPredB[0] = 1
        # -----B--Age groupe----------#
    if ListPredicted_B[1] == mp.l_B_AgeG[0]:
            listPredB[2] = 2
    elif ListPredicted_B[1] == mp.l_B_AgeG[1]:
            listPredB[2] = 0
    else:
        listPredB[2] = 1
        # -----B----Adults--XOII------#
    if len(ListPredicted_B) == 4:
        if ListPredicted_B[2] == mp.l_B_A_M_X[0]:
                listPredB[3] = 1
        elif ListPredicted_B[2] == mp.l_B_A_M_X[1]:
                listPredB[3] = 0
        else:
            listPredB[3] = 2
            # -----B--- Kids-XOII----------#
        if ListPredicted_B[2] == mp.l_B_K_M_X[0]:
            listPredB[3] = 1
        elif ListPredicted_B[2] == mp.l_B_K_M_X[1]:
            listPredB[3] = 0
        else:
            listPredB[3] = 2
            # -----B----Teenagers--XOII------#
        if ListPredicted_B[2] == mp.l_B_T_M_X[0]:
            listPredB[3] = 1
        elif ListPredicted_B[2] == mp.l_B_T_M_X[1]:
            listPredB[3] = 0
        else:
            listPredB[3] = 2
    lastIndex_B = len(ListPredicted_B) - 1
    listPredB[4] = int(ListPredicted_B[(lastIndex_B)])
    listB = listPredB
    print("listB-----",listB)
    return listB
'''if mp.max_W_B_pred == mp.l_W_B[0]:
   lB= decod_list_B(ListPredicted_B)
else:
    lW = decod_list_B(ListPredicted_B)'''
print(listPredW)#[1, 1, -1, 1, 39]
print(listPredB)#[1, 1, -1, 1, 39]

print("**********************************")
lB = decod_list_B(ListPredicted_B)
print("lB",lB)
lW = decod_list_W(ListPredicted_W)
print("lW",lW)
'''    if ListPredicted_W[0] == mp.l_W_B[0]:
        listPred[0] = -1
        listPred[1] = 1'''