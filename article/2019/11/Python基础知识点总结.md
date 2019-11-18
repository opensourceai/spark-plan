# Python基础知识点总结
### Python标识符
在 Python 里，标识符有字母、数字、下划线组成。

在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。

Python 中的标识符是区分大小写的。

以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
以双下划线开头的 __foo 代表类的私有成员；以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
### Python有五个标准的数据类型
Numbers（数字）

String（字符串）

List（列表）

Tuple（元组）

Dictionary（字典）
### Python支持四种不同的数字类型
int（有符号整型）

long（长整型[也可以代表八进制和十六进制]）

float（浮点型）

complex（复数）
### python的字串列表有2种取值顺序
从左到右索引默认0开始的，最大范围是字符串长度少1

从右到左索引默认-1开始的，最大范围是字符串开头
### List（列表） 是 Python 中使用最频繁的数据类型
列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。

列表用 [ ] 标识，是 python 最通用的复合数据类型。

列表中值的切割也可以用到变量 [头下标:尾下标] ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾

加号 + 是列表连接运算符，星号 * 是重复操作。
### 元组是另一个数据类型，类似于List（列表）
元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
### 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型
列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
### Python数据类型转换
有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。

以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

	int(x [,base])--将x转换为一个整数
	long(x [,base] )--将x转换为一个长整数
	float(x)--将x转换到一个浮点数
	complex(real [,imag])--创建一个复数
	str(x)--将对象 x 转换为字符串
	repr(x)--将对象 x 转换为表达式字符串
	eval(str)--用来计算在字符串中的有效Python表达式,并返回一个对象
	tuple(s)--将序列 s 转换为一个元组
	list(s)--将序列 s 转换为一个列表
	set(s)--转换为可变集合
	dict(d)--创建一个字典。d 必须是一个序列 (key,value)元组。
	frozenset(s)--转换为不可变集合
	chr(x)--将一个整数转换为一个字符
	unichr(x)--将一个整数转换为Unicode字符
	ord(x)--将一个字符转换为它的整数值
	hex(x)--将一个整数转换为一个十六进制字符串
	oct(x)--将一个整数转换为一个八进制字符串
### Python元组
Python的元组(tuple)与列表类似，不同之处在于元组的元素不能修改。

元组使用小括号，列表使用方括号。

元组内置函数：

Python元组包含了以下内置函数

	cmp(tuple1, tuple2)比较两个元组元素。
	len(tuple)计算元组元素个数。
	max(tuple)返回元组中元素最大值。
	min(tuple)返回元组中元素最小值。
	tuple(seq)将列表转换为元组。
### Python字典（dictionary）

字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中

字典内置函数及方法：

Python字典包含了以下内置函数：

	cmp(dict1, dict2)  比较两个字典元素。
	len(dict)  计算字典元素个数，即键的总数。
	str(dict)  输出字典可打印的字符串表示。
	type(variable)  返回输入的变量类型，如果变量是字典就返回字典类型。

Python字典包含了以下内置方法：

	dict.clear()删除字典内所有元素
	dict.copy()返回一个字典的浅复制
	dict.fromkeys(seq[, val]))创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
	dict.get(key, default=None)返回指定键的值，如果值不在字典中返回default值
	dict.has_key(key)如果键在字典dict里返回true，否则返回false
	dict.items()以列表返回可遍历的(键, 值) 元组数组
	dict.keys()以列表返回一个字典所有的键
	dict.setdefault(key, default=None)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
	dict.update(dict2)把字典dict2的键/值对更新到dict里
	dict.values()以列表返回字典中的所有值
	pop(key[,default])删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
	popitem()随机返回并删除字典中的一对键和值。
### 匿名函数lambda
python 使用 lambda 来创建匿名函数。

lambda只是一个表达式，函数体比def简单很多。

lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。

lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。

虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
如：

	sum =lambda arg1, arg2: arg1 + arg2;print"相加后的值为 : ", sum(10,20) //输出30
### Python 循环语句
Python提供了for循环和while循环（在Python中没有do..while循环）:

	while 循环在给定的判断条件为 true 时执行循环体，否则退出循环体。
	for 循环重复执行语句
	嵌套循环你可以在while循环体中嵌套for循环
	循环控制语句可以更改语句执行的顺序。Python支持以下循环控制语句：
	break 语句在语句块执行过程中终止循环，并且跳出整个循环
	continue 语句在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环。
	pass 语句pass是空语句，是为了保持程序结构的完整性。
### python import语句
From...import语句

Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：

	from modname import name1[, name2[, ... nameN]]
例如，要导入模块 fib 的 fibonacci 函数，使用如下语句：

	from fib import fibonacci
这个声明不会把整个 fib 模块导入到当前的命名空间中，它只会将 fib 里的 fibonacci 单个引入到执行这个声明的模块的全局符号表。
From...import*语句

把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

	from modname import *
这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。
例如我们想一次性引入 math 模块中所有的东西，语句如下：

	from math import*
	
### Python字符串
Python转义字符

在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。

如下表：

\(在行尾时)续行符

\\反斜杠符号

\'单引号

\"双引号

\a响铃

\b退格(Backspace)

\e转义

\000空

\n换行

\v纵向制表符

\t横向制表符

\r回车

\f换页

\oyy八进制数，yy代表的字符，例如：\o12代表换行

\xyy十六进制数，yy代表的字符，例如：\x0a代表换行

\other其它的字符以普通格式输出

### Python字符串运算符

下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"


+字符串连接

	>>>a + b'HelloPython'
*重复输出字符串

	>>>a * 2'HelloHello'
[]通过索引获取字符串中字符

	>>>a[1]'e'
[ : ]截取字符串中的一部分

	>>>a[1:4]'ell'

in成员运算符 - 如果字符串中包含给定的字符返回 True

	>>>"H"inaTrue
not in成员运算符 - 如果字符串中不包含给定的字符返回 True

	>>>"M"notinaTrue
r/R原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。

	>>>printr'\n' \n >>> printR'\n' \n

### Python字符串格式化
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。

在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。

如下实例：

	#!/usr/bin/pythonprint "My name is %s and weight is %d kg!" % ('Zara', 21)

以上实例输出结果：

	My name is Zara and weight is 21 kg!
python字符串格式化符号：

	%c 格式化字符及其ASCII码
	%s 格式化字符串
	%d 格式化整数
	%u 格式化无符号整型
	%o 格式化无符号八进制数
	%x 格式化无符号十六进制数
	%X 格式化无符号十六进制数（大写）
	%f 格式化浮点数字，可指定小数点后的精度
	%e 用科学计数法格式化浮点数
	%E 作用同%e，用科学计数法格式化浮点数
	%g %f和%e的简写
	%G %f 和 %E 的简写
	%p 用十六进制数格式化变量的地址
	
原文链接：http://baijiahao.baidu.com/s?id=1599767502424567293&wfr=spider&for=pc