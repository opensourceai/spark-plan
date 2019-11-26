# 一、关于Scrapy

Scrapy是一个快速的高级Web爬网和Web爬网框架，用于爬网网站并从其页面提取结构化数据。 它可以用于从数据挖掘到监视和自动化测试的广泛用途。

欲了解更多信息，包括功能列表，请访问Scrapy主页：[https://scrapy.org](https://scrapy.org/)

 

即使Scrapy最初是为Web抓取而设计的，它也可以用于使用API（例如Amazon Associates Web Services）或作为通用Web搜寻器来提取数据。

示例爬网的演练

为了向您展示Scrapy带来的好处，我们将通过最简单的运行的方法向您介绍Scrapy Spider的示例。

以下是在分页之后从网站http://quotes.toscrape.com抓取著名报价的代码：
```python
import scrapy

class QuotesSpider(scrapy.Spider):

  name = 'quotes'

  start_urls = [

   'http://quotes.toscrape.com/tag/humor/',

  ]

 

  def parse(self, response):

    for quote in response.css('div.quote'):

      yield {

        'text': quote.css('span.text::text').get(),
        'author': quote.xpath('span/small/text()').get(),

      }

 

    next_page = response.css('li.next a::attr("href")').get()

    if next_page is not None:

      yield response.follow(next_page, self.parse)
```

将其放在文本文件中，将其命名为quotes_spider.py之类的名称，然后使用runspider命令运行：

```shell
scrapy runspider quotes_spider.py -o quotes.json
```

完成此操作后，您将在quotes.json文件中具有JSON格式的引号列表，其中包含文本和作者，如下所示（此处重新格式化以提高可读性）：

```shell
[{
    "author": "Jane Austen",
    "text": "\u201cThe person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.\u201d"
},
{
    "author": "Groucho Marx",
    "text": "\u201cOutside of a dog, a book is man's best friend. Inside of a dog it's too dark to read.\u201d"
},
{
    "author": "Steve Martin",
    "text": "\u201cA day without sunshine is like, you know, night.\u201d"
},
...]
```

 

**刚刚发生了什么？**

当您运行命令scrapy runtimepider quotes_spider.py时，Scrapy会在其中查找Spider定义，并通过其搜寻器引擎运行它。

爬网开始于对start_urls属性中定义的URL进行请求（在这种情况下，仅是幽默类别中的引号的URL），然后调用默认的回调方法parse，将响应对象作为参数传递。在解析回调中，我们使用CSS选择器遍历quote元素，生成包含提取的引用文本和作者的Python dict，查找指向下一页的链接，并使用与回调相同的parse方法安排另一个请求。

在这里，您会注意到Scrapy的主要优势之一：请求是异步调度和处理的。这意味着Scrapy无需等待请求完成和处理，它可以同时发送另一个请求或执行其他操作。这也意味着即使某些请求失败或在处理过程中发生错误，其他请求也可以继续执行。

尽管这使您能够进行非常快速的爬网（以容错的方式同时发送多个并发请求），但是Scrapy还使您可以通过一些设置来控制爬网的礼貌。您可以执行以下操作：设置每个请求之间的下载延迟，限制每个域或每个IP的并发请求数量，甚至使用试图自动找出这些请求的自动限制扩展。

 

Tips：这是使用Feed导出来生成JSON文件，您可以轻松更改导出格式（例如XML或CSV）或存储后端（例如FTP或Amazon S3）。 您还可以编写项目管道以将项目存储在数据库中。

 

**还有什么？**

您已经了解了如何使用Scrapy从网站提取和存储项目，但这仅仅是表面。 Scrapy提供了许多强大的功能，使抓取变得简单而有效，例如：

使用扩展的CSS选择器和XPath表达式从HTML / XML源中选择和提取数据的内置支持，以及使用正则表达式提取的辅助方法。

一个交互式的Shell控制台（支持IPython），用于尝试CSS和XPath表达式以刮取数据，这在编写或调试Spider时非常有用。

内置支持以多种格式（JSON，CSV，XML）生成提要导出并将其存储在多个后端（FTP，S3，本地文件系统）中

强大的编码支持和自动检测功能，用于处理外来的，非标准的和损坏的编码声明。

强大的可扩展性支持，使您可以使用信号和定义明确的API（中间件，扩展和管道）插入自己的功能。

广泛的内置扩展和中间件，用于处理：

Cookie和会话处理

HTTP功能，如压缩，身份验证，缓存

用户代理欺骗

robots.txt

爬行深度限制

和更多Telnet控制台，用于挂接到Scrapy进程中运行的Python控制台中，以内省和调试您的搜寻器

再加上其他可重复使用的spider之类的东西，例如可从Sitemaps和XML / CSV feed爬网的站点，可自动下载与被抓取的项目关联的图像（或任何其他媒体）的媒体管道，可缓存的DNS解析器等等！

# 二、安装Scrapy

Scrapy在CPython（默认Python实现）和PyPy（从PyPy 5.9开始）下的Python 2.7和Python 3.5或更高版本上运行。

 

如果您使用的是Anaconda或Miniconda，则可以从conda-forge渠道安装该软件包，该渠道包含适用于Linux，Windows和OS X的最新软件包。

 

要使用conda安装Scrapy，请运行：

```shell
conda install -c conda-forge scrapy
```

 

另外，如果您已经熟悉Python软件包的安装，则可以使用以下方法从PyPI安装Scrapy及其依赖项：

```shell
pip install Scrapy
```

 

请注意，有时这可能需要解决某些Scrapy依赖项的编译问题，具体取决于您的操作系统，因此请务必查看特定于平台的安装说明。

强烈建议您在专用的virtualenv中安装Scrapy，以避免与系统软件包冲突。

值得了解的事情

Scrapy是用纯Python编写的，并且依赖于一些关键的Python包（以及其他一些包）：

lxml，高效的XML和HTML解析器

parsel，是在lxml之上编写的HTML / XML数据提取库，

w3lib，用于处理URL和网页编码的多功能帮助器

扭曲的异步网络框架

加密和pyOpenSSL，以处理各种网络级安全需求

测试Scrapy的最低版本为：

Twisted 14.0

lxml 3.4

pyOpenSSL 0.14

Scrapy可以使用这些软件包的较早版本，但不能保证它会继续运行，因为尚未对其进行测试。

其中一些软件包本身依赖于非Python软件包，这可能需要其他安装步骤，具体取决于您的平台。请查看下面特定于平台的指南。



使用虚拟环境（推荐）

TL; DR：我们建议在所有平台上的虚拟环境中安装Scrapy。

Python软件包可以全局安装（也就是系统范围内），也可以安装在用户空间中。 我们不建议在整个系统范围内安装刮板系统。

相反，我们建议您在所谓的“虚拟环境”（virtualenv）内安装scrapy。 Virtualenvs允许您与已经安装的Python系统软件包不冲突（这可能会破坏您的某些系统工具和脚本），并且仍然可以使用pip正常安装软件包（没有sudo等）。

要开始使用虚拟环境，请参阅virtualenv安装说明。 要在全球范围内安装它（在这里实际安装它会有所帮助），应该通过运行来解决：

```shell
$ [sudo] pip install virtualenv
```

 

Tips：如果使用Linux或OS X，则virtualenvwrapper是创建virtualenvs的便捷工具。

 

创建virtualenv之后，就可以像其他任何Python软件包一样，使用pip在其内部安装scrapy。 

可以将Python virtualenvs创建为默认使用Python 2或默认使用Python 3。

如果要使用Python 3安装scrapy，请在Python 3 virtualenv中安装scrapy。

如果要使用Python 2安装scrapy，请在Python 2 virtualenv中安装scrapy。

 

平台特定的安装说明

### Windows

尽管可以使用pip在Windows上安装Scrapy，但建议您安装Anaconda或Miniconda并使用conda-forge渠道中的软件包，这样可以避免大多数安装问题。

 

安装Anaconda或Miniconda后，请使用以下方法安装Scrapy：

```shell
conda install -c conda-forge scrapy
```

### Ubuntu 14.04 or above

目前，Scrapy已使用最新版本的lxml，twisted和pyOpenSSL进行了测试，并且与最新的Ubuntu发行版兼容。 但是它也应该支持Ubuntu的较早版本，例如Ubuntu 14.04，尽管存在TLS连接的潜在问题。

 

不要使用Ubuntu提供的python-scrapy软件包，它们通常太旧且太慢，无法赶上最新的Scrapy。

 

要在Ubuntu（或基于Ubuntu的）系统上安装scrapy，您需要安装以下依赖项：

```shell
sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

 

•lxml需要python-dev，zlib1g-dev，libxml2-dev和libxslt1-dev

•加密需要libssl-dev和libffi-dev

 


 如果您想在Python 3上安装scrapy，则还需要Python 3开发标头：

```shell
sudo apt-get install python3 python3-dev
```

 

在virtualenv内，您可以使用pip安装Scrapy之后：

```shell
pip install scrapy
```

注意; 相同的非Python依赖项可用于在Debian Jessie（8.0）及更高版本中安装Scrapy。

### Mac OS X

构建Scrapy的依赖项需要使用C编译器和开发标头。 在OS X上，这通常由Apple的Xcode开发工具提供。 要安装Xcode命令行工具，请打开一个终端窗口并运行：

```shell
xcode-select --install
```

 

有一个已知的问题，导致pip无法更新系统软件包。 必须解决此问题才能成功安装Scrapy及其依赖项。 以下是一些建议的解决方案：

 

1、（推荐）不要使用系统python，请安装与系统其余部分不冲突的新的更新版本。 使用自制程序包管理器的方法如下：

 

按照https://brew.sh/中的说明安装自制软件

 

更新您的PATH变量，以指出应在系统软件包之前使用自制软件软件包（如果将zsh用作默认外壳，则将.bashrc更改为.zshrc）：

```shell
echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.bashrc
```

 

重新加载.bashrc以确保已进行更改：

```shell
source ~/.bashrc
```

 

安装python：

```shell
brew install python
```

 

最新版本的python已捆绑了pip，因此您无需单独安装。 如果不是这种情况，请升级python：

```shell
brew update; brew upgrade python
```

 

2、（可选）在隔离的python环境中安装Scrapy。

 

此方法是解决上述OS X问题的一种解决方法，但它是管理依赖项的总体良好做法，并且可以补充第一种方法。

 

virtualenv是可用于在python中创建虚拟环境的工具。 我们建议您阅读类似http://docs.python-guide.org/zh-CN/latest/dev/virtualenvs/的教程以开始使用。

 

这些解决方法中的任何一种之后，您都应该能够安装Scrapy：

```shell
pip install Scrapy
```

 

 

我们建议使用最新的PyPy版本。测试的版本是5.9.0。对于PyPy3，仅测试了Linux安装。

 

现在，大多数可疑的依赖对象都具有CPython的二进制轮子，而PyPy没有。这意味着将在安装过程中建立这些依赖关系。在OS X上，您可能会遇到构建加密技术依赖项的问题，此处描述了此问题的解决方案，即酿造install openssl，然后导出此命令建议的标志（仅在安装scrapy时需要）。在Linux上安装除了安装构建依赖项外没有其他特殊问题。未测试在Windows上使用PyPy安装scrapy。

 

您可以通过运行scrapy bench来检查scrapy是否已正确安装。如果此命令给出诸如TypeError：...的错误，则得到2个意外的关键字参数，这意味着setuptools无法获取一个特定于PyPy的依赖项。要解决此问题，请运行pip install'PyPyDispatcher> = 2.1.0'。

 

故障排除

AttributeError：“模块”对象没有属性“ OP_NO_TLSv1_1”

在安装或升级Scrapy，Twisted或pyOpenSSL之后，您可能会收到带有以下回溯的异常：

 

```shell
[…]
  File "[…]/site-packages/twisted/protocols/tls.py", line 63, in <module>
    from twisted.internet._sslverify import _setAcceptableProtocols
  File "[…]/site-packages/twisted/internet/_sslverify.py", line 38, in <module>
    TLSVersion.TLSv1_1: SSL.OP_NO_TLSv1_1,
AttributeError: 'module' object has no attribute 'OP_NO_TLSv1_1'
```

出现此异常的原因是您的系统或虚拟环境具有Twisted版本不支持的pyOpenSSL版本。

要安装您的Twisted版本支持的pyOpenSSL版本，请使用tls extra选项重新安装Twisted：

```shell
pip install twisted[tls]
```

 

# 三、Scrapy教程

在本教程中，我们假设您的系统上已经安装了Scrapy。如果不是这种情况，请参阅安装指南。

 

本教程将指导您完成以下任务：

 

创建一个新的Scrapy项目

编写代码爬网站点并提取数据

使用命令行导出抓取的数据

更改爬虫以递归地跟随链接

使用爬虫参数

Scrapy用Python编写。如果您是该语言的新手，则可能首先要了解该语言的外观，以充分利用Scrapy。

 

## 一、建立项目

在开始抓取之前，您将必须设置一个新的Scrapy项目。 输入您要存储代码并运行的目录：

```shell
scrapy startproject tutorial
```

这将创建一个包含以下内容的教程目录：

```
tutorial/
    scrapy.cfg            # deploy configuration file
 
    tutorial/             # project's Python module, you'll import your code from here
        __init__.py
 
        items.py          # project items definition file
 
        middlewares.py    # project middlewares file
 
        pipelines.py      # project pipelines file
 
        settings.py       # project settings file
 
        spiders/          # a directory where you'll later put your spiders
            __init__.py
```

 

我们的第一只Spider

Spider是您定义的类，Scrapy用于从网站（或一组网站）中获取信息。 他们必须将Spider子类化，并定义最初的请求，可以选择如何跟随页面中的链接，以及如何解析下载的页面内容以提取数据。

 

这是我们第一个Spider的代码。 将其保存在项目中tutorial / spiders目录下的一个名为quotes_spider.py的文件中：

```python
import scrapy
 
 
class QuotesSpider(scrapy.Spider):
    name = "quotes"
 
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
```

如您所见，我们的Spider子类scrapy.Spider并定义了一些属性和方法：

 

名称：标识Spider。 它在一个项目中必须是唯一的，也就是说，您不能为不同的Spider设置相同的名称。

 

start_requests（）：必须返回一个可迭代的请求（您可以返回请求列表或编写一个生成器函数），Spider将从中开始爬行。 随后的请求将从这些初始请求中依次生成。

 

parse（）：一种方法，将调用该方法来处理为每个请求下载的响应。 response参数是TextResponse的一个实例，该实例保存页面内容并具有其他有用的方法来处理它。

 

parse（）方法通常解析响应，提取刮取的数据作为字典，还查找要遵循的新URL并从中创建新请求（请求）。

 

如何运行我们的Spider

要使我们的Spider工作，请转到项目的顶级目录并运行：

```shell
scrapy crawl quotes
```

此命令运行带有我们刚刚添加的名称引号的Spider，它将发送对quotes.toscrape.com域的一些请求。 您将获得类似于以下的输出：

```shell
... (omitted for brevity)
2016-12-16 21:24:05 [scrapy.core.engine] INFO: Spider opened
2016-12-16 21:24:05 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2016-12-16 21:24:05 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/2/> (referer: None)
2016-12-16 21:24:05 [quotes] DEBUG: Saved file quotes-1.html
2016-12-16 21:24:05 [quotes] DEBUG: Saved file quotes-2.html
2016-12-16 21:24:05 [scrapy.core.engine] INFO: Closing spider (finished)
...
```

现在，检查当前目录中的文件。 您应该注意到已经创建了两个新文件：quotes-1.html和quotes-2.html，其中包含相应URL的内容，如我们的parse方法所指示的那样。

注意：

到底发生了什么？

Scrapy调度Spider的start_requests方法返回的scrapy.Request对象。 在收到每个响应时，它实例化Response对象并调用与请求关联的回调方法（在本例中为parse方法），并将响应作为参数传递。

 

start_requests方法的快捷方式

无需实现从URL生成scrapy.Request对象的start_requests（）方法，您只需定义带有URL列表的start_urls类属性即可。 然后，start_requests（）的默认实现将使用此列表来为您的Spider创建初始请求：

```python
import scrapy
 
 
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
 
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
```

即使我们没有明确告诉Scrapy这样做，也会调用parse（）方法来处理这些URL的每个请求。 发生这种情况是因为parse（）是Scrapy的默认回调方法，对于没有显式分配的回调的请求将调用该方法。

提取数据

学习如何使用Scrapy提取数据的最好方法是使用Scrapy shell尝试选择器。 运行：

```shell
scrapy shell 'http://quotes.toscrape.com/page/1/'
```

您将看到类似以下内容

```shell
[ ... Scrapy log here ... ]
2016-09-19 12:09:27 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x7fa91d888c90>
[s]   item       {}
[s]   request    <GET http://quotes.toscrape.com/page/1/>
[s]   response   <200 http://quotes.toscrape.com/page/1/>
[s]   settings   <scrapy.settings.Settings object at 0x7fa91d888c10>
[s]   spider     <DefaultSpider 'default' at 0x7fa91c8af990>
[s] Useful shortcuts:
[s]   shelp()           Shell help (print this help)
[s]   fetch(req_or_url) Fetch request (or URL) and update local objects
[s]   view(response)    View response in a browser
>>> 
```

使用shell，您可以尝试使用带有响应对象的CSS选择元素：

```python
>>> response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]
```

 

运行response.css（'title'）的结果是一个称为SelectorList的类似列表的对象，该对象表示围绕XML / HTML元素的Selector对象的列表，并允许您运行进一步的查询来细化选择或提取内容 数据。

要从上面的标题中提取文本，您可以执行以下操作：

```python
>>> response.css('title::text').getall()
['Quotes to Scrape']
```

 

这里有两点需要注意：一是我们在CSS查询中添加了:: text，这意味着我们只想直接在<title>元素内选择text元素。 如果不指定:: text，则会获得完整的title元素，包括其标签：

```
>>> response.css('title').getall()
['<title>Quotes to Scrape</title>']
```

 

另一件事是，调用.getall（）的结果是一个列表：选择器有可能返回多个结果，因此我们将它们全部提取出来。 当您知道只想要第一个结果时，在这种情况下，您可以执行以下操作：

```python
>>> response.css('title::text').get()
'Quotes to Scrape'
```

或者，您可以编写：

```python
>>> response.css('title::text')[0].get()
'Quotes to Scrape'
```

但是，直接在SelectorList实例上使用.get（）可以避免IndexError，并且在找不到与所选内容匹配的任何元素时返回None。

 

这里有一个教训：对于大多数抓取代码，您希望它能够对由于页面上找不到内容而导致的错误具有弹性，因此即使某些部分未能被抓取，您也至少可以获取一些数据。

 

除了getall（）和get（）方法之外，您还可以使用re（）方法使用正则表达式进行提取：

 

```python
>>> response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']
>>> response.css('title::text').re(r'Q\w+')
['Quotes']
>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']
```

 

为了找到合适的CSS选择器，您可能会发现使用view（response）从Web浏览器的外壳中打开响应页面很有用。 您可以使用浏览器的开发人员工具检查HTML并提供选择器（请参阅使用浏览器的开发人员工具进行抓取）。

 

Selector Gadget还是一个不错的工具，可以快速找到用于视觉选择元素的CSS选择器，该选择器可在许多浏览器中使用。

 

XPath：简要介绍

除了CSS，Scrapy选择还支持使用XPath表达式：

```sehll
>>> response.xpath('//title')
[<Selector xpath='//title' data='<title>Quotes to Scrape</title>'>]
>>> response.xpath('//title/text()').get()
'Quotes to Scrape'
```

XPath表达式非常强大，并且是Scrapy Selectors的基础。实际上，CSS选择器是在后台转换为XPath的。您可以看到，如果您仔细阅读外壳中选择器对象的文本表示形式。

 

尽管XPath表达式可能不如CSS选择器流行，但它提供了更多功能，因为除了浏览结构之外，它还可以查看内容。使用XPath，您可以选择以下内容：选择包含文本“下一页”的链接。这使XPath非常适合于抓取任务，并且即使您已经知道如何构造CSS选择器，我们也鼓励您学习XPath，这将使抓取更加容易。

 

提取报价和作者

```html
http://quotes.toscrape.com中的每个引用都由如下所示的HTML元素表示：<div class="quote">
    <span class="text">“The world as we have created it is a process of our
    thinking. It cannot be changed without changing our thinking.”</span>
    <span>
        by <small class="author">Albert Einstein</small>
        <a href="/author/Albert-Einstein">(about)</a>
    </span>
    <div class="tags">
        Tags:
        <a class="tag" href="/tag/change/page/1/">change</a>
        <a class="tag" href="/tag/deep-thoughts/page/1/">deep-thoughts</a>
        <a class="tag" href="/tag/thinking/page/1/">thinking</a>
        <a class="tag" href="/tag/world/page/1/">world</a>
    </div>
