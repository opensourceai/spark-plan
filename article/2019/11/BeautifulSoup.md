 

 

# 一、关于Beautiful Soup

Beautiful Soup是一个Python库，旨在用于快速的周转项目，例如屏幕抓取。三个功能使其强大：

 

Beautiful Soup提供了一些用于导航，搜索和修改解析树的简单方法和Pythonic习惯用法：用于剖析文档并提取所需内容的工具箱。编写应用程序不需要太多代码

Beautiful Soup会自动将传入文档转换为Unicode，将传出文档转换为UTF-8。您不必考虑编码，除非文档未指定编码并且Beautiful Soup无法检测到编码。然后，您只需要指定原始编码即可。

Beautiful Soup它位于HTML或XML解析器之上，使您可以尝试不同的解析策略或提高灵活性。

Beautiful Soup会解析您提供的任何内容，并为您进行树遍历。您可以告诉它“查找所有链接”，或“查找类externalLink的所有链接”，或“查找其URL与“ foo.com”匹配的所有链接，或“查找具有粗体文本的表标题，然后输入那是我的文字。”

 

曾经被锁定在设计不当的网站中的宝贵数据现在已经可以触及。使用Beautiful Soup，本来需要数小时才能完成的项目只需几分钟。

# 一、下载Beautiful Soup

当前版本是Beautiful Soup 4.8.1（2019年10月6日）。

 

1、如果你用的是新版的Debain或ubuntu,那么可以通过系统的软件包管理来安装:

$ `apt-get install Python-bs4`

2、如果你无法使用系统包管理安装,那么也可以通过 easy_install或 pip 来安装.包的名字是 beautifulsoup4 ,这个包兼容Python2和Python3.

$`easy_install beautifulsoup4`

$`pip install beautifulsoup4`

