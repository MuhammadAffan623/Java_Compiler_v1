mainTable_ = []
functionTable_ = []
scopeStack_ = [0]
highestScope = 0
typeCompatibility = {
    "intint+": "int",
    "intint-": "int",
    "intint*": "int",
    "intint/": "int",
    "intint%": "int",
    "intint=": "int",
    "intint==": " bool",
    "intint!=": "bool",
    "intint<=": "bool",
    "intint<": "bool",
    "intint>": "bool",
    "intint>=": "bool",
    "intfloat+": "float",
    "intfloat-": "float",
    "intfloat*": "float",
    "intfloat/": "float",
    "intfloat=": "int",
    "intfloat==": "bool",
    "intfloat!=": "bool",
    "intfloat<=": "bool",
    "intfloat<": "bool",
    "intfloat>": "bool",
    "intfloat>=": "bool",
    "intchar+": "int",
    "intchar-": "int",
    "intchar*": "int",
    "intchar/": "int",
    "intchar%": "int",
    "intchar=": "int",
    "intchar==": "bool",
    "intchar!=": "bool",
    "intchar<=": "bool",
    "intchar<": "bool",
    "intchar>": "bool",
    "intchar>=": "bool",
    "intbool+": "int",
    "intbool-": "int",
    "intbool*": "int",
    "intbool/": "int",
    "intbool%": "int",
    "intbool=": "int",
    "intbool==": "bool",
    "intbool!=": "bool",
    "intbool<=": "bool",
    "intbool<": "bool",
    "intbool>": "bool",
    "intbool>=": "bool",
    "floatfloat+": "float",
    "floatfloat-": "float",
    "floatfloat*": "float",
    "floatfloat/": "float",
    "floatfloat=": "float",
    "floatint=": "float",
    "floatfloat==": "bool",
    "floatfloat!=": "bool",
    "floatfloat<=": "bool",
    "floatfloat<": "bool",
    "floatfloat>": "bool",
    "floatfloat>=": "bool",
    "floatchar+": "float",
    "floatchar-": "float",
    "floatchar*": "float",
    "floatchar/": "float",
    "floatchar%": "float",
    "floatchar=": "float",
    "floatchar==": "bool",
    "floatchar!=": "bool",
    "floatchar<=": "bool",
    "floatchar<": "bool",
    "floatchar>": "bool",
    "floatchar>=": "bool",
    "floatbool+": "float",
    "floatbool-": "float",
    "floatbool*": "float",
    "floatbool/": "float",
    "floatbool=": "bool",
    "floatbool==": "bool",
    "floatbool!=": "bool",
    "floatbool<=": "bool",
    "floatbool<": "bool",
    "floatbool>": "bool",
    "floatbool>=": "bool",
    "stringstring+": "string",
    "stringstring=": "string",
    "stringstring==": "bool",
    "stringstring!=": "bool",
    "stringstring<=": "bool",
    "stringstring<": "bool",
    "stringstring>": "bool",
    "stringstring>=": "bool",
    "stringint=": "int",
    "stringfloat=": "int",
    "stringchar+": "string",
    "stringchar=": "string",
    "stringbool=": "string",
    "charchar+": "int",
    "charchar-": "int",
    "charchar*": "int",
    "charchar/": "int",
    "charchar%": "int",
    "charchar=": "char",
    "charchar==": "bool",
    "charchar!=": "bool",
    "charchar<=": "bool",
    "charchar<": "bool",
    "charchar>": "bool",
    "charchar>=": "bool",
    "charint+": "char",
    "charint-": "char",
    "charint*": "char",
    "charint/": "char",
    "charint%": "int",
    "charint=": "char",
    "charint==": "bool",
    "charint!=": "bool",
    "charint<=": "bool",
    "charint<": "bool",
    "charint>": "bool",
    "charint>=": "bool",
    "charfloat+": "float",
    "charfloat-": "float",
    "charfloat*": "float",
    "charfloat/": "float",
    "charfloat=": "char",
    "charfloat==": "bool",
    "charfloat!=": "bool",
    "charfloat<=": "bool",
    "charfloat<": "bool",
    "charfloat>": "bool",
    "charfloat>=": "bool",
    "charstring+": "string",
    "charbool+": "int",
    "charbool-": "int",
    "charbool*": "int",
    "charbool/": "int",
    "charbool%": "int",
    "charbool=": "char",
    "charbool==": "bool",
    "charbool!=": "bool",
    "charbool<=": "bool",
    "charbool<": "bool",
    "charbool>": "bool",
    "charbool>=": "bool",
    "boolbool+": "bool",
    "boolbool-": "bool",
    "boolbool*": "bool",
    "boolbool/": "bool",
    "boolbool%": "bool",
    "boolbool=": "bool",
    "boolbool==": "bool",
    "boolbool!=": "bool",
    "boolbool<=": "bool",
    "boolbool<": "bool",
    "boolbool>": "bool",
    "boolbool>=": "bool",
    "boolbool&&": "bool",
    "boolbool||": "bool",
    "boolint+": "int",
    "boolint-": "int",
    "boolint*": "int",
    "boolint/": "int",
    "boolint%": "int",
    "boolint=": "bool",
    "boolint==": "bool",
    "boolint!=": "bool",
    "boolint<=": "bool",
    "boolint<": "bool",
    "boolint>": "bool",
    "boolint>=": "bool",
    "boolfloat-": "float",
    "boolfloat*": "float",
    "boolfloat/": "float",
    "boolfloat%": "float",
    "boolfloat=": "bool",
    "boolfloat==": "bool",
    "boolfloat!=": "bool",
    "boolfloat<=": "bool",
    "boolfloat<": "bool",
    "boolfloat>": "bool",
    "boolfloat>=": "bool",
    "boolchar+": "int",
    "boolchar-": "int",
    "boolchar*": "int",
    "boolchar/": "int",
    "boolchar%": "int",
    "boolchar=": "bool",
    "boolchar==": "bool",
    "boolchar!=": "bool",
    "boolchar<=": "bool",
    "boolchar<": "bool",
    "boolchar>": "bool",
    "boolchar>=": "bool",
    "char!": "bool",
    "int!": "bool",
    "int++": "int",
    "int--": "int",
    "float!": "bool",
    # "bool!": "bool",
    # "bool++": "bool",
    # "bool--": "bool",
    # "char++": "char",
    # "char--": "char",
    # "float++": "float",
    # "float--": "float"
}


