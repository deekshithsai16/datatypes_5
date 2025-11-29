chart="learn"
print(chart[0:5:1])
print(chart[::]) #by default chart[0:5:1].

char="education"
print(char[6:10:2])	#to print "in".
print(char[3:6:1])	#to print "cat".


char="everyone doent have equal talent, but everyone have equal opportunity to develop your talent"
print(char[7::7])
print(char[4::4])
print(char[1:26:2])
print(char[5:8:1])
print(char[::])


char="empowering every student to turn technology into innovations"
print(char[49:51:1])
print(char[51:55:1])
print(char[37:39:1])
print(char[7:18:10])
print(char[33:37:1])


char=162712376
binary=char
print(bin(char))
bina="0b1001101100101100101100111000"
print(bina[26::1])
binar="0b1000"
print(int(binar,2))


ph_num='9381732559'
print(ph_num[4])
print(type(ph_num[4]))
print(int(ph_num[4]))
print(oct(int(ph_num[4])))
