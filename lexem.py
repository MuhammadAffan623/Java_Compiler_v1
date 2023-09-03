from ast import operator
from operator import truediv
import re
import os.path
from tkinter import FALSE

# For Identifiers
def identifier(txt):
    identifier = "(([A-Z]|[a-z]|_)+[0-9]*)+"
    result = re.match(identifier, txt)
    if result:
        return True
    else:
        return False


def Integerss(txt):
    # For Integer
    integerss = "([+]|[-])?[0-9]+$"
    result = re.match(integerss, txt)
    if result:
        return True
    else:
        return False


def floatt(txt):
    floatt = "([+]|[-])?([1]|[2]|[3]|[4]|[5]|[6]|[7]|[8]|[9]|[0])*[.]([1]|[2]|[3]|[4]|[5]|[6]|[7]|[8]|[9]|[0])+$"
    result = re.match(floatt, txt)
    if result:
        return True
    else:
        return False


def charachter(txt):
    a = ["\\", "t", "'", '"', "n", "r", "f"]
    if (txt[0] == "'") & (txt[-1] == "'"):
        if ((len(txt) == 4) & (txt[1] == "\\") & (txt[2] in a)) | (len(txt) == 3):
            return True
        else:
            return False
    else:
        return False


def stringg(txt):
    stringg = '^"(.)*"$'
    result = re.match(stringg, txt)
    if result:
        return True
    else:
        return False


def checker(txt, ln, txtcheck):
    if ("." in txt) & (txtcheck == False):
        cou = txt.count(".")
        sep = txt.split(".")
        dots = []
        for i in range(cou):
            dots.append(".")
        for i in range(cou + 1):
            if identifier(sep[i]):
                if (i > 0) & (dots[i - 1] == "."):
                    tokenlist.append(("dot", ".", ln))
                    dots[i - 1] = ""
                if sep[i] in keywords:
                    tokenlist.append((keywords[sep[i]], sep[i], ln))
                else:
                    tokenlist.append(("identifier", sep[i], ln))
                sep[i] = ""
            elif i < cou:
                if Integerss(sep[i]):
                    if floatt(sep[i] + "." + sep[i + 1]):
                        tokenlist.append(("floatConst", sep[i] + "." + sep[i + 1], ln))
                        dots[i] = ""
                        sep[i] = ""
                        sep[i + 1] = ""
                    else:
                        tokenlist.append(("lexeme error", sep[i] + ".", ln))
                        sep[i] = ""
                        dots[i] = ""
            if i > 0:
                if (floatt(sep[i - 1] + "." + sep[i])) & (dots[i - 1] == "."):
                    tokenlist.append(("floatConst", sep[i - 1] + "." + sep[i], ln))
                    dots[i - 1] = ""
                    sep[i] = ""
                    sep[i - 1] = ""
            if Integerss(sep[i]):
                if i == cou:
                    tokenlist.append(("intConst", sep[i], ln))
                    sep[i] = ""
                else:
                    if i != 0:
                        if dots[i - 1] == ".":
                            tokenlist.append((".", ".", ln))
                            dots[i - 1] = ""
                    tokenlist.append(("lexeme error", sep[i], ln))
                    tokenlist.append((".", ".", ln))
                    dots[i] = ""
                    sep[i] = ""
            elif sep[i] != "":
                if i == (cou - 1):
                    tokenlist.append(("lexeme error", sep[i], ln))
                    sep[i] = ""
                    if dots[i] == ".":
                        dots[i] = ""
                        tokenlist.append((".", ".", ln))
                elif i > 0:
                    if dots[i - 1] == ".":
                        dots[i - 1] = ""
                        tokenlist.append((".", ".", ln))
                    tokenlist.append(("lexeme error", sep[i], ln))
                    sep[i] = ""

    elif txt in keywords:
        tokenlist.append((keywords[txt], txt, ln))
    elif stringg(txt):
        tmp = txt[1:-1]
        tokenlist.append(("stringConst", tmp, ln))
    elif charachter(txt):
        tmp = txt[1:-1]
        tokenlist.append(("charConst", txt, ln))
    elif floatt(txt):
        tokenlist.append(("floatConst", txt, ln))
    elif Integerss(txt):
        tokenlist.append(("intConst", txt, ln))
    elif identifier(txt):
        tokenlist.append(("identifier", txt, ln))
    else:
        tokenlist.append(("lexeme error", txt, ln))


def strcharchecker(typ, invcomopen, done, tempp, c, line, slash, check):
    if (invcomopen == False) & (len(tempp) > 0):
        checker(tempp, ln, False)
        tempp = ""
    done = False
    invcomopen = True
    tempp += line[c]
    c += 1
    if c < len(line):
        while line[c] != typ:
            if c < (len(line) - 1):
                if (line[c] == "\\") & (line[c + 1] == typ):
                    tempp += typ
                    c += 2
                elif line[c] == "\\":
                    if line[c + 1] in slash:
                        tempp += slash[line[c + 1]]
                        c += 2
                    else:
                        c += 1
                        tempp += line[c]
                        c += 1
                else:
                    tempp += line[c]
                    c += 1
            if (c >= len(line) - 1) & (invcomopen):
                break
    if c <= (len(line) - 1):
        if line[c] == typ:
            tempp += line[c]
            done = True
            invcomopen = False
            if check:
                checker(tempp, ln, True)
            tempp = ""
            c += 1
    return invcomopen, done, tempp, c