</div>
```

让我们打开scrapy shell，玩一会儿，找出如何提取所需的数据：

```shell
$ scrapy shell 'http://quotes.toscrape.com'
```

我们获得带有HTML报价的选择器的列表，其中包括：

```shell
>>> response.css("div.quote")
```

上面的查询返回的每个选择器都允许我们在其子元素上运行进一步的查询。 让我们将第一个选择器分配给变量，以便我们可以直接在特定引号上运行CSS选择器：

```shell
>>> quote = response.css("div.quote")[0]
```

现在，让我们使用刚刚创建的quote对象从该报价中提取文本，作者和标签：

```shell
>>> text = quote.css("span.text::text").get()
>>> text
'“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'
>>> author = quote.css("small.author::text").get()
>>> author
'Albert Einstein'
```

鉴于标签是字符串列表，我们可以使用.getall（）方法来获取所有标签：

```shell
>>> tags = quote.css("div.tags a.tag::text").getall()
>>> tags
['change', 'deep-thoughts', 'thinking', 'world']
```

在弄清楚如何提取每一位之后，我们现在可以遍历所有引号元素并将它们放到Python字典中：

```shell
>>> for quote in response.css("div.quote"):
...     text = quote.css("span.text::text").get()
...     author = quote.css("small.author::text").get()
...     tags = quote.css("div.tags a.tag::text").getall()
...     print(dict(text=text, author=author, tags=tags))
{'tags': ['change', 'deep-thoughts', 'thinking', 'world'], 'author': 'Albert Einstein', 'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'}
{'tags': ['abilities', 'choices'], 'author': 'J.K. Rowling', 'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”'}
    ... a few more of these, omitted for brevity
