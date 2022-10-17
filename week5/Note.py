from string import Template
import sys

# 变量的赋值
# 内存驻留 interning in python (Optimization)
#   None
#   int (-5,256)
#   String（字符串长度为0或1；字符串大于1时，且字符串中只包含大小写字母，数字，下划线）

# 字符串只在编译时进行驻留，而非运行时
str1='sten'+'waves'  #编译
print(str1 is 'stenwaves')
str3='sten'
str4=str3+'waves'  #运行
print(str4 is 'stenwaves')  

# intern方法强制驻留
a="a*&&"
b="a*&&"
print(a is b)
c=sys.intern(b)
print(c is b)


x,*y = 99,88,77
print(y)  #注意是列表形式

x=99,88,77
print(x)  #注意是元组形式 （定义元组，主要是看它的元素是不是由逗号隔开，元组的括号可以省略）



# 格式化输出
# %，format()，f-strings（一般选择），String Template Class
x='looked'
print("Misha %s and %s around." % ('walked',x))
print("The value of pi is %5.4f" % 3.141592)  #A.B, A表示宽度，B表示精确位，如果宽度不够用空格填充，如果实际宽度大于A，忽略
print("Floating point numbers %1.0f" % 13.144)

print('{2} {1} {0}'.format('directions','the','Read'))
print('a:{a}, b:{b}, c:{c}'.format(a=1,b='Two',c=12.3))
print('The value of pi is {0:1.5f}'.format(3.141592))  # {[index]:[width][.precision][type]}

name='Ele'
print(f"My name is {name}")
print(f"He said his age is {(lambda x: x*2)(3)}")  
num=3.1415926535
print(f"The value of pi is: {num:{1}.{5}}")  # {value:{width}.{precision}}

n1='Hello'
n2='GeekforGeeks'
n=Template('$n3 ! This is $n4.')
print(n.substitute(n3=n1,n4=n2))



# 截取/切片字符串
s='Hello World!'
print(s[2:5]) # 左闭右开
print(s[2:])
print(s[-1:-5:-2])  # -2是步长



lst=['1','4','2','6','2']
s='-'
print(s.join(lst))