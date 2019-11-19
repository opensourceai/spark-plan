作者：Qiang He  

邮箱：1422127065@qq.com  

**python高级用法之-迭代器、生成器、装饰器**

##### 1 .迭代器  
一般在python中可以使用for循环，对于像list，dict等都可以。但是他们称之为可迭代的对象，而不是迭代器。
迭代器同样可以使用for循环遍历，迭代器基于两个方法，iter()将其转化为迭代器，neext() 对迭代器取值，调用一次按排列顺序取一个值
使用迭代器的优势：不需要将所有数据一次性加载，而是用next()方法调用元素，不需要考虑内存的问题 

代码示例
```python
list = [1,5,6]
it=iter(list) #创建一个迭代器对象
print(it)   #output  1
print(it)   #output  2
```

##### 2 .生成器
生成器可理解为高级迭代器，在返回元素的代码更加简洁，更重要的是不在需要创建迭代器，在函数中使用yield，该函数就被成为生成器。
生成器是可以迭代的，但是只可以读取它一次。因为用的时候才生成 , 生(generator）能够迭代的关键是他有next()方法，工作原理就是通过重复调用next()方法，直到捕获一个异常, yield是一个类似return 的关键字，迭代一次遇到yield的时候就返回yield后面或者右面的值。而且下一次迭代的时候，从上一次迭代遇到的yield后面的代码开始执行 
**注意**的是生成器只能用于迭代操作

代码示例
```python
def fib(n):
    prev, curr = 0, 1
    while n > 0:
        n -= 1
        yield curr
        prev, curr = curr, curr + prev
res=fib(10)
for x in res:
    print(x)
#output
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55

```

##### 3. 装饰器
装饰器本质是一个Python函数，它可以让其它函数在没有任何代码变动的情况下增加额外功能 

代码示例
```python
#求和的函数
def add(func):
    def new_add(a,b):
        print("求和")
        func(a,b)
        print("结果是：{}".format(a + b))
        print("end")
    return new_add 
@add
def func(a,b):
    pass
if __name__ == '__main__':
    func(3,4)
#output
求和
结果是：7
end
```



#### 4. staticmethod和classmethod

代码示例
~~~python
class Test(object):

    def add(self,a,b):
        print("add:{}+{}={}".format(a,b,a+b))
    @classmethod #调用该方法的时候可以不需要实例化
    def minus(self, a, b):
        print("minus:{}+{}={}".format(a, b, a - b))
    @staticmethod #实例声明了静态方法 multiply，从而可以实现实例化使用 Test().multiply()，当然也可以不实例化调用该方法 Test().multiply()。
    def multiply(self, a, b):
        print("multiply:{}*{}={}".format(a, b, a * b))

Test().minus(3,2)

~~~

