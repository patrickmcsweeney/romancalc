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
    
    def __sub__(self, numtosub):
        ret = romannumeral(self.val)
        while numtosub.val != "N":
            ret = ret.decrement()
            numtosub = numtosub.decrement()
            if ret.val == "N":
                raise Overflow("No negative numbers")

                

        return ret


    def __str__(self):
        return self.val

    def __lt__(self, other):
        if self == other:
            return False
        n1 = romannumeral("N")
        n2 = romannumeral("N")
        while (n1.val != self.val and n2.val != other.val):
            n1 = n1.increment()
            n2 = n2.increment()
        if n1.val == self.val:
            return True
        return False

    def __eq__(self, other):
        return self.val == other.val
    def __ne__(self, other):
        return self<other or other<self
    def __gt__(self, other):
        return other<self
    def __ge__(self, other):
        return not self<other
    def __le__(self, other):
        return not other<self

    def __mul__(self, other):
        newnum = romannumeral("N")
        counter = romannumeral("N")
        while counter < other:
            newnum += self
            counter += romannumeral("I")
        return newnum

    def __div__(self, other):
        newnum = romannumeral("N")
        counter = romannumeral("N")
        while newnum < self:
            newnum += other
            counter += romannumeral("I")
        if newnum != self:
            return counter - romannumeral("I")
        return counter

    def __mod__(self, other):
        newnum = romannumeral("N")
        counter = romannumeral("N")
        while newnum < self:
            newnum += other
            counter += romannumeral("I")
        if newnum == self:
            return romannumeral("N")
        else:
            return  other - (newnum - self)
        

class Overflow(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

foo = romannumeral("V") + romannumeral("IV")
print foo
foo = romannumeral("V") - romannumeral("IV")
print foo
try:
    foo = romannumeral("V") - romannumeral("VI")
except Overflow:
    print "No negative numbers " + str(foo)

print romannumeral("II") * romannumeral("II")
print romannumeral("X") / romannumeral("III")
print romannumeral("X") / romannumeral("II")
print romannumeral("X") % romannumeral("III")
print romannumeral("X") % romannumeral("II")
