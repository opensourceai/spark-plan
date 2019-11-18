
# Python2与Python3常用语法区别
## print函数
Python 2中print是语句（statement），Python 3中print则变成了函数。在Python 3中调用print需要加上括号，
不加括号会报SyntaxError。Python 2.6与Python 2.7部分地支持这种形式的print语法。在Python 2.6与Python
2.7里面，以下三种形式是等价的：

	print "123"
	print ("123") #注意print后面有个空格
	print("123") #print()不能带有任何其它参数
	# 然而，Python 2.6实际已经支持新的print()语法：
	from __future__ import print_function
	print("123", "456", sep=', ')
	
## Unicode
Python 2有两种字符串类型：str和unicode，Python 3中的字符串默认就是Unicode，Python 3中的str相当于Python 2
中的unicode。在Python 2中，如果代码中包含非英文字符，需要在代码文件的最开始声明编码，如下：

	# -*- coding: utf-8 -*-
由于 Python3.X 源码文件默认使用utf-8编码，这就使得以下代码是合法的：

	>>> 你好 = 'hello'
	>>>print(你好)
	hello
Python 2.x：

	>>> str = "我爱北京天安门"
	>>> str
	'\xe6\x88\x91\xe7\x88\xb1\xe5\x8c\x97\xe4\xba\xac\xe5\xa4\xa9\xe5\xae\x89\xe9\x97\xa8'
	>>> str = u"我爱北京天安门"
	>>> str
	u'\u6211\u7231\u5317\u4eac\u5929\u5b89\u95e8'

Python 3.x：
	
	>>> str = "我爱北京天安门"
	>>> str
	'我爱北京天安门'
## 除法运算
Python中的除法较其它语言显得非常高端，有套很复杂的规则。Python中的除法有两个运算符，/和//。

首先来说/除法:在python 2.x中/除法就跟我们熟悉的大多数语言，比如Java啊C啊差不多，整数相除的结果是一个整数，
把小数部分完全忽略掉，浮点数除法会保留小数点的部分得到一个浮点数的结果。在python 3.x中/除法不再这么做了，
对于整数之间的相除，结果也会是浮点数。
Python 2.x：

	>>> 1 / 2
	>>> 1.0 / 2.0

Python 3.x：

	>>> 1/2

而对于//除法，这种除法叫做floor除法，会对除法的结果自动进行一个floor操作，在python 2.x和python 3.x
中是一致的。
Python 2.x/Python 3.x相同：

	>>> -1 // 2
	-1
## 异常处理
在 Python 3 中处理异常也轻微的改变了，在 Python 3 中我们现在使用 as 作为关键词。捕获异常的语法由 except exc, var 改为 except exc as var。使用语法except (exc1, exc2) as var可以同时捕获多种类别的异常。

Python 2.x：

	try:
	  1/0
	except ZeroDivisionError, e:
	  print str(e)
Python 3.x(此种方式python 2.x也可用，python 3.x必须带as)：

	try:
	  1/0
	except ZeroDivisionError as e:
	  print str(e)
## xrange
在 Python 2 中 xrange() 创建迭代对象的用法是非常流行的。比如： for 循环或者是列表/集合/字典推导式。
这个表现十分像生成器（比如。"惰性求值"）。但是这个 xrange-iterable 是无穷的，意味着你可以无限遍历。
由于它的惰性求值，如果你不得仅仅不遍历它一次，xrange() 函数 比 range() 更快（比如 for 循环）。
尽管如此，对比迭代一次，不建议你重复迭代多次，因为生成器每次都从头开始。在 Python 3 中，range() 
是像 xrange() 那样实现以至于一个专门的 xrange() 函数都不再存在（在 Python 3 中 xrange() 
会抛出命名异常）。简单来说就是：Python 2中有 range 和 xrange 两个方法。其区别在于，range返回一个list，
在被调用的时候即返回整个序列；xrange返回一个iterator，在每次循环中生成序列的下一个数字。
Python 3中不再支持 xrange 方法，Python 3中的 range 方法就相当于 Python 2中的 xrange 方法。 
## map、filter 和 reduce
这三个函数号称是函数式编程的代表。在 Python3.x 和 Python2.x 中也有了很大的差异。首先我们先简单的在 
Python2.x 的交互下输入 map 和 filter,看到它们两者的类型是 built-in function(内置函数)：

	>>> map
	<built-in function map>
	>>> filter
	<built-in function filter>
	>>>
	
但是在Python 3.x中它们却不是这个样子了：

	>>> map
	<class 'map'>
	>>> map(print,[1,2,3])
	<map object at 0x10d8bd400>
	>>> filter
	<class 'filter'>
	>>> filter(lambda x:x % 2 == 0, range(10))
	<filter object at 0x10d8bd3c8>
	>>>
首先它们从函数变成了类，其次，它们的返回结果也从当初的列表成了一个可迭代的对象, 我们尝试用 next 函数来进行手工迭代，
对于比较高端的 reduce 函数，它在 Python 3.x 中已经不属于 built-in 了，被挪到 functools 模块当中。
## raw_input()和input()
在python2.x中raw_input()和input( )，两个函数都存在，其中区别为：

raw_input()---将所有输入作为字符串看待，返回字符串类型

input()---只能接收"数字"的输入，在对待纯数字输入时具有自己的特性，它返回所输入的数字的类型（int, float ）

在python3.x中raw_input()和input( )进行了整合，去除了raw_input()，仅保留了input()函数，
其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
## 数据类型
Python3.x去除了long类型，现在只有一种整型——int，但它的行为就像Python2.x版本的long

新增了bytes类型，对应于2.X版本的八位串，定义一个bytes字面量的方法如下

	>>> b = b'china'
	>>> type(b)
	<type 'bytes'>
	str对象和bytes对象可以使用.encode() (str -> bytes) or .decode() (bytes -> str)方法相互转化。
	>>> s = b.decode()
	>>> s
	'china'
	>>> b1 = s.encode()
	>>> b1
	b'china'
	
dict的.keys()、.items 和.values()方法返回迭代器，而之前的iterkeys()等函数都被废弃。
同时去掉的还有 dict.has_key()，用 in替代它吧 。

原文链接：https://www.jb51.net/article/159848.htm