>>> 
```

在我们的Spider中提取数据

让我们回到蜘蛛。 到目前为止，它没有特别提取任何数据，只是将整个HTML页面保存到本地文件中。 让我们将上面的提取逻辑集成到我们的Spider中。

 

Scrapy Spider通常会生成许多字典，其中包含从页面提取的数据。 为此，我们在回调中使用yield Python关键字，如下所示：

```python
import scrapy
 
 
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
 
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
```

如果运行此Spider，它将输出提取的数据和日志：

```
2016-09-19 18:57:19 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'tags': ['life', 'love'], 'author': 'André Gide', 'text': '“It is better to be hated for what you are than to be loved for what you are not.”'}
2016-09-19 18:57:19 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'tags': ['edison', 'failure', 'inspirational', 'paraphrased'], 'author': 'Thomas A. Edison', 'text': "“I have not failed. I've just found 10,000 ways that won't work.”"}
```

 

存储抓取的数据

存储抓取数据的最简单方法是使用Feed导出，并使用以下命令：

```shell
scrapy crawl quotes -o quotes.json
```

这将生成一个quotes.json文件，其中包含所有以JSON序列化的抓取项。

 

由于历史原因，Scrapy会附加到给定文件，而不是覆盖其内容。 如果您两次运行此命令而没有在第二次之前删除该文件，那么您将得到一个损坏的JSON文件。

 

您还可以使用其他格式，例如JSON Lines：

```shell
scrapy crawl quotes -o quotes.jl
```

 

JSON Lines格式很有用，因为它像流一样，您可以轻松地向其添加新记录。 当您运行两次时，它就不会遇到同样的JSON问题。 另外，由于每条记录都是单独的一行，因此您可以处理大文件而不必将所有内容都放入内存中，因此有类似JQ的工具可以在命令行中帮助您完成此操作。

 

在小型项目中（例如本教程中的项目），这应该足够了。 但是，如果要对已刮除的物料执行更复杂的操作，则可以编写物料管道。 创建项目时，已在tutorial / pipelines.py中为项目管道设置了占位符文件。 尽管您只想存储已刮除的项目，则无需实施任何项目管道。

 

以下链接

假设，您不仅需要从http://quotes.toscrape.com的前两个页面中抓取内容，还希望从网站的所有页面中引用内容。

 

现在您知道了如何从页面中提取数据，让我们看看如何跟踪页面中的链接。

 

首先是将链接提取到我们要关注的页面。 检查我们的页面，我们可以看到指向下一页的链接，带有以下标记：

```html
<ul class="pager">
    <li class="next">
        <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
    </li>
