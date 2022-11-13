# from LexicalNew import tokenlist
from seFunction import declarationError, highestScope, insertenumconst, createScope, destroyScope, insertAttribute, insertFunctionTable, insertMainTable, lookupAttributeTable, lookupFunctionTable, lookupMainTable, scopeStack_, binTypeCompatible, uniTypeCompatible, mainTable_, functionTable_, redeclarationError, createScope, destroyScope

error = ""
errorList = []
currentFunction = 0
currentScope = 0
# print(tokenlist)
tokenType = []
tokenValue = []
i = 0
currentClass = ""
mainTableTypeMOD = ""
multipleInterface = []
extendingClass = ""
mainTableType = ""
enumlist = []
accessMODvalue = ""
isStatic = False
isFinal = False
isAbstract = False
signature = []
isFunc = False
# for line in tokenlist:
#     tokenType.append(line[0])
#     tokenValue.append(line[1])

# tokenType.append("EOF")
# tokenValue.append("EOF")

# print(tokenType)


def clearAccesandNonAccess():
    global accessMODvalue, isStatic, isFinal, isAbstract
    accessMODvalue = ""
    isStatic = False
    isFinal = False
    isAbstract = False


def calclateLineNo(itr):
    # allLines[itr] = allLines[itr].replace("(", "")
    # allLines[itr] = allLines[itr].replace(")", "")
    theLine = allLines[itr].split(",")
    return theLine[2]


def errorMesssage(itr):
    errorString = 'invalid syntax at line :', calclateLineNo(
        itr), 'the token : ', allLines[itr], "after ", allLines[itr+1], "before r ", allLines[itr-1]
    errorList.append(errorString)


    # print('invalid syntax at line :' , calclateLineNo(itr) , 'the token : ', allLines[itr])
# --------------------
resultFile = open("result.txt")

a = resultFile.read()
allLines = a.split("\n")
tokenType = []
tokenLine = []

for line in allLines:
    splitted = line.split(",")
    if(len(splitted) > 2):
        tokenType.append(splitted[0])
        tokenValue.append(splitted[1])

