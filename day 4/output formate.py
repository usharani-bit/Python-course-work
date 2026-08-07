Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # OUTPUT FORMATE
>>> a = 10
>>> b = 10.2
>>> c = 'codegnan'
>>> print(a,b,c)
10 10.2 codegnan
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 10.2 c= codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='')
a=10b=10.2c=codegnan
>>> print("a=",a,"b=",b,"c=",c,sep='/n')
a=/n10/nb=/n10.2/nc=/ncodegnan
>>> print("a=",a,"b=",b,"c=",c,sep = '\n')
a=
10
b=
10.2
c=
codegnan
>>> print("a=",a,"b=",b,"c=",c,sep = '\t')
a=	10	b=	10.2	c=	codegnan
>>> print("a=",a,"b=",b,"c=",c,sep = '\t',end= '\n\n')
a=	10	b=	10.2	c=	codegnan

>>> print("a=",a,"b=",b,"c=",c,sep = '\t',end= '@')
a=	10	b=	10.2	c=	codegnan@