class mainTable:
    def __init__(self, name, Type, typeMod, extends, implements):
        self.name = name
        self.type = Type
        self.typeMod = typeMod
        self.extends = extends
        self.implements = implements
        self.attrTable = []

    def getTypeMod(self):
        return self.typeMod

    def getName(self):
        return self.name


class attributeTable:
    def __init__(self, name, Type, accessMod, static, abstract, final):
        self.name = name
        self.type = Type
        self.accessMod = accessMod
        self.static = static
        self.abstract = abstract
        self.final = final


class functionTable:
    def __init__(self, name, Type, scope):
        self.name = name
        self.type = Type
        self.scope = scope


def lookupMainTable(name):
    x = next((j for j in mainTable_ if j.name == name), "")
    print("what is x", x)
    if x == "":
        return False
    # print("\tLookUp Main Table")
    # print(vars(x))
    return x


def insertenumconst(val, enumlist):
    for i in mainTable_:
        fname = i.getName()
        if fname == val:
            i.attrTable = enumlist
            return True
    return False


def insertMainTable(name, Type, typeMod, extends, implements):

    if lookupMainTable(name) == False:
        if extends != "" and lookupMainTable(extends) == False:
            print("------------cannot extends---------")
            return False, extends
        elif extends != "":
            for i in mainTable_:
                fname = i.getName()
                ftype = i.getTypeMod()
                if (fname == extends) and (ftype == "final"):
                    extends = ""
                    print("------------cannot extends bcz final---------")
                    return False, extends

        obj = mainTable(name, Type, typeMod, extends, implements)
        mainTable_.append(obj)
        # print("\tMain Table")
        # for t in mainTable_:
        #     print(vars(t))
        return True, extends
    return False, extends