tokenType.append("EOF")
tokenValue.append("EOF")
print('<<<<<<<<<<<<<<<<<<<<<<<<<EXTRAS START>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(tokenType)
print('<<<<<<<<<<<<<<<<<<<<<<<<<EXTRAS END>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def MVA():
    global i, tokenType
    if func_def():
        return True
    elif Decl():
        return True
    elif abs_func_def():
        return True
    elif construct_def():
        return True
    else:
        return False


def MVC():
    global i, tokenType
    if func_def():
        return True
    elif Decl():
        return True
    elif construct_def():
        return True
    else:
        return False


def AM():
    global i, tokenType
    if tokenType[i] == "public":
        i = i + 1
        return True
    elif tokenType[i] == "private":
        i = i + 1
        return True
    else:
        return True


def NAMS():
    global i, tokenType, isStatic
    if tokenType[i] == "static":
        isStatic = True
        i = i + 1
        return True
    else:
        return True


def TSD():
    global i, tokenType
    if TS():
        if tokenType[i] == "dot":
            i = i + 1
            return True
        else:
            errorMesssage(i)
            return False
    else:
        return False


def for_B():
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        if Exp():
            return True
        else:
            return False
    elif tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i + 1
            if for_B():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    elif tokenType[i] == "incDec":
        i = i + 1
        return True
    elif tokenType[i] == "openroundbrace":
        i = i + 1
        if Args():
            if tokenType[i] == "closeroundbrace":
                i = i + 1
                if FNB():
                    return True
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    elif tokenType[i] == "opensquarebrace":
        i = i + 1
        if Exp():
            if tokenType[i] == "closesquarebrace":
                i = i+1
                if D2DA():
                    if Ref2():
                        if ETExp():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def FNB():
    global i, tokenType
    if tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i + 1
            if for_B():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def Ref2():
    global i, tokenType
    if tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i + 1
            if for_B():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return True


def ETExp():
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        if Exp():
            return True
        else:
            return False
    else:
        return False


def mStringConst():
    global i, tokenType, enumlist
    if tokenType[i] == "comma":
        i = i + 1
        if tokenType[i] == "stringConst":
            enumlist.append(tokenValue[i])
            i = i + 1
            if mStringConst():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return True


def TRAS():
    global i, tokenType
    print("IN TRASSSSSSS 3333333333", tokenType[i])
    if TSD():
        print("TSD TRUEEEEEEEEEE", errorList)

        if tokenType[i] == "identifier":
            first = tokenValue[i]
            print("IN TRASSSSSSSSSSSSSSS")
            i = i + 1
            if MAS(first):
                return True
            else:
                return False
        else:
            print("idFALSE", errorList)
            errorMesssage(i)
            return False
    elif tokenType[i] == "identifier":
        first = tokenValue[i]
        print("IN TRASSSSSSSSSSSSSSS")
        i = i + 1
        if MAS(first):
            return True
        else:
            return False
    else:
        return False


def D2DA():
    global i, tokenType
    if tokenType[i] == "opensquarebrace":
        i = i + 1
        if Exp():
            if tokenType[i] == "closesquarebrace":
                i = i + 1
                return True
            else:
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return True


def ADT():
    global i, tokenType
    if tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i + 1
            if B():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    elif tokenType[i] == "openroundbrace":
        i = i + 1
        if Args():
            if tokenType[i] == "closeroundbrace":
                i = i + 1
                if tokenType[i] == "terminator":
                    i = i + 1
                    return True
                else:
                    errorMesssage(i)
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def TS():
    global i, tokenType
    if (tokenType[i] in ['this']):
        print(tokenType[i])
        i = i + 1
        return True
    elif tokenType[i] in ['super']:
        i = i + 1
        return True
    else:
        return False


def TAssign_st():
    global i, tokenType
    if TS():
        print("after ts")
        if ADT():
            return True
        else:
            return False
    else:
        return False


def FNA():
    global i, tokenType
    if tokenType[i] == "terminator":
        i = i + 1
        return True
    elif tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i+1
            if B():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def Ref():
    global i, tokenType
    if tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i+1
            if B():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return True


def EExp():
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        if Exp():
            if tokenType[i] == "terminator":
                i = i + 1
                return True
            else:
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def B():
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        print("IN EQUALS", tokenType[i])
        if Exp():
            print("IN EXPPPPP", tokenType[i])
            if tokenType[i] == "terminator":
                i = i+1
                return True
            else:
                errorMesssage(i)
                return False
        else:
            return False
    elif tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i + 1
            if B():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    elif tokenType[i] == "incDec":
        i = i + 1
        if tokenType[i] == "terminator":
            return True
        else:
            errorMesssage(i)
            return False
    elif tokenType[i] == "openroundbrace":
        i = i + 1
        if Args():
            print("ARGSSSSSS TRUEEEEEEEEEE", tokenType[i])
            if tokenType[i] == "closeroundbrace":
                i = i + 1
                if FNA():
                    return True
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    elif tokenType[i] == "opensquarebrace":
        i = i + 1
        if Exp():
            if tokenType[i] == "closesquarebrace":
                i = i+1
                if D2DA():
                    if Ref():
                        if EExp():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def LAS(parent):
    global i, tokenType, highestScope, accessMODvalue, isStatic, isAbstract, isFinal, currentClass
    if tokenType[i] == "equals":

        i = i + 1
        print('going in exp', tokenType[i])
        if Exp():
            print('after exp in las', tokenType[i])
            if tokenType[i] == "terminator":
                i = i+1
                return True
            else:
                errorMesssage(i)
                return False
        else:
            return False
    elif tokenType[i] == "dot":
        i = i + 1
        print("dot trueeeee")
        if tokenType[i] == "identifier":

            i = i + 1
            print("ID GAINNNNNNNN", tokenType[i])
            if B():
                print("inBBBBBBBBBBB ")
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    elif tokenType[i] == "incDec":
        i = i + 1
        if tokenType[i] == "terminator":
            i = i + 1
            return True
        else:
            print("NOT TERMMMMMMMMMMMMMM")
            errorMesssage(i)
            return False
    elif tokenType[i] == "identifier":
        iDforType = tokenValue[i]
        if(isFunc):
            check2 = lookupMainTable(parent)
            check = insertFunctionTable(iDforType, parent, highestScope)
        else:
            check2 = lookupMainTable(parent)
            check = insertAttribute(
                iDforType,  parent, accessMODvalue, isStatic, isAbstract, isFinal, currentClass)
        i = i + 1
        if OBJR() and check and check2:
            return True
        else:
            if(check2 == False):
                errorList.append(declarationError(parent))
                return False
            if(check == False):
                errorList.append(redeclarationError(iDforType))
                return False
            return False
    elif tokenType[i] == "openroundbrace":
        i = i + 1
        if Args():
            print("ERRRRRAAGHAHGA", tokenType[i])
            if tokenType[i] == "closeroundbrace":
                i = i + 1
                if FNA():
                    return True
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    elif tokenType[i] == "opensquarebrace":
        i = i + 1
        if Exp():
            if tokenType[i] == "closesquarebrace":
                i = i+1
                if D2DA():
                    if Ref():
                        if EExp():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def Assign_st():
    global i, tokenType
    if tokenType[i] == "identifier":
        iDforType = tokenValue[i]
        # lookup
        i = i + 1
        print("IN IDDDDDDDDDDDDDDD", tokenType[i])
        check = LAS(iDforType)
        if check:
            print("LAS TRUEEEEEEEEEEEEE", tokenType[i])
            return True
        else:
            return False
    else:
        return False


def VAS():
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        if Exp():
            return True
        else:
            return False
    elif tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            i = i + 1
            if for_B():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    elif tokenType[i] == "incDec":
        i = i + 1
        return True
    else:
        return False


def OBJ():
    global i, tokenType
    if tokenType[i] == "identifier":
        i = i + 1
        if OBJR():
            return True
        else:
            return False
    else:
        return False


def OBJR():
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        if tokenType[i] == "new":
            i = i + 1
            if tokenType[i] == "identifier":
                i = i + 1
                if tokenType[i] == "openroundbrace":
                    i = i + 1
                    if Args():
                        if tokenType[i] == "closeroundbrace":
                            i = i + 1
                            if tokenType[i] == "terminator":
                                i = i + 1
                                return True
                            else:
                                errorMesssage(i)
                                return False
                        else:
                            errorMesssage(i)
                            return False
                    else:
                        return False
                else:
                    errorMesssage(i)
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            errorMesssage(i)
            return False
    elif tokenType[i] == "terminator":
        i = i + 1
        return True
    else:
        return False


def Ref1():
    global i, tokenType
    if tokenType[i] == "dot":
        i = i + 1
        if tokenType[i] == "identifier":
            first = tokenValue[i]
            i = i + 1
            if MAS(first):
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return True


def MAS(parent):
    global i, tokenType, currentClass
    searchIn = parent
    print("IN MAS", tokenType[i])
    if tokenType[i] == "dot":
        if(searchIn != ""):
            print('lookup')
        # print("dot true : parent in mas ", parent)
        # chk = lookupFunctionTable(parent)
        # print('chk in MAS', chk)
        # if(chk == False):
        #     print('not access able in currrent scope')
        #     return False
        # if(chk in ["intConst", "stringConst", "charConst", "boolConst", "floatConst"]):
        #     print('cannot refer premittive type')
        #     return False
        # searchIn = chk
        # print('the first parent ,', chk)
        i = i + 1
        if tokenType[i] == "identifier":
            first = tokenValue[i]
            lookupAttributeTable(tokenValue[i], "~", searchIn)
            i = i + 1
            if MAS(first):
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    elif tokenType[i] == "incDec":
        i = i + 1
        return True
    elif tokenType[i] == "openroundbrace":
        i = i + 1
        if Args():
            print("AFTER ARGS", tokenType[i])
            if tokenType[i] == "closeroundbrace":
                i = i + 1
                if Ref1():
                    print("efhjsfgwiufg")
                    return True
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    elif tokenType[i] == "opensquarebrace":
        i = i + 1
        if Exp():
            if tokenType[i] == "closesquarebrace":
                i = i+1
                if D2DA():
                    if Ref1():
                        print("ras true")
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return True


def Decl():
    global i, tokenType, currentClass, accessMODvalue, isStatic, isFinal, isAbstract, isFunc, highestScope
    if tokenType[i] == "dataType":
        dt = tokenValue[i]
        i = i + 1
        if tokenType[i] == "identifier":
            mainID = tokenValue[i]
            i = i+1
            check, arrDimen = AR(dt)
            if check:
                if(arrDimen != ""):
                    dt = arrDimen
                print("oppppppppppppppppppp", dt,
                      mainID, arrDimen, accessMODvalue, isStatic, isFinal, isAbstract, currentClass)
                if(isFunc == False):
                    isInserted = insertAttribute(
                        mainID,  dt, accessMODvalue, isStatic, isAbstract, isFinal, currentClass)
                else:
                    isInserted = insertFunctionTable(mainID, dt, highestScope)
                if init1() and isInserted:
                    if list1(dt):
                        return True
                    else:
                        return False
                else:
                    if (isInserted == False):
                        sms = redeclarationError(mainID)
                        errorList.append(sms)
                    return False
            else:
                return False
        else:
            return False

    else:
        return False


def AR(dt):
    global i, tokenType
    arryDimension = ''
    if tokenType[i] == "opensquarebrace":
        i = i + 1
        if ExpN():
            if tokenType[i] == "closesquarebrace":
                arryDimension = '[ %s ]' % (dt)
                i = i + 1
                check, arryDimension2 = D2DB(arryDimension)
                if check:
                    if arryDimension2 == "":
                        return True, arryDimension
                    return True, arryDimension2
                else:
                    return False, arryDimension
            else:
                errorMesssage(i)
                return False, arryDimension
        else:
            return False, arryDimension
    else:
        return True, arryDimension


def D2DB(dt):
    global i, tokenType
    arryDimension = ''
    if tokenType[i] == "opensquarebrace":
        i = i + 1
        if ExpN():
            if tokenType[i] == "closesquarebrace":
                arryDimension = dt+dt
                print('the assdfwdf arraydimension', arryDimension, dt)
                i = i + 1
                return True, arryDimension
            else:
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return True, arryDimension


def list1(dt):
    global i, tokenType, accessMODvalue, isStatic, isFinal, isAbstract
    if tokenType[i] == "terminator":
        i = i + 1
        return True
    elif tokenType[i] == "comma":
        i = i + 1
        if tokenType[i] == "identifier":
            theID = tokenValue[i]
            i = i + 1
            check, arrDimen = AR(dt)
            if check:
                if(arrDimen != ""):
                    dt = arrDimen
                print("oppppppppppppppppppp list mod", dt,
                      theID, arrDimen, accessMODvalue, isStatic, isFinal, isAbstract, currentClass)
                isInserted = insertAttribute(
                    theID, dt, accessMODvalue, isStatic, isAbstract, isFinal, currentClass)
                if init1() and isInserted:
                    if list1(dt):
                        return True
                    else:
                        return False
                else:
                    if isInserted == False:
                        sms = redeclarationError(theID)
                        errorList.append(sms)
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def init1():
    global i, tokenType
    if tokenType[i] == "equals":
        i = i + 1
        if initD():
            return True
        else:
            errorMesssage(i)
            return False
    else:
        return True


def initD():
    global i, tokenType
    if TRAS():
        if init1():
            return True
        else:
            return False
    elif tokenType[i] in ["intConst", "stringConst", "charConst", "boolConst", "floatConst"]:
        i = i+1
        return True
    elif tokenType[i] == "opensquarebrace":
        i = i+1
        if Args():
            if tokenType[i] == "closesquarebrace":
                i = i+1
                return True
            else:
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def while_st():
    global i, tokenType
    if tokenType[i] == "while":
        i = i + 1
        if tokenType[i] == "openroundbrace":
            i = i + 1
            if Exp():
                if tokenType[i] == "closeroundbrace":
                    i = i + 1
                    if tokenType[i] == "opencurlybrace":
                        i = i + 1
                        if MST():
                            if tokenType[i] == "closecurlybrace":
                                i = i + 1
                                return True
                            else:
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        errorMesssage(i)
                        return False
                else:
                    errorMesssage(i)
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def for_st():
    global i, tokenType
    print("in for", tokenType[i])
    if tokenType[i] == "for":
        print("for true")
        i = i + 1
        if tokenType[i] == "openroundbrace":
            i = i + 1
            if P1():
                print("p1 tru", tokenType[i])
                if P2():
                    print("p2 tru", tokenType[i])
                    if tokenType[i] == "terminator":
                        i = i + 1
                        if P3():
                            print("p3 tru", tokenType[i])
                            if tokenType[i] == "closeroundbrace":
                                i = i + 1
                                if tokenType[i] == "opencurlybrace":
                                    i = i + 1
                                    if MST():
                                        if tokenType[i] == "closecurlybrace":
                                            i = i + 1
                                            print("for endeddddddd")
                                            return True
                                        else:
                                            errorMesssage(i)
                                            return False
                                    else:
                                        return False
                                else:
                                    errorMesssage(i)
                                    return False
                            else:
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def P1():
    global i, tokenType
    if Decl():
        return True
    elif Assign_st():
        return True
    elif tokenType[i] == "terminator":
        i = i + 1
        return True
    elif TAssign_st():
        return True
    else:
        return False


def P2():
    global i, tokenType
    if Exp():
        return True
    else:
        return True


def P3():
    global i, tokenType
    if for_assign():
        return True
    elif inc_dec():
        print("DECCCCCCCCCCC TRUUUEEE")
        return True
    else:
        return True


def for_assign():
    global i, tokenType
    if TSD():
        if tokenType[i] == "identifier":
            i = i + 1
            if VAS():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def inc_dec():
    global i, tokenType
    if tokenType[i] == "incDec":
        i = i + 1
        print("DECCCCCCCCC", tokenType[i])
        if tokenType[i] == "identifier":
            # look type

            # dt = tokenValue[i]
            i = i + 1
            return True, dt
        else:
            errorMesssage(i)
            return False
    else:
        return False


def switch_st():
    global i, tokenType
    if tokenType[i] == "switch":
        i = i + 1
        if tokenType[i] == "openroundbrace":
            i = i + 1
            if switch_in():
                if tokenType[i] == "closeroundbrace":
                    i = i + 1
                    if tokenType[i] == "opencurlybrace":
                        i = i + 1
                        if switch_B():
                            if tokenType[i] == "closecurlybrace":
                                i = i + 1
                                return True
                            else:
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        errorMesssage(i)
                        return False
                else:
                    errorMesssage(i)
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def switch_in():
    global i, tokenType
    if tokenType[i] in ["identifier", "intConst", "floatConst", "charConst", "stringConst", "boolConst"]:
        i = i + 1
        return True
    else:
        return False


def switch_B():
    global i, tokenType
    if condition():
        if tokenType[i] == "opencurlybrace":
            i = i + 1
            if MST():
                if tokenType[i] == "closecurlybrace":
                    i = i + 1
                    if switch_B():
                        return True
                    else:
                        return False
                else:
                    errorMesssage(i)
                    return False
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return True


def condition():
    global i, tokenType
    if tokenType[i] == "case":
        i = i + 1
        if tokenType[i] in {"intConst", "floatConst", "charConst", "stringConst", "boolConst"}:
            i = i + 1
            if tokenType[i] == "colon":
                i = i + 1
                return True
            else:
                errorMesssage(i)
                return False
        else:
            errorMesssage(i)
            return False

    elif tokenType[i] == "default":
        i = i + 1
        if tokenType[i] == "colon":
            i = i + 1
            return True
        else:
            errorMesssage(i)
            return False
    else:
        return False


def if_else_elif():
    global i, tokenType
    if tokenType[i] == "if":
        i = i + 1
        if Exp():
            if tokenType[i] == "opencurlybrace":
                i = i + 1
                if MST():
                    if tokenType[i] == "closecurlybrace":
                        i = i + 1
                        if elif_st():
                            if else_st():
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def elif_st():
    global i, tokenType
    if tokenType[i] == "elif":
        i = i + 1
        if Exp():
            if tokenType[i] == "opencurlybrace":
                i = i + 1
                if MST():
                    if tokenType[i] == "closecurlybrace":
                        i = i + 1
                        if elif_st():
                            return True
                        else:
                            return False
                    else:
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return True


def else_st():
    global i, tokenType
    if tokenType[i] == "else":
        i = i + 1
        if tokenType[i] == "colon":
            i = i + 1
            if tokenType[i] == "opencurlybrace":
                i = i + 1
                if MST():
                    if tokenType[i] == "closecurlybrace":
                        i = i + 1
                        return True
                    else:
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return True


def break_st():
    global i, tokenType
    if tokenType[i] == "break":
        i = i + 1
        if tokenType[i] == "terminator":
            i = i + 1
            return True
        else:
            errorMesssage(i)
            return False
    else:
        return False


def continue_st():
    global i, tokenType
    if tokenType[i] == "continue":
        i = i + 1
        if tokenType[i] == "terminator":
            i = i + 1
            return True
        else:
            return False
    else:
        return False


def return_st():
    global i, tokenType
    if tokenType[i] == "return":
        i = i + 1
        if ExpN():
            if tokenType[i] == "terminator":
                i = i + 1
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def ExpN():
    global i, tokenType
    if Exp():
        return True
    else:
        return True


def Args():
    global i, tokenType
    print("in argssssssss", tokenType[i])
    if Exp():
        print("exp trueeeeee")
        if ArgsD():
            return True
        else:
            return False
    else:
        print(errorList)
        print("EXP FALSEEEEE", tokenType[i])
        return True


def ArgsD():
    global i, tokenType
    print("in argsd")
    if tokenType[i] == "comma":
        i = i + 1
        if Exp():
            if ArgsD():
                return True
            else:
                return False
        else:
            return False
    else:
        return True


def try_catch_st():
    global i, tokenType
    if tokenType[i] == "try":
        i = i + 1
        if tokenType[i] == "opencurlybrace":
            i = i + 1
            if MST():
                if tokenType[i] == "closecurlybrace":
                    i = i + 1
                    if OTC():
                        return True
                    else:
                        return False
                else:
                    errorMesssage(i)
                    return False
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def OTC():
    global i, tokenType
    if tokenType[i] == "catch":
        i = i + 1
        if tokenType[i] == "openroundbrace":
            i = i + 1
            if tokenType[i] == "Exception":
                i = i + 1
                if tokenType[i] == "identifier":
                    i = i + 1
                    if tokenType[i] == "closeroundbrace":
                        i = i + 1
                        if tokenType[i] == "opencurlybrace":
                            i = i + 1
                            if MST():
                                if tokenType[i] == "closecurlybrace":
                                    i = i + 1
                                    if OTFD():
                                        return True
                                    else:
                                        return False
                                else:
                                    errorMesssage(i)
                                    return False
                            else:
                                return False
                        else:
                            errorMesssage(i)
                            return False
                    else:
                        errorMesssage(i)
                        return False
                else:
                    errorMesssage(i)
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    elif OTF():
        return True
    else:
        return False


def OTF():
    global i, tokenType
    if tokenType[i] == "finally":
        i = i + 1
        if tokenType[i] == "opencurlybrace":
            i = i + 1
            if MST():
                if tokenType[i] == "closecurlybrace":
                    i = i + 1
                else:
                    errorMesssage(i)
                    return False
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def OTFD():
    global i, tokenType
    if tokenType[i] == "finally":
        i = i + 1
        if tokenType[i] == "opencurlybrace":
            i = i + 1
            if MST():
                if tokenType[i] == "closecurlybrace":
                    i = i + 1
                else:
                    errorMesssage(i)
                    return False
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return True


def Exp():
    global i, tokenType
    if ANDOP():
        print("in Andop")
        if ExpD():
            return True
        else:
            return False
    else:
        return False


def ExpD():
    global i, tokenType
    if tokenType[i] == "LogicOp":
        i = i+1
        if ANDOP():
            if ExpD():
                return True
            else:
                return False
        else:
            return False
    else:
        return True


def ANDOP():
    global i, tokenType
    if ROPOP():
        if ANDOPD():
            return True
        else:
            return False
    else:
        return False


def ANDOPD():
    global i, tokenType
    if tokenType[i] == "LogicOp":
        i = i + 1
        if ROPOP():
            if ANDOPD():
                return True
            else:
                return False
        else:
            return False
    else:
        return True


def ROPOP():
    global i, tokenType
    if E():
        if ROPOPD():
            return True
        else:
            return False
    else:
        return False


def ROPOPD():
    global i, tokenType
    print("in ropopd", tokenType[i])
    # need to be check
    if tokenType[i] in ["compareOp", "compare"]:
        i = i + 1
        if E():
            if ROPOPD():
                return True
            else:
                return False
        else:
            return False
    else:
        return True


def E():
    global i, tokenType
    if T():
        if ED():
            return True
        else:
            return False
    else:
        return False


def ED():
    global i, tokenType
    if tokenType[i] == "PM":
        i = i + 1
        if T():
            if ED():
                return True
            else:
                return False
        else:
            return False
    else:
        return True


def T():
    global i, tokenType
    if F():
        if TD():
            return True
        else:
            return False
    else:
        return False


def TD():
    global i, tokenType
    if tokenType[i] == "MDM":
        i = i + 1
        if F():
            if TD():
                return True
            else:
                return False
        else:
            return False
    else:
        return True


def F():
    global i, tokenType
    if tokenType[i] == "openroundbrace":
        i = i + 1
        if Args():
            # return laiga

            if tokenType[i] == "closeroundbrace":
                i = i + 1
                # will return function rdt
                return True
            else:
                errorMesssage(i)
                return False
        else:
            return False
    elif tokenType[i] in {"intConst", "floatConst", "charConst", "stringConst", "boolConst"}:
        dt = tokenType[i]
        i = i + 1
        return True, dt
    elif tokenType[i] == "notOp":
        i = i+1
        check, dtOut = F()
        if check:
            # f will return dt
            return True, dtOut

    elif inc_dec():
        return True
    elif tokenType[i] == "opensquarebrace":
        i = i + 1
        if Args():
            if tokenType[i] == "closesquarebrace":
                i = i + 1
                # will return array dt
                return True
            else:
                errorMesssage(i)
                return False
        else:
            return False
    elif TRAS():
        return True
    else:
        return False


def int_var():
    global i, tokenType
    if tokenType[i] == "public":
        print("public match")
        i = i + 1
        if tokenType[i] == "static":
            i = i + 1
            if tokenType[i] == "final":
                i = i + 1
                if tokenType[i] == "dataType":
                    i = i + 1
                    if tokenType[i] == "identifier":
                        i = i + 1
                        if tokenType[i] == "equals":
                            i = i + 1
                            if Exp():
                                if tokenType[i] == "terminator":
                                    i = i + 1
                                    return True
                                else:
                                    errorMesssage(i)
                                    return False
                            else:
                                return False
                        else:
                            errorMesssage(i)
                            return False
                    else:
                        errorMesssage(i)
                        return False
                else:
                    errorMesssage(i)
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def int_B():
    global i, tokenType
    print("in interface b", tokenType[i])
    if abs_func_def():
        print("abs func match")
        if int_B():
            return True
        else:
            return False
    elif int_var():
        if int_B():
            return True
        else:
            return False
    else:
        return True


def idDash():
    global i, tokenType, multipleInterface
    if tokenType[i] == "comma":
        i = i + 1
        if tokenType[i] == "identifier":
            multipleInterface.append(tokenValue[i])
            i = i + 1
            if idDash():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return True


def int_INH():
    global i, tokenType,  extendingClass
    if tokenType[i] == "extends":
        i = i + 1
        if tokenType[i] == "identifier":
            extendingClass = tokenValue[i]
            i = i + 1
            if idDash():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return True


def enum_body():
    global i, tokenType, enumlist
    if tokenType[i] == "stringConst":
        enumlist.append(tokenValue[i])
        i = i + 1
        if mStringConst():
            return True
        else:
            return False
    else:
        return True


def NAMF():
    global i, tokenType, mainTableTypeMOD, isFinal
    if tokenType[i] == "final":
        isFinal = True
        mainTableTypeMOD = "final"
        i = i + 1
        return True
    return True


def enum_def():
    global i, tokenType, mainTableType, currentClass, mainTableTypeMOD, enumlist
    if tokenType[i] == "enum":
        mainTableType = "enum"
        i = i + 1
        if tokenType[i] == "identifier":
            currentClass = tokenValue[i]
            notExist = insertMainTable(
                currentClass, mainTableType, mainTableTypeMOD, extendingClass, multipleInterface)
            print(notExist, "the result")
            print('after insertion')
            i = i + 1
            if tokenType[i] == "opencurlybrace" and notExist:
                i = i + 1
                if enum_body():
                    print(enumlist)
                    success = insertenumconst(currentClass, enumlist)
                    if tokenType[i] == "closecurlybrace" and success:
                        currentClass = ''
                        mainTableType = ''
                        i = i + 1
                        return True
                    else:
                        if(not success):
                            print('attribute not inrted')
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                if notExist == False:
                    errorList.append(redeclarationError(currentClass))
                errorMesssage(i)
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def imp():
    global i, tokenType, multipleInterface

    if tokenType[i] == "implements":
        i = i + 1
        if tokenType[i] == "identifier":
            multipleInterface.append(tokenValue[i])
            i = i + 1
            if idDash():
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return True


def INH():
    global i, tokenType, extendingClass
    if tokenType[i] == "extends":
        i = i + 1
        if tokenType[i] == "identifier":
            extendingClass = tokenValue[i]
            i = i + 1
            if imp():
                return True
        else:
            errorMesssage(i)
            return False
    elif imp():
        return True
    else:
        return True


def AN(dataTy):
    global i, tokenType
    cons = ''
    if tokenType[i] == "opensquarebrace":
        i = i + 1
        if tokenType[i] == "closesquarebrace":
            i = i + 1
            cons = dataTy + "[]"
            return True, cons
        else:
            errorMesssage(i)
            return False
    else:
        return True, cons


def RDT():
    global i, tokenType
    dt = ''
    if tokenType[i] == "void":
        dt = 'void'
        i = i + 1
        return True, dt
    elif tokenType[i] == "dataType":
        dt = tokenValue[i]
        i = i + 1
        chker, rdddt = AN(dt)
        if chker:
            if(rdddt != ""):
                dt = rdddt
            return True, dt
    elif tokenType[i] == "identifier":
        # search type in ftable
        i = i + 1
        return True, dt
    else:
        return False, dt


def Dec():
    global i, tokenType, signature
    if tokenType[i] == "dataType":
        fdt = tokenValue[i]
        i = i + 1
        if tokenType[i] == "identifier":
            yid = tokenValue[i]
            # insertFunctionTable()
            i = i + 1
            chk, fadt = AN(fdt)
            if(fadt != ""):
                fdt = fadt
            if chk:
                signature.append(fdt)
                cheker = insertFunctionTable(yid, fdt, highestScope)
                if(cheker):
                    print('success append in fyncrion ----------------')
                print('appende from declaration -----------------')
                return True
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def obj():
    global i, tokenType
    if tokenType[i] == "identifier":
        fdt = tokenValue[i]
        i = i + 1
        if tokenType[i] == "identifier":
            signature.append(fdt)
            print("append from obj ----------------")
            i = i + 1
            return True
        else:
            errorMesssage(i)
            return False
    else:
        return False


def Dec_Obj():
    global i, tokenType
    if Dec():
        return True
    elif obj():
        return True
    else:
        return False


def PARAM1():
    global i, tokenType
    if tokenType[i] == "comma":
        i = i + 1
        if Dec_Obj():
            if PARAM1():
                return True
        else:
            return False
    else:
        return True


def PARAM():
    global i, tokenType
    if Dec():
        if PARAM1():
            return True
    elif obj():
        if PARAM1():
            return True
    else:
        return True


def func_def():
    global i, tokenType, currentClass, signature, accessMODvalue, isStatic, isAbstract, isFinal, createScope, highestScope, isFunc
    if tokenType[i] == "basic":
        i = i+1
        check, retdt = RDT()
        if check:
            if tokenType[i] == "def":
                i = i + 1
                if tokenType[i] == "identifier":
                    funcId = tokenValue[i]
                    i = i + 1
                    if tokenType[i] == "openroundbrace":
                        highestScope = createScope()
                        isFunc = True
                        i = i + 1
                        if PARAM():
                            if tokenType[i] == "closeroundbrace":

                                signature.append("->")
                                signature.append(retdt)
                                chk = insertAttribute(funcId, signature, accessMODvalue,
                                                      isStatic, isAbstract, isFinal, currentClass)
                                signature = []
                                i = i + 1
                                if tokenType[i] == "opencurlybrace" and chk == True:
                                    i = i + 1
                                    if MST():
                                        if tokenType[i] == "closecurlybrace":
                                            value = destroyScope()
                                            isFunc = False
                                            i = i + 1
                                            print("close curly truuu",
                                                  tokenType[i])
                                            return True
                                        else:
                                            errorMesssage(i)
                                            return False
                                    else:
                                        return False
                                else:
                                    if(chk == False):
                                        errorList.append(
                                            redeclarationError(currentClass))
                                        return False
                                    errorMesssage(i)
                                    return False
                            else:
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        errorMesssage(i)
                        return False
                else:
                    errorMesssage(i)
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            if check == False:
                print('type error')
            errorMesssage(i)
            return False
    else:
        return False


def construct_def():
    global i, tokenType, currentClass, signature, accessMODvalue, isStatic, isAbstract, isFinal, createScope, highestScope, isFunc
    if tokenType[i] == "def":
        i = i + 1
        if tokenType[i] == "identifier":
            if(tokenValue[i] != currentClass):
                print('constructor syntax error')
                errorMesssage(i)
                return False
            i = i + 1
            if tokenType[i] == "openroundbrace":
                print("-------SCOPE BEFORE-------", highestScope)
                highestScope = createScope()
                isFunc = True
                print("--------SCOPE AFTER---------", highestScope)
                i = i + 1
                if PARAM():
                    if tokenType[i] == "closeroundbrace":
                        signature.append("->")
                        chk = insertAttribute(currentClass, signature, accessMODvalue,
                                              isStatic, isAbstract, isFinal, currentClass)
                        signature = []
                        i = i + 1
                        if tokenType[i] == "opencurlybrace" and chk == True:
                            i = i + 1
                            if MST():
                                if tokenType[i] == "closecurlybrace":
                                    value = destroyScope()
                                    isFunc = False
                                    i = i + 1
                                    return True
                                else:
                                    errorMesssage(i)
                                    return False
                            else:
                                return False
                        else:
                            if(chk == False):
                                errorList.append(
                                    redeclarationError(currentClass))
                                return False
                            errorMesssage(i)
                            return False
                    else:
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def SST():
    global i, tokenType
    print("sst")
    if tokenType[i] == "while":
        if while_st():
            return True
        else:
            return False
    elif tokenType[i] == "for":
        if for_st():
            return True
        else:
            return False
    elif tokenType[i] == "switch":
        if switch_st():
            return True
        else:
            return False
    elif tokenType[i] == "if":
        if if_else_elif():
            return True
        else:
            return False
    elif tokenType[i] == "break":
        if break_st():
            return True
        else:
            return False
    elif tokenType[i] == "continue":
        if continue_st():
            return True
        else:
            return False
    elif tokenType[i] == "return":
        if return_st():
            return True
        else:
            return False
    elif tokenType[i] == "identifier":
        if Assign_st():
            print("assign truuuuuuuuu")
            return True
        else:
            return False
    elif (tokenType[i] in ['this', 'super']):
        if TAssign_st():
            return True
        else:
            return False
    elif Decl():
        return True
    elif tokenType[i] == "try":
        if try_catch_st():
            return True
        else:
            return False
    else:
        return False


def MST():
    global i, tokenType
    if SST():
        if MST():
            return True
        else:
            return False
    else:
        return True


def CB():
    global i, tokenType, accessMODvalue, isStatic, isFinal, isAbstract
    if Assign_st():
        if CB():
            return True
        else:
            return False
    elif TAssign_st():
        if CB():
            return True
        else:
            return False
    elif tokenType[i] == "public":
        accessMODvalue = "public"
        print('update to p :', accessMODvalue)
        i = i + 1
        if NAMS():
            print("static true")
            if NAMF():
                print("final true")
                if MVC():
                    print("mvc true")
                    clearAccesandNonAccess()
                    # false
                    if CB():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokenType[i] == "private":
        accessMODvalue = "private"
        i = i + 1
        if NAMS():
            print("static true")
            if NAMF():
                print("final true")
                if MVC():
                    print("mvc true")
                    clearAccesandNonAccess()
                    # false
                    if CB():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokenType[i] == "static":
        isStatic = True
        i = i + 1
        if NAMF():
            print("static true")
            if MVC():
                print("mvc true")
                clearAccesandNonAccess()
                # false
                if CB():
                    return True
                else:
                    return False
            else:
                return False
    elif tokenType[i] == "final":
        i = i + 1
        if MVC():
            print("mvc true")
            if CB():
                return True
            else:
                return False
        else:
            return False
    elif MVC():
        if CB():
            return True
        else:
            return False
    else:
        return True


def class_def():
    global i, tokenType, extendingClass, multipleInterface, mainTableTypeMOD, mainTableType, currentClass
    if NAMF():
        if tokenType[i] == "class":
            mainTableType = "class"
            i = i + 1
            if tokenType[i] == "identifier":
                currentClass = tokenValue[i]
                i = i + 1
                if INH():
                    notExist = insertMainTable(
                        currentClass, mainTableType, mainTableTypeMOD, extendingClass, multipleInterface)
                    print(notExist, "the result")
                    print('after insertion')
                    if tokenType[i] == "opencurlybrace" and notExist:
                        i = i + 1
                        if CB():
                            print("CB TRUE")
                            if tokenType[i] == "closecurlybrace":
                                currentClass = ""
                                extendingClass = ""
                                multipleInterface = []
                                mainTableTypeMOD = ""
                                mainTableType = ""
                                print("class curly")
                                i = i + 1
                                return True
                            else:
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        if(notExist == False):
                            theERROR = redeclarationError(currentClass)
                            errorList.append(theERROR)
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            return False
    else:
        return False


def interface_def():
    global i, tokenType, extendingClass, multipleInterface, mainTableTypeMOD, mainTableType, currentClass
    if tokenType[i] == "interface":
        mainTableType = "interface"
        i = i + 1
        if tokenType[i] == "identifier":
            currentClass = tokenValue[i]
            i = i + 1
            if int_INH():
                notExist = insertMainTable(
                    currentClass, mainTableType, mainTableTypeMOD, extendingClass, multipleInterface)
                print(notExist, "the result")
                if tokenType[i] == "opencurlybrace" and notExist:
                    i = i + 1
                    if int_B():
                        if tokenType[i] == "closecurlybrace":
                            currentClass = ""
                            extendingClass = ""
                            multipleInterface = []
                            mainTableTypeMOD = ""
                            mainTableType = ""
                            print("class curly interface")
                            i = i + 1
                            return True
                        else:
                            errorMesssage(i)
                            return False
                    else:
                        return False
                else:
                    if(notExist == False):
                        theERROR = redeclarationError(currentClass)
                        errorList.append(theERROR)
                    errorMesssage(i)
                    return False
            else:
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def abs_func_def():
    global i, tokenType
    if tokenType[i] == "abstract":
        print("BAS MATCH")
        i = i + 1
        if RDT():
            if tokenType[i] == "def":
                i = i + 1
                if tokenType[i] == "identifier":
                    i = i + 1
                    if tokenType[i] == "openroundbrace":
                        i = i + 1
                        if PARAM():
                            if tokenType[i] == "closeroundbrace":
                                i = i + 1
                                if tokenType[i] == "terminator":
                                    i = i + 1
                                    return True
                                else:
                                    errorMesssage(i)
                                    return False
                            else:
                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        errorMesssage(i)
                        return False
                else:
                    errorMesssage(i)
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def abs_B():
    global i, tokenType
    print("in abs")
    if Assign_st():
        if abs_B():
            return True
        else:
            return False
    elif TAssign_st():
        if abs_B():
            return True
        else:
            return False
    elif tokenType[i] == "public":
        i = i + 1
        if NAMS():
            print("static true")
            if NAMF():
                print("final true")
                if MVA():
                    print("mvc true")
                    if abs_B():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokenType[i] == "private":
        i = i + 1
        if NAMS():
            print("static true")
            if NAMF():
                print("final true")
                if MVA():
                    print("mvc true")
                    if abs_B():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif tokenType[i] == "static":
        i = i + 1
        if NAMF():
            print("static true")
            if MVA():
                print("mvc true")
                if abs_B():
                    return True
                else:
                    return False
            else:
                return False
    elif tokenType[i] == "final":
        i = i + 1
        if MVA():
            print("mvc true")
            if abs_B():
                return True
            else:
                return False
        else:
            return False
    elif MVA():
        if abs_B():
            return True
        else:
            return False
    else:
        return True


def abs_class_def():
    global i, tokenType, extendingClass, multipleInterface, mainTableTypeMOD, mainTableType, currentClass
    if tokenType[i] == "abstract":
        mainTableTypeMOD = "abstract"
        i = i + 1
        if tokenType[i] == "class":
            mainTableType = "class"
            i = i + 1
            if tokenType[i] == "identifier":
                currentClass = tokenValue[i]
                i = i + 1
                if INH():
                    notExist, extendsClass = insertMainTable(
                        currentClass, mainTableType, mainTableTypeMOD, extendingClass, multipleInterface)
                    print(notExist, "the result")
                    if tokenType[i] == "opencurlybrace" and notExist:
                        i = i + 1
                        if abs_B():
                            if tokenType[i] == "closecurlybrace":
                                currentClass = ""
                                extendingClass = ""
                                multipleInterface = []
                                mainTableTypeMOD = ""
                                mainTableType = ""
                                print("abstract class curly")
                                i = i + 1
                                return True
                            else:

                                errorMesssage(i)
                                return False
                        else:
                            return False
                    else:
                        if(notExist == False):
                            if(extendsClass != ""):
                                theERROR = redeclarationError(
                                    currentClass)
                                errorList.append(theERROR)
                            else:
                                theERROR = redeclarationError(
                                    currentClass)
                                errorList.append(theERROR)
                        errorMesssage(i)
                        return False
                else:
                    return False
            else:
                errorMesssage(i)
                return False
        else:
            errorMesssage(i)
            return False
    else:
        return False


def defs():
    global i, tokenType
    if class_def():
        print("norm")
        if defs():
            return True
    elif interface_def():
        print("int is true")
        if defs():
            return True
    elif abs_class_def():
        print("abs class")
        if defs():
            return True
    elif enum_def():
        if defs():
            return True
    else:
        return True


def NAM():
    global i, tokenType
    if tokenType[i] == "final":
        i = i + 1
        return True
    else:
        return True


def structure():
    global i, tokenType

    if defs():
        if tokenType[i] == "EOF":
            print("defs true")
            return True
        else:
            return False
    else:
        return False


def syntaxAnalyzer():
    if structure():
        return True
    else:
        return False


result = syntaxAnalyzer()

print('                           -------------BACK tracking Print Statement----------------------------------')
print('*****************************************************************************')
if(result and len(errorList) > 0):
    print('parsed unconditionaly!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')

if (result and len(errorList) == 0):
    print("                         >>>>>>>>>>>Parsed Successfully<<<<<<<<<<<<<")
elif(len(errorList) != 0):
    print("ERROR <>>>>>>>>>>>", errorList[0])
else:
    print("error in line :", calclateLineNo(i), allLines[i])
print('                             -------------------ERROR LIST------------------------------------------------')
print(errorList)
print('                              -------------------MAIN TABLE------------------------------------------------')
print("TOTAL OBJ REF <>>>>>>>> :", len(mainTable_))
for i in mainTable_:
    print("-----------------------CLASS NAME:", i.getName())
    print(vars(i), "the valus")
    for j in i.attrTable:
        print('attributes---')
        print(vars(j), "the valus")
print('                            -------------------function TABLE------------------------------------------------')
for i in functionTable_:
    print(vars(i), "the valus")
print('*****************************************************************************')
