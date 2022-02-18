import itertools as its 
digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz²&é'(-è_çà)=~1234567890°+ù*%µ!:;,?./§<>¹~#{[|`^@]}¤ń”“¢»ł@ßðđŋħłµþø→↓←ŧ¶€«æ "
r = its.product(digits, repeat=int(input("how many digits? \n->") ))
name = f"passwords"
dic = open(name, "w")
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()