</ul>
```

我们可以尝试将其提取到shell中：

```shell
>>> response.css('li.next a').get()
'<a href="/page/2/">Next <span aria-hidden="true">→</span></a>'
```

这获得了anchor元素，但我们需要属性href。 为此，Scrapy支持CSS扩展，可让您选择属性内容，如下所示：

```shell
>>> response.css('li.next a::attr(href)').get()
'/page/2/'
```

还有一个attrib属性可用

```shell
>>> response.css('li.next a').attrib['href']
'/page/2'
```

现在让我们看一下我们的Spider，将其修改为以递归方式链接到下一页的链接，并从中提取数据：

```python
import scrapy
 
 
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
 
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
 
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
```

现在，在提取数据之后，parse（）方法将查找到下一页的链接，使用urljoin（）方法构建完整的绝对URL（因为链接可以是相对的），并产生对下一页的新请求， 将其自身注册为回调，以处理下一页的数据提取并保持所有页面的爬网。

 

您在这里看到的是Scrapy的以下链接机制：当您在回调方法中产生请求时，Scrapy将安排该请求的发送并在该请求完成时注册要执行的回调方法。

 

使用此工具，您可以构建复杂的搜寻器，并根据定义的规则跟踪链接，并根据其访问的页面提取不同类型的数据。

 

在我们的示例中，它创建了一个循环，将其链接到下一页的所有链接，直到找不到该链接为止-便于通过分页方式爬网博客，论坛和其他网站。

 

创建请求的快捷方式

作为创建请求对象的快捷方式，您可以使用response.follow：

```python
import scrapy
 
 
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
 
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
 
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
```

与scrapy.Request不同，response.follow直接支持相对URL-无需调用urljoin。 注意response.follow仅返回一个Request实例； 您仍然必须产生此请求。

 

您也可以将选择器传递给response.follow而不是字符串。 该选择器应提取必要的属性：

```python
for href in response.css('li.next a::attr(href)'):
    yield response.follow(href, callback=self.parse)
