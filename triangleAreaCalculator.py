import math
class Fraction:
    '''represents fractions'''

    def __init__(self,num=0,denom=1):
        '''Fraction(num,denom) -> Fraction
        creates the fraction object representing num/denom Fraction(x)=x and Fraction()=0'''
        if denom == 0: # raise an error if the denominator is zero
            raise ZeroDivisionError
        if type(num)==int==type(denom):
            #Both the numerator and denominator are integers so we can just make a fraction normally
            gcd=math.gcd(num,denom)
            if num<0 and denom<0:
                self.num=-int(num/gcd)
                self.denom=-int(denom/gcd)
            else:
                self.num=int(num/gcd)
                self.denom=int(denom/gcd)
        elif type(num)==Fraction==type(denom):
            self.num=(num/denom).num
            self.denom=(num/denom).denom
        elif type(num)==Fraction and type(denom)==int:
            self.num=num.num
            self.denom=num.denom*denom
            if self.num<0 and self.denom<0:
                self.num=-self.num
                self.denom=-self.denom
            gcd=math.gcd(self.num,self.denom)
            self.num=self.num//gcd
            self.denom=self.denom//gcd
    def __str__(self):
        answer=""
        answer+=str(self.num)
        answer+="/"
        answer+=str(self.denom)
        return answer
    def __float__(self):
        return self.num/self.denom
    def __add__(self, target):
        #first we have to get common denominators
        gcd=math.gcd(self.denom,target.denom)
        lcm=int(self.denom*target.denom/gcd)
        #now we can just add
        return Fraction((self.num*lcm//self.denom)+(target.num*lcm//target.denom), lcm)
    def __sub__(self, target):
        #first we have to get common denominators
        gcd=math.gcd(self.denom,target.denom)
        lcm=int(self.denom*target.denom/gcd)
        #now we can just subtract
        return Fraction((self.num*lcm//self.denom)-(target.num*lcm//target.denom), lcm)
    def __mul__(self, target):
        #just multiply numerators and denominators because the __init__ takes care of lowest terms for us
        return(Fraction(self.num*target.num,self.denom*target.denom))
    def __truediv__(self,target):
        #just return self*(the reciprocal of target) because that's how division of two fractions works
        return(self*Fraction(target.denom,target.num))
    def __eq__(self,target):
        #first make sure lowest terms and we don't have numerator and denominator negative
        if self.num<0 and self.denom<0:
            self.num=-self.num
            self.denom=-self.denom
        gcd=math.gcd(self.num,self.denom)
        self.num=self.num//gcd
        self.denom=self.denom//gcd
        if target.num<0 and target.denom<0:
            target.num=-target.num
            target.denom=-target.denom
        gcd=math.gcd(target.num,target.denom)
        target.num=target.num//gcd
        target.denom=target.denom//gcd
        #now make sure that if only one of numerator or denominator is negative that the negative sign goes on the numerator.
        #We do this so we don't end up with the first fraction as 5/-6 and the second as -5/6 because if we had that it would say False while it should be true
        #So, we move all the negatives in the denominator into the numerator
        if self.denom<0:
            self.num=-self.num
            self.denom=-self.denom
        if target.denom<0:
            target.denom=-target.denom
            target.num=-target.num
        if self.num == target.num and self.denom==target.denom:
            return True
        else:
            return False
def triangle_area(s1, s2, s3):
    Semiperimeter= Fraction(s1+s2+s3)/Fraction(2)
    return "Square Root of "+str(Semiperimeter*(Semiperimeter-s1)*(Semiperimeter-s2)*(Semiperimeter-s3))
if __name__=="__main__":
    n1=int(input("Put in the first numerator"))
    d1=int(input("Put in the first denominator"))
    n2=int(input("Put in the second numerator"))
    d2=int(input("Put in the second denominator"))
    n3=int(input("Put in the third numerator"))
    d3=int(input("Put in the third denominator"))
    print(triangle_area(Fraction(n1,d1),Fraction(n2,d2),Fraction(n3,d3)))
