def damage(self,d,s,t):
    self.d = d
    self.s = s
    self.t = t

    if(t=="minute"):
        print(d*(s*60))
    elif(t=="hour"):
        print(d*s*60*60)
    else:
        print(d*s)

a=damage(40,5,"minute")
print(a)