replace_table = {
    "NI": "I",
    "IIII": "IV",
    "IVI": "V",
    "VIV": "IX",
    "IXI": "X",
}

class romannumeral:
    def __init__(self, val):
        self.val = val

    def increment(self):
        newval = self.val + "I"
        for rep, wi in replace_table.items():
            newval = newval.replace(rep, wi)
        return romannumeral(newval)

    def decrement(self):
        if self.val == "I":
            return romannumeral("N")
        newnum = romannumeral("I")
        lastnum = romannumeral("N")
        while newnum.val != self.val:
            newnum = newnum.increment()
            lastnum = lastnum.increment()
        return lastnum

    def __add__(self, numtoadd):
        ret = romannumeral(self.val)      
        while numtoadd.val != "N":
            ret = ret.increment()
            numtoadd = numtoadd.decrement()
        return ret

    def __str__(self):
        return self.val


v = romannumeral("X")
for i in range(5):
    v = v.decrement()
    print v

foo = romannumeral("V") + romannumeral("IV")
print foo