tokenlist = []
keywords = {
    "public": "public",
    "private": "private",
    "abstract": "abstract",
    "basic": "basic",
    "char": "dataType",
    "int": "dataType",
    "bool": "dataType",
    "String": "string",
    "double": "dataType",
    "float": "dataType",
    "def": "def",
    "class": "class",
    "True": "boolConst",
    "False": "boolConst",
    "return": "return",
    "enum": "enum",
    "void": "void",
    "extends": "extends",
    "implements": "implements",
    "interface": "interface",
    "default": "default",
    "this": "this",
    "super": "super",
    "not": "notOp",
    "and": "logicOp",
    "or": "logicOp",
    "if": "if",
    "elif": "elif",
    "for": "for",
    "while": "while",
    "continue": "continue",
    "break": "break",
    "else": "else",
    "new": "new",
    "break": "break",
    "switch": "switch",
    "case": "case",
    "final": "final",
    "throw": "throw",
    "finally": "finally",
    "static": "static",
    "try": "try",
    "catch": "catch",
    "Exception": "Exception",
}
wordbreakers = {
    ":": "colon",
    ";": "terminator",
    ",": "comma",
    "(": "openroundbrace",
    ")": "closeroundbrace",
    "[": "opensquarebrace",
    "]": "closesquarebrace",
    "{": "opencurlybrace",
    "}": "closecurlybrace",
}
operators = {
    "+": "PM",
    "=": "equals",
    "-": "PM",
    "*": "MDM",
    "/": "MDM",
    "%": "MDM",
    ">": "compareOp",
    "<": "compareOp",
    "!": "notOp",
    "&": "AND",
    "|": "OR",
}
doubleoperators = {
    # && and || dekhna
    "*=": "assignSelf",
    "/=": "assignSelf",
    "%=": "assignSelf",
    "!=": "compareOp",
    "++": "incDec",
    "--": "incDec",
    ">=": "compareOp",
    "==": "compareOp",
    "<=": "compareOp",
    "+=": "assignSelf",
    "-=": "assignSelf",
}
slash = {"n": "\n", "t": "\t"}
f = open("myfile.txt")
invcomopen = False
hash = False
tempp = ""
ln = 0
done = False
dotcheck = False
for line in f:
    ln += 1
    c = 0
    typ = "'"
    while c < len(line):
        if ((line[c] == '"') | (line[c] == "'")) & (hash == False):
            if (line[c] == '"') & (invcomopen == False):
                typ = '"'
            elif (line[c] == "'") & (invcomopen == False):
                typ = "'"
            invcomopen, done, tempp, c = strcharchecker(
                typ, invcomopen, done, tempp, c, line, slash, True
            )
            incomopen = False
        elif ((line[c] == "#") & (hash == False) & (invcomopen == False)) | (
            hash == True
        ):
            hash, done, tempp, c = strcharchecker(
                "#", hash, done, tempp, c, line, slash, False
            )
        elif line[c] in operators:
            if len(tempp) > 0:
                checker(tempp, ln, False)
                tempp = ""
            if c < len(line) - 1:
                t = line[c] + line[c + 1]
                if t in doubleoperators:
                    tokenlist.append((doubleoperators[t], t, ln))
                    c += 2
                else:
                    tokenlist.append((operators[line[c]], line[c], ln))
                    c += 1
            else:
                tokenlist.append((operators[line[c]], line[c], ln))
                c += 1
        elif (line[c] == "\n") | (line[c] == "\t") | (line[c] == " "):
            if len(tempp) > 0:
                checker(tempp, ln, False)
                tempp = ""
            c += 1
        elif line[c] in wordbreakers:
            if len(tempp) > 0:
                checker(tempp, ln, False)
                tempp = ""
            tokenlist.append((wordbreakers[line[c]], line[c], ln))
            c += 1
        else:
            tempp += line[c]
            c += 1
        if c >= len(line):
            if (line[len(line) - 1] != "\n") & (len(tempp) > 0):
                checker(tempp, ln, False)
                tempp = ""
            break  
print(tokenlist[0])
k = open("result.txt", "w")
k.write(
    str(tokenlist[0][0])
    + ", "
    + str(tokenlist[0][1])
    + ", "
    + str(tokenlist[0][2])
    + "\n"
)
k.close()
k = open("result.txt", "a")
for i in range(1, len(tokenlist)):
    # print(tokenlist[i])
    k.write(
        str(tokenlist[i][0])
        + ", "
        + str(tokenlist[i][1])
        + ", "
        + str(tokenlist[i][2])
        + "\n"
    )
k.close()
