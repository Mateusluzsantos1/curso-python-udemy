a = 'A'
b = 'B'
c = 1.1

string = 'a ={0} b ={1} c={2:.2f} '.format(a, b , c)

formato = string.format(a,b,c)
print(formato)