```

 

对于<a>元素，有一个快捷方式：response.follow自动使用其href属性。 因此，代码可以进一步缩短：

```python
for a in response.css('li.next a'):
    yield response.follow(a, callback=self.parse)
```

注意：esponse.follow（response.css（'li.next a'））无效，因为response.css返回具有所有结果选择器的列表状对象，而不是单个选择器。 像上面示例中的for循环，或response.follow（response.css（'li.next a'）[0]）都可以。

 

更多示例和模式

这是另一个说明回调和后续链接的爬虫链接，这次是用于抓取作者信息：

```python
import scrapy
 
 
class AuthorSpider(scrapy.Spider):
    name = 'author'
 
    start_urls = ['http://quotes.toscrape.com/']
 
    def parse(self, response):
        # follow links to author pages
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)
 
        # follow pagination links
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)
 
    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()
 
        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
```

 

该爬虫将从首页开始，它将跟随指向作者页面的所有链接，并为每个作者页面调用parse_author回调，以及如前所述的带有parse回调的分页链接。

 

在这里，我们将回调传递给response.follow作为位置参数，以使代码更短；它也适用于scrapy.Request。

 

parse_author回调定义了一个辅助函数，用于从CSS查询中提取和清除数据，并生成包含作者数据的Python字典。

 

该爬虫演示的另一件有趣的事情是，即使同一位作者的引文很多，我们也不必担心会多次访问同一作者页面。默认情况下，Scrapy过滤掉对已访问URL的重复请求，避免了由于编程错误而导致服务器过多访问的问题。可以通过设置DUPEFILTER_CLASS进行配置。

 

希望到目前为止，您已经对如何在Scrapy中使用跟踪链接和回调的机制有了很好的了解。

 

作为利用以下链接机制的蜘蛛的另一个示例，请查看CrawlSpider类中的通用爬虫，该爬虫实现了一个小的规则引擎，您可以使用该规则引擎在其上编写爬虫。

 

同样，一种常见的模式是使用一个技巧将更多数据传递给回调，从而使用来自多个页面的数据来构建项目。

 

使Spider蛛参数

您可以在运行爬虫时使用-a选项为爬虫提供命令行参数：

```shell
scrapy crawl quotes -o quotes-humor.json -a tag=humor
```

 

这些参数会传递给Spider的__init__方法，并默认成为爬虫属性。

在此示例中，为tag参数提供的值可通过self.tag获得。 您可以使用它使您的Spider只获取带有特定标记的引号，并根据参数构建URL：

 

```shell
import scrapy
 
 
class QuotesSpider(scrapy.Spider):
    name = "quotes"
 
    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)
 
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }
 
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```

如果您将tag = humor参数传递给该爬虫，您会注意到它只会访问来自幽默标签的URL，例如http://quotes.toscrape.com/tag/humor。

 

最好的学习方法是通过示例，Scrapy也不例外。 因此，有一个名为quotesbot的示例Scrapy项目，您可以使用它来玩和了解有关Scrapy的更多信息。 它包含两个用于http://quotes.toscrape.com的蜘蛛，一个使用CSS选择器，另一个使用XPath表达式。

 

quotesbot项目可在以下网址获得：https：//github.com/scrapy/quotesbot。 您可以在项目的自述文件中找到有关它的更多信息。

 

如果您熟悉git，则可以签出代码。 否则，您可以通过单击此处将项目下载为zip文件。

 

 

