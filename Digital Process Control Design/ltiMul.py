from scipy.signal.ltisys import TransferFunctionContinuous as TransFun
from numpy import polymul,polyadd
import scipy
from scipy.signal import lti

class TFMult(TransFun):
    def __neg__(self):
        return TFMult(-self.num,self.den)

    def __mul__(self,other):
        if type(other) in [int, float]:
            return TFMult(self.num * other, self.den)
        elif type(other) in [TransFun, TFMult]:
            numer = polymul(self.num, other.num)
            denom = polymul(self.den, other.den)
            return TFMult(numer, denom)

    def __div__(self,other):
        if type(other) in [int, float]:
            return TFMult(self.num,self.den*other)
        if type(other) in [TransFun, TFMult]:
            numer = polymul(self.num,other.den)
            denom = polymul(self.den,other.num)
            return TFMult(numer,denom)

    def __rdiv__(self,other):
        if type(other) in [int, float]:
            return TFMult(other*self.den,self.num)
        if type(other) in [TransFun, TFMult]:
            numer = polymul(self.den,other.num)
            denom = polymul(self.num,other.den)
            return TFMult(numer,denom)

    def __add__(self,other):
        if type(other) in [int, float]:
            return TFMult(polyadd(self.num,self.den*other),self.den)
        if type(other) in [TransFun, type(self)]:
            numer = polyadd(polymul(self.num,other.den),polymul(other.num,self.den))
            denom = polymul(self.den,other.den)
            return TFMult(numer,denom)

    def __sub__(self,other):
        if type(other) in [int, float]:
            return TFMult(polyadd(self.num,-self.den*other),self.den)
        if type(other) in [TransFun, type(self)]:
            numer = polyadd(polymul(self.num,other.den),-polymul(other.den,self.num))
            denom = polymul(self.den,other.den)
            return TFMult(numer,denom)

    def __rsub__(self,other):
        if type(other) in [int, float]:
            return TFMult(polyadd(-self.num,self.den*other),self.den)
        if type(other) in [TransFun, type(self)]:
            numer = polyadd(polymul(other.num,self.den),-polymul(self.den,other.num))
            denom = polymul(self.den,other.den)
            return TFMult(numer,denom)
    # sheer laziness: symmetric behaviour for commutative operators
    __rmul__ = __mul__
    __radd__ = __add__