3、如果你没有安装 easy_install 或 pip ,那你也可以 [下载BS4的源码](http://www.crummy.com/software/BeautifulSoup/download/4.x/) ,然后通过setup.py来安装.

 

$ `Python setup.py install`

 

4、如果上述安装方法都行不通,Beautiful Soup的发布协议允许你将BS4的代码打包在你的项目中,这样无须安装即可使用.

作者在Python2.7和Python3.2的版本下开发Beautiful Soup, 理论上Beautiful Soup应该在所有当前的Python版本中正常工作

# 三、安装完成后的问题

Beautiful Soup发布时打包成Python2版本的代码,在Python3环境下安装时,会自动转换成Python3的代码,如果没有一个安装的过程,那么代码就不会被转换.

1、如果代码抛出了 ImportError 的异常: “No module named HTMLParser”, 这是因为你在Python3版本中执行Python2版本的代码.

2、如果代码抛出了 ImportError 的异常: “No module named html.parser”, 这是因为你在Python2版本中执行Python3版本的代码.

如果遇到上述2种情况,最好的解决方法是重新安装BeautifulSoup4.

3、如果在ROOT_TAG_NAME = u’[document]’代码处遇到 SyntaxError “Invalid syntax”错误,需要将把BS4的Python代码版本从Python2转换到Python3. 可以重新安装BS4:

`$ Python3 setup.py install`

或在bs4的目录中执行Python代码版本转换脚本

`$ 2to3-3.2 -w bs4`

# 四、安装解析器

Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器,其中一个是 [lxml](http://lxml.de/) .根据操作系统不同,可以选择下列方法来安装lxml:

`$ apt-get install Python-lxml`

`$ easy_install lxml`

`$ pip install lxml`

另一个可供选择的解析器是纯Python实现的 [html5lib](http://code.google.com/p/html5lib/) , html5lib的解析方式与浏览器相同,可以选择下列方法来安装html5lib:

`$ apt-get install Python-html5lib`

`$ easy_install html5lib`

`$ pip install html5lib`

下表列出了主要的解析器,以及它们的优缺点:

| **解析器**       | **使用方法**                                                 | **优势**                                                     | **劣势**                                               |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------ |
| Python标准库     | BeautifulSoup(markup,` `"html.parser")                       | ·      Python的内置标准库  ·      执行速度适中  ·      文档容错能力强 | ·      Python 2.7.3 or 3.2.2)前 的版本中文档容错能力差 |
| lxml HTML 解析器 | BeautifulSoup(markup,` `"lxml")                              | ·      速度快  ·      文档容错能力强                         | ·      需要安装C语言库                                 |
| lxml XML 解析器  | BeautifulSoup(markup,` `["lxml-xml"])  BeautifulSoup(markup,` `"xml") | ·      速度快  ·      唯一支持XML的解析器                    | ·      需要安装C语言库                                 |
| html5lib         | BeautifulSoup(markup,` `"html5lib")                          | ·      最好的容错性  ·      以浏览器的方式解析文档  ·      生成HTML5格式的文档 | ·      速度慢  ·      不依赖外部扩展                   |

推荐使用lxml作为解析器,因为效率更高. 在Python2.7.3之前的版本和Python3中3.2.2之前的版本,必须安装lxml或html5lib, 因为那些Python版本的标准库中内置的HTML解析方法不够稳定.

提示: 如果一段HTML或XML文档格式不正确的话,那么在不同的解析器中返回的结果可能是不一样的,查看 [解析器之间的区别](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id53) 了解更多细节

# 五、如何使用

将一段文档传入BeautifulSoup 的构造方法,就能得到一个文档的对象, 可以传入一段字符串或一个文件句柄.

```
from bs4 import BeautifulSoup
 
soup = BeautifulSoup(open("index.html"))
 
soup = BeautifulSoup("<html>data</html>")
```

首先,文档被转换成Unicode,并且HTML的实例都被转换成Unicode编码

```
BeautifulSoup("Sacr&eacute; bleu!")
<html><head></head><body>Sacré bleu!</body></html>
```

然后,Beautiful Soup选择最合适的解析器来解析这段文档,如果手动指定解析器那么Beautiful Soup会选择指定的解析器来解析文档.(参考 [解析成XML](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#xml) ).

# 六、对象的种类

Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种: Tag , NavigableString , BeautifulSoup , Comment .

## 1、Tag

Tag 对象与XML或HTML原生文档中的tag相同:

```
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
type(tag)
# <class 'bs4.element.Tag'>
```

Tag有很多方法和属性,在 [遍历文档树](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id18) 和 [搜索文档树](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id27) 中有详细解释.现在介绍一下tag中最重要的属性: name和attributes

### （1）、Name

每个tag都有自己的名字,通过 .name 来获取:

```
tag.name
# u'b'
```

如果改变了tag的name,那将影响所有通过当前Beautiful Soup对象生成的HTML文档:

```
tag.name = "blockquote"
tag
# <blockquote class="boldest">Extremely bold</blockquote>
```

### （2）、Attributes

一个tag可能有很多个属性. tag <b` `class="boldest"> 有一个 “class” 的属性,值为 “boldest” . tag的属性的操作方法与字典相同:

```
tag['class']
# u'boldest'
```

也可以直接”点”取属性, 比如: .attrs :

```
tag.attrs
# {u'class': u'boldest'}
```

tag的属性可以被添加,删除或修改. 再说一次, tag的属性操作方法与字典一样

```
tag['class'] = 'verybold'
tag['id'] = 1
tag
# <blockquote class="verybold" id="1">Extremely bold</blockquote>
 
del tag['class']
del tag['id']
tag
# <blockquote>Extremely bold</blockquote>
 
tag['class']
# KeyError: 'class'
print(tag.get('class'))
# None
```

### （3）、多值属性

HTML 4定义了一系列可以包含多个值的属性.在HTML5中移除了一些,却增加更多.最常见的多值的属性是 class (一个tag可以有多个CSS的class). 还有一些属性 rel , rev , accept-charset , headers , accesskey . 在Beautiful Soup中多值属性的返回类型是list:

```
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.p['class']
# ["body", "strikeout"]
 
css_soup = BeautifulSoup('<p class="body"></p>')
css_soup.p['class']
# ["body"]
```

如果某个属性看起来好像有多个值,但在任何版本的HTML定义中都没有被定义为多值属性,那么Beautiful Soup会将这个属性作为字符串返回

```
id_soup = BeautifulSoup('<p id="my id"></p>')
id_soup.p['id']
# 'my id'
```

将tag转换成字符串时,多值属性会合并为一个值

```
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
rel_soup.a['rel']
# ['index']
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>
```

如果转换的文档是XML格式,那么tag中不包含多值属性

```
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
xml_soup.p['class']
# u'body strikeout'
```

## 2、可以遍历的字符串

字符串常被包含在tag内.Beautiful Soup用 NavigableString 类来包装tag中的字符串:

```
tag.string
# u'Extremely bold'
type(tag.string)
# <class 'bs4.element.NavigableString'>
```

一个 NavigableString 字符串与Python中的Unicode字符串相同,并且还支持包含在 [遍历文档树](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id18) 和 [搜索文档树](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id27) 中的一些特性. 通过 unicode() 方法可以直接将 NavigableString 对象转换成Unicode字符串:

```
unicode_string = unicode(tag.string)
unicode_string
# u'Extremely bold'
type(unicode_string)
# <type 'unicode'>
```

tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用 [replace_with()](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#replace-with) 方法:

```
tag.string.replace_with("No longer bold")
tag
# <blockquote>No longer bold</blockquote>
```

NavigableString 对象支持 [遍历文档树](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id18) 和 [搜索文档树](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id27) 中定义的大部分属性, 并非全部.尤其是,一个字符串不能包含其它内容(tag能够包含字符串或是其它tag),字符串不支持 .contents 或 .string 属性或 find() 方法.

如果想在Beautiful Soup之外使用 NavigableString 对象,需要调用 unicode() 方法,将该对象转换成普通的Unicode字符串,否则就算Beautiful Soup已方法已经执行结束,该对象的输出也会带有对象的引用地址.这样会浪费内存.

## 3、BeautifulSoup

BeautifulSoup 对象表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象,它支持 [遍历文档树](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id18) 和 [搜索文档树](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id27) 中描述的大部分的方法.

因为 BeautifulSoup 对象并不是真正的HTML或XML的tag,所以它没有name和attribute属性.但有时查看它的 .name 属性是很方便的,所以 BeautifulSoup 对象包含了一个值为 “[document]” 的特殊属性 .name

```
soup.name
# u'[document]'
```

## 4、注释及特殊字符串

Tag , NavigableString , BeautifulSoup 几乎覆盖了html和xml中的所有内容,但是还有一些特殊对象.容易让人担心的内容是文档的注释部分:

```
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string
type(comment)
# <class 'bs4.element.Comment'>
```

Comment 对象是一个特殊类型的 NavigableString 对象:

```
comment
# u'Hey, buddy. Want to buy a used parser'
```

但是当它出现在HTML文档中时, Comment 对象会使用特殊的格式输出:

```
print(soup.b.prettify())
# <b>
#  <!--Hey, buddy. Want to buy a used parser?-->
# </b>
```

Beautiful Soup中定义的其它类型都可能会出现在XML的文档中: CData , ProcessingInstruction , Declaration , Doctype .与 Comment 对象类似,这些类都是 NavigableString 的子类,只是添加了一些额外的方法的字符串独享.下面是用CDATA来替代注释的例子:

```
from bs4 import CData
cdata = CData("A CDATA block")
comment.replace_with(cdata)
 
print(soup.b.prettify())
# <b>
#  <![CDATA[A CDATA block]]>
# </b>
```

# 六、遍历文档树

还拿”爱丽丝梦游仙境”的文档来做例子:

```
html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>
 
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
 
<p class="story">...</p>
"""
 
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

通过这段例子来演示怎样从文档的一段内容找到另一段内容

## 1、子节点

一个Tag可能包含多个字符串或其它的Tag,这些都是这个Tag的子节点.Beautiful Soup提供了许多操作和遍历子节点的属性.

注意: Beautiful Soup中字符串节点不支持这些属性,因为字符串没有子节点

### （1）tag的名字

操作文档树最简单的方法就是告诉它你想获取的tag的name.如果想获取 <head> 标签,只要用 soup.head :

```
soup.head
# <head><title>The Dormouse's story</title></head>
 
soup.title
# <title>The Dormouse's story</title>
```

这是个获取tag的小窍门,可以在文档树的tag中多次调用这个方法.下面的代码可以获取<body>标签中的第一个<b>标签:

```
soup.body.b
# <b>The Dormouse's story</b>
```

通过点取属性的方式只能获得当前名字的第一个tag:

```
soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
```

如果想要得到所有的<a>标签,或是通过名字得到比一个tag更多的内容的时候,就需要用到 Searching the tree 中描述的方法,比如: find_all()

```
soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
```

### （2）.contents 和 .children

tag的 .contents 属性可以将tag的子节点以列表的方式输出:

```
head_tag = soup.head
head_tag
# <head><title>The Dormouse's story</title></head>
 
head_tag.contents
[<title>The Dormouse's story</title>]
 
title_tag = head_tag.contents[0]
title_tag
# <title>The Dormouse's story</title>
title_tag.contents
# [u'The Dormouse's story']
```

BeautifulSoup 对象本身一定会包含子节点,也就是说<html>标签也是 BeautifulSoup 对象的子节点:

```
len(soup.contents)
# 1
soup.contents[0].name
# u'html'
```

字符串没有 .contents 属性,因为字符串没有子节点:

```
text = title_tag.contents[0]
text.contents
# AttributeError: 'NavigableString' object has no attribute 'contents'
```

通过tag的 .children 生成器,可以对tag的子节点进行循环:

```
for child in title_tag.children:
    print(child)
    # The Dormouse's story
```

### （3）.descendants

.contents 和 .children 属性仅包含tag的直接子节点.例如,<head>标签只有一个直接子节点<title>

```
head_tag.contents
# [<title>The Dormouse's story</title>]
```

但是<title>标签也包含一个子节点:字符串 “The Dormouse’s story”,这种情况下字符串 “The Dormouse’s story”也属于<head>标签的子孙节点. .descendants 属性可以对所有tag的子孙节点进行递归循环 [[5\]](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id92) :

```
for child in head_tag.descendants:
    print(child)
    # <title>The Dormouse's story</title>
    # The Dormouse's story
```

上面的例子中, <head>标签只有一个子节点,但是有2个子孙节点:<head>节点和<head>的子节点, BeautifulSoup 有一个直接子节点(<html>节点),却有很多子孙节点:

```
len(list(soup.children))
# 1
len(list(soup.descendants))
# 25
```

### （4）.string

如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点:

```
title_tag.string
# u'The Dormouse's story'
```

如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同:

```
head_tag.contents
# [<title>The Dormouse's story</title>]
 
head_tag.string
# u'The Dormouse's story'
```

如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None :

```
print(soup.html.string)
# None
```

### （5）.strings 和 stripped_strings

如果tag中包含多个字符串 [[2\]](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id89) ,可以使用 .strings 来循环获取:

```
for string in soup.strings:
    print(repr(string))
    # u"The Dormouse's story"
    # u'\n\n'
    # u"The Dormouse's story"
    # u'\n\n'
    # u'Once upon a time there were three little sisters; and their names were\n'
    # u'Elsie'
    # u',\n'
    # u'Lacie'
    # u' and\n'
    # u'Tillie'
    # u';\nand they lived at the bottom of a well.'
    # u'\n\n'
    # u'...'
    # u'\n'
```

输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容:

```
for string in soup.stripped_strings:
    print(repr(string))
    # u"The Dormouse's story"
    # u"The Dormouse's story"
    # u'Once upon a time there were three little sisters; and their names were'
    # u'Elsie'
    # u','
    # u'Lacie'
    # u'and'
    # u'Tillie'
    # u';\nand they lived at the bottom of a well.'
    # u'...'
```

全部是空格的行会被忽略掉,段首和段末的空白会被删除