def lookupAttributeTable(name, paramList, ofName):
    x = lookupMainTable(ofName)
    if x != False:
        if "->" not in paramList:
            y = next((j for j in x.attrTable if j.name == name), "")
            if y == "":
                return False
            # print("\tLookUp Attr Table")
            # print(vars(y))
            c = y.type
            print("[[[[[[[[[[[[[[[[[[[[[0", c)

            return c
        else:
            y = next(
                (j for j in x.attrTable if j.name == name and j.type == paramList), ""
            )
            if y == "":
                return False
            # print("\tLookUp Attr Table")
            # print(vars(y))
            c = y.type
            print("[[[[[[[[[[[[[[[[[[[[[0", c)
            return c
            # return y
    return False


def lookupAttributeForType(name, ofName):
    x = lookupMainTable(ofName)
    y = next((j for j in x.attrTable if j.name == name), "")
    if y == "":
        return False
    elif "->" not in y.type:
        return y.type
    else:
        return False


def insertAttribute(name, Type, accessMod, static, abstract, final, ofName):
    if lookupAttributeTable(name, Type, ofName) == False:
        for i in mainTable_:
            if i.name == ofName:
                obj = attributeTable(name, Type, accessMod, static, abstract, final)
                i.attrTable.append(obj)
                # print("\tAttr Table")
                # for t in i.attrTable:
                #     print(vars(t))
                return True
    return False


def lookupFunctionTable(name):
    for i in scopeStack_:
        x = next((j for j in functionTable_ if j.scope == i and j.name == name), "")
        if x != "":
            # print("\tLookUp Func Table")
            # print(vars(x))
            return x.type
    return False


def insertFunctionTable(name, Type, scope):
    if lookupFunctionTable(name) == False:
        obj = functionTable(name, Type, scope)
        functionTable_.append(obj)
        # print("\tFunction Table")
        # for t in functionTable_:
        #     print(vars(t))
        return True
    return False


def createScope():
    global highestScope
    highestScope += 1
    x = highestScope
    # print("createdScope:\t", x)
    # scopeStack_.insert(0, x)
    scopeStack_.append(x)
    return scopeStack_[-1]


def destroyScope():
    x = scopeStack_.pop()
    # print("destroyedScope:\t", x)
    return scopeStack_[-1]


def binTypeCompatible(left, right, op):
    check = left.strip() + right.strip() + op.strip()
    print("the check in cccc:", check)
    if check in typeCompatibility.keys():
        return typeCompatibility[check]
    # check = right.strip() + left.strip() + op.strip()
    # print("the check in cccc:", check)
    # if check in typeCompatibility.keys():
    #     return typeCompatibility[check]
    return False


def uniTypeCompatible(left, op):
    check = left + op
    if check in typeCompatibility.keys():
        return typeCompatibility[check]
    return False


def redeclarationError(sd):
    sms = (
        "!!!!!!!!!!  redeclaration error  : "
        + "'"
        + sd
        + "'"
        + " already exist !!!!!!!!!!!"
    )
    return sms


def declarationError(sd):
    sms = (
        "!!!!!!!!!!  Declaration error  : "
        + "'"
        + sd
        + "'"
        + " does not  exist !!!!!!!!!!!"
    )
    return sms


def ptypeError(parent):
    sms = "primitive type Error at " + parent
    return sms


def scopeError(parent):
    sms = "not access able in currrent scope" + parent
    return sms


def typeMISmatchError(left, right):
    sms = "TYPE MISMATCH ERROR OF   " + left + " AND   " + right
    return sms
