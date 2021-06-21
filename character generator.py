import itertools as its
n=0
a=0
b=2
while a<b:
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz²&é'(-è_çà)=~1234567890°+ù*%µ!:;,?./§<>¹~#{[|`^@]}¤ń”“¢»ł@ßðđŋħłµþø→↓←ŧ¶€«æ "
    r = its.product(digits, repeat=int(n))
    name = f"password of {n}-digits"
    dic = open (name, "w")
    for i in r:
    	dic.write("".join(i))
    	dic.write("".join("\n"))
    dic.close()
    n=n+1