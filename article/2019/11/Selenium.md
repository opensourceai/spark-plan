# 一、关于Selenium

Selenium 是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括IE（7, 8, 9, 10, 11），[Mozilla Firefox](https://baike.baidu.com/item/Mozilla Firefox/3504923)，Safari，Google Chrome，Opera等。这个工具的主要功能包括：测试与浏览器的兼容性——测试你的应用程序看是否能够很好得工作在不同浏览器和操作系统之上。测试系统功能——创建回归测试检验软件功能和用户需求。支持自动录制动作和自动生成 .Net、Java、Perl等不同语言的测试脚本、

`Selenium Python` 提供了一个简单的API 便于我们使用 `Selenium WebDriver`编写 功能/验收测试。 通过Selenium Python的API，你可以直观地使用所有的 `Selenium WebDriver` 功能

`Selenium Python`提供了一个很方便的接口来驱动 `Selenium WebDriver` ，例如 `Firefox`、`Chrome`、`Ie`,以及Remote ，目前支持的`python`版本有`2.7`, `3.2`, `3.3` 和 `3.4`.

使用python爬虫调用selenium来模拟正常用户访问浏览器.

# 二、安装与配置

你可以从[这里](http://pypi.python.org/pypi/selenium) 下载python的selenium安装包，但是更好的办法是用`pip`来安装。 `Python3.4`的标准库里就有现成的`pip`工具，可以用`pip`安装selenium: 

win: pip install selenium

liunx: pip3 install selenium

## windows用户的详细说明

注意：你需要联网来完成这个安装

1. 安装python3.4 [安装地址](http://www.python.org/download)

2. 用`cmd.exe`开启命令行，并用下面的命令安装`selenium`

```shell
C:\Python34\Scripts\pip.exe install selenium
```

现在你可以用`python`来运行你的测试脚本了。例如，如果你创建了一个Selenium脚本然后保存到文件`C:\my_selenium_script.py`,然后运行它：

```shell
C:\Python34\python.exe C:\my_selenium_script.py
```

## 下载Selenium server

注意：如果你想要使用 `Remote WebDriver`，必须要安装`Selenium server`,更多的细节可以看[这里](http://selenium-python.readthedocs.org/getting-started.html#selenium-remote-webdriver)。 如果你刚开始学Selenium,你可以跳过这一块从下一章节开始。

`Selenium server` 是个`Java`程序，推荐使用`1.6`及以上的`JRE`来运行`Selenium server`。 你可以从[这里](http://seleniumhq.org/download/)下载`2.x`的 `Selenium server`，文件名看起来应该类似于这样`selenium-server-standalone-2.x.x.jar` 什么时候你都可以下载到最新的2.x Selenium server

如果你的机器没有安装JRE，你可以从[JRE from the Oracle website](http://www.oracle.com/technetwork/java/javase/downloads/index.html)下载一个。如果你使用的是`GNU/Linux`系统并且有`ROOT`权限的话，你也可以使用系统命令来安装JRE。 如果你的PATH(环境变量)里 `java`命令是可用的话，你可以用这个命令来开启`Selenium server`:

```shell
java -jar selenium-server-standalone-2.x.x.jar
```

把`2.x.x`替换成你从网下下载的版本。 如果是一个`非``ROOT`用户安装的JRE，或者环境变量里`java`命令不可用，你可以输入`java`命令的相对路径或者绝对路径，同样你也可以提供`Selenium server`的相对路径或者绝对路径:

```shell
/path/to/java -jar /path/to/selenium-server-standalone-2.x.x.jar
```

# 三、使用教程

如果你已经安装好Python 和 Selenium，可以这样开始使用：

```shell
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```

把上面的脚本保存到文件(例：python_org_search.py)，然后就可以这样运行它了：

```shell
  python python_org_search.py
```

运行的python需要安装 selenium 模块

## 实例分析

`selenium.webdriver` 模块提供了所有 WebDriver的实现，现在支持的WebDriver的实现有 Firefox,Ie,Chrome,Remote,`Keys`类提供了键盘的代码（回车,ALT,F1等等）

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```

然后我们创建一个Firefox的实例：

```python
driver = webdriver.Firefox()
```

`driver.get`方法会导向给定的URL的页面，WebDriver会等待页面完全加载完(就是`onload`函数被触发了),才把程序的控制权交给你的测试或者脚本。 但是如果你的页面用了太多的AJAX，那么这个机制就没什么卵用了，因为它不知道页面到底是什么时候加载完。

```python
driver.get("http://www.python.org")
```

WebDrive提供了一系统类似于`find_element_by_*`的方法来寻找页面元素，例如，我们利用`find_element_by_name`方法，通过元素的`name`属性来定位一个文本输入框元素。 更详细的寻找元素的方法可以参阅 [第四章-元素定位](https://github.com/StephinChou/seleniumDocument/blob/master/4.元素定位.md):

```python
elem = driver.find_element_by_name("q")
```

接着我们发送了一些字符，类似于用键盘直接输入。特殊的键盘符我们可以导入`selenium.webdriver.common.keys`,然后用`Keys`类来表示:

```python
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
```

提交页面之后我们应该确认一下是否有返回，为了确定有东西返回，我们在这里下一个断言:

```python
assert "No results found." not in driver.page_source
```

最后浏览器窗口被关闭了，你也可以调用`quit`方法来代替`close`，区别在于`quit`会退出整个浏览器，而`close`只会关闭一个标签，但是如果浏览器只有一个标签，那么这两个方法完全一样，都会关闭整个浏览器。

```python
driver.close()
```

## 使用Selenium测试

Selenium经常被用来写测试用例，它本身的包不提供测试的工具或者框架。我们可以用Python的单元测试模块来编写测试用例。 另一个工具/框架的选择是？？？ (原文：The other options for a tool/framework are py.test and nose.) 在本章节我们使用`unittest`做框架，下面是一个用`unittest`模块改进后的例子，是对 `python.org` 函数搜索功能的测试:

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
class PythonOrgSearch(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Firefox()
 
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
 
 
    def tearDown(self):
        self.driver.close()
 
if __name__ == "__main__":
    unittest.main()
```

你可以在shell里运行这个测试用例:

```shell
python test_python_org_search.py
.
----------------------------------------------------------------------
Ran 1 test in 15.566s
 
OK
```

上面的结果表明我们的测试用例成功执行了

## 实例分析

脚本的开头我们引入了所有需要的模块，单元测试是python内置的基于`Java's JUnit`的模块，提供了组织单元测试的框架。 `selenium.webdriver`模块提供了WebDriver的所有实现： Firefox,Ie,Chrome,Remote,`Keys`类提供了键盘的代码（回车,ALT,F1等等）：

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```

测试用例类继承了`unittest.TestCase`类，这表明这个类是一个测试用例：

```python
class PythonOrgSearch(unittest.TestCase):
```

`setUp`函数进行了初始化，你将要在这个类里编写的所有测试方法都要先调用这个方法，接着我们创建了一个`Firefox WebDriver`实例：

```python
def setUp(self):
    self.driver = webdriver.Firefox()
```

接下来是测试用例的方法，它应该总是以字符'test'开始. 方法的第一行 本地引用了 `setUp`方法中创建的driver对象：

```python
def test_search_in_python_org(self):
    driver = self.driver
```

`driver.get`方法会导向给定的URL的页面，WebDriver会等待页面完全加载完(就是`onload`函数被触发了),才把程序的控制权交给你的测试或者脚本。 但是如果你的页面用了太多的AJAX，那么这个机制就没什么卵用了，因为它不知道页面到底是什么时候加载完。

```python
driver.get("http://www.python.org")
```

下一行是个断言，确认页面标题里是否有'Python'这个单词:

```python
self.assertIn("Python", driver.title)
```

WebDrive提供了一系统类似于`find_element_by_*`的方法来寻找页面元素，例如，我们利用`find_element_by_name`方法，通过元素的`name`属性来定位一个文本输入框元素。 更详细的寻找元素的方法可以参阅 [第四章-元素定位](https://python-selenium-zh.readthedocs.io/zh_CN/latest/2.开始/):

```python
elem = driver.find_element_by_name("q")
```

接着我们发送了一些字符，类似于用键盘直接输入。特殊的键盘符我们可以导入`selenium.webdriver.common.keys`,然后用`Keys`类来表示:

```python
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
```

提交页面之后我们应该确认一下是否有返回，为了确定有东西返回，我们在这里下一个断言:

```python
assert "No results found." not in driver.page_source
```

最后浏览器窗口被关闭了，你也可以调用`quit`方法来代替`close`，区别在于`quit`会退出整个浏览器，而`close`只会关闭一个标签，但是如果浏览器只有一个标签，那么这两个方法完全一样，都会关闭整个浏览器。

```python
driver.close()
```

Final lines are some boiler plate code to run the test suite:

```python
if __name__ == "__main__":
    unittest.main()
```

## 使用Selenium 的 remote WebDriver

要使用remote WebDriver，你先要运行Selenium server,用下面这个命令:

```python
  java -jar selenium-server-standalone-2.x.x.jar
```

运行Selenium server时，你可以看到类似这样一条信息:

```python
  15:43:07.541 INFO - RemoteWebDriver instances should connect to: http://127.0.0.1:4444/wd/hub
```

意思是说你可以用这个URL连接到 remote WebDriver,下面是一些例子:

```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)
 
driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.OPERA)
 
driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)
```

`desired_capabilities` 是一个`dict`，如果你不使用默认的`dict`，你可以自己指定值:

```python
driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities={'browserName': 'htmlunit',
                         'version': '2',
                        'javascriptEnabled': True})
```

 

# 四、导航

你用WebDriver要做的第一件事就是指定一个链接，一般我们使用`get`方法：

```python
driver.get("http://www.google.com")
```

WebDriver会等待页面完全加载完(就是`onload`函数被触发了),才把程序的控制权交给你的测试或者脚本。 但是如果你的页面用了太多的AJAX，那么这个机制就没什么卵用了，因为它不知道页面到底是什么时候加载完。如果你需要确定页面完全加载完了，你可以使用`waits`

## 页面交互

我们比较喜欢做的事情就是和页面交互，准确的说，是和页面里的HTML元素交互。首先，我们要找到一个元素，WebDrive提供了许多方法查找元素，例如，给定一个这样的元素：

```python
<input type="text" name="passwd" id="passwd-id" />
```

你可以用下列任意方法找到它：

```python
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
```

你也可以通过文本信息来找到一个链接，但是要注意，文本必须要完全匹配。 在使用`XPATH`的时候也要注意，如果有多个元素匹配，只会返回第一个。如果匹配不到任何元素，会抛出一个`NoSuchElementException`异常。

WebDriver有一个 基于对象的 API，我们可以通过同一个接口代表所有类型的元素，这意味着当你敲击你IDE的自动补全组合键的时候，虽然你会看到你可以调用很多方法，但不是所有的方法都行得通。不过不要担心！WebDriver会自己尝试做正确的选择。并且如果你调用一个没用的方法(例如在一个`meta`标签上调用`setSelected()`),WebDriver会抛出一个异常

那么，当你获取到一个元素之后，你可以做些什么呢？首先，你可能会想输入一些文本到一个文本区域:

```python
element.send_keys("some text")
```

你可以使用`Keys`类来模拟输入方向键:

```python
element.send_keys(" and some", Keys.ARROW_DOWN)
```

理论上任意的元素都可以调用`send_keys`方法,就是说我们可以测试例如Gmail的键盘快捷键。`send_keys`的副作用就是输入文本到文本域不会自动清除，而是会附加到原有的文本后面，我们可以使用`clear`方法来很方便的清除文本框或者文本域的内容:

```python
element.clear()
```

## 填充表单

我们已经知道怎么向一个文本框和文本域输入内容，但是其他元素我们要怎么处理？ 你可以触发下拉选框，并且用`setSelected`方法来让一个选项被选中，处理`选择框`不会很困难:

```python
element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s") % option.get_attribute("value")
    option.click()
```

这段代码会找到页面的第一个选择框元素，然后遍历每个选项，输出他们的值，并且依次选中。

你可以看到，这种方式处理选择框不太高效，WebDriver支持许多类，其中包括一个`Select`的类，给我们提供了许多有用的方法：

```python
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.selct_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
```

WebDriver 也提供了取消选中选项的方法：

```python
select = Select(driver.find_element_by_id('id'))
select.deselect_all()
```

上面的代码会取消页面第一个选择框的所有选中项。

假设测试中，我们需要所有默认选中项的列表，`Select`类提供了一个属性:

```python
select = Select(driver.find_element_by_xpath("xpath"))
all_selected_options = select.all_selected.options
```

获取所有可用的选项：

```python
options = select.options
```

一旦你填写完表单，一般就要提交表单，一个方法是找到提交按钮然后点击它：

```python
# Assume the button has the ID "submit" :)
driver.find_element_by_id("submit").click()
```

WebDriver 对每个元素都提供一个`submit`方法，如果在一个表单内的元素上调用，WebDriver会沿着DOM树往上一直寻找，直到找到一个闭合的表单为止，然后调用`submit`方法；如果元素不在表单内，那么会抛出一个`NoSuchElementException`异常。

## 拖放

你可以使用拖放功能，移动确定数量的元素，或者拖到另一个元素上面：

```python
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")
 
from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element,target).perform()
```

可以看这个页面的[演示](http://www.w3schools.com/html/html5_draganddrop.asp)

## 在窗口(window)和框架(frame)间移动

现在的网页应用里没有页面框架或者只用一个窗口就包含了所有内容的已经很少了。WebDriver 支持在指定的窗口间移动，方法为`switch_to_window`：

```python
driver.switch_to_window("windowName")
```

现在所有的driver的调用都会指向这个给定的窗口，但是我们怎么知道窗口的名字是什么呢？可以看一看打开这个窗口的`javascript`脚本或者`link`链接:

```html
<a href="somewhere.html" target="windowName">Click here to open a new window</a>
```

或者，你可以传一个`window handle`给`switch_to_window()`方法,它就可以像这样迭代每一个打开的窗口:

```python
for handle in driver.window_handles:
    driver.switch_to_window(handle)
```

你也可以在框架和框架之间切换 (or into iframes):

```python
driver.switch_to_frame("frameName")
```

我们可以用`.`分离路径来访问子框架，并且可以指定它的索引:

```python
driver.switch_to_frame("frameName.0.child")
```

这会跳到'frameName'框架内第一个名为'child'的子框架。All frames are evaluated as if from *top*.

一旦我们操作完了框架，我们可以通过下面的操作回到父框架：

```python
driver.switch_to_default_content()
```

## 弹出对话框

Selenium内置支持处理弹出对话框，当你触发了弹框操作，你可以用下面的方法获得对话框元素：

```python
alert = driver.switch_to_alert()
```

上述代码返回当前打开的对话框对象，有了这个对象 我们可以做确定、忽略、阅读提示文本或者甚至输入prompt,这个接口可以很好的操作alerts、confirms、prompts等对话框。更多内容参阅API文档

## 导航：历史记录和定位

前面我们可以使用get命令（`driver.get("http://www.example.com")`）导航到一个页面。如你所见，WebDriver有一些较小的，侧重任务的接口，导航是一个很有用的任务，要打开一个页面，你可以使用`get`方法:

```python
driver.get("http://www.example.com")
```

要在浏览器的历史记录的后退或者前进:

```python
driver.forward()
driver.back()
```

要记得这些函数完全依赖于底层驱动，如果你过去习惯某一个浏览器的运行状态，当切换到新的浏览器时，调用这些方法有可能会出现预料之外的情况。

## Cookies

Before we leave these next steps。你可能会好奇如何使用cookie，首先你需要处在一个域名下，然后这样设置cookie:

```python
# Go to the correct domain
driver.get("http://example.com")
 
# Now set the cookie. This one's valid for the entire domain
cookie = {'name':'foo','value':'bar'}
driver.add_cookie(cookie)
 
# And now output all the available cookies for the current URL
driver.get_cookies()
```

 

# 五、元素定位

我们有许多方法对页面的元素进行定位，你可以根据自己的需要选择最合适的一种。Selenium提供了下面的方法进行元素定位： *find_element_by_id* find_element_by_name *find_element_by_xpath*find_element_by_link_text *find_element_by_partial_link_text* find_element_by_tag_name*find_element_by_class_name* find_element_by_css_selector

寻找多个元素（下列方法会返回一个list，其余使用方式相同）： *find_elements_by_name*find_elements_by_xpath *find_elements_by_link_text* find_elements_by_partial_link_text*find_elements_by_tag_name* find_elements_by_class_name * find_elements_by_css_selector

除了上面这些公有的方法，我们还有2个私有的方法来帮助页页面对象的定位。这两个方法就是`find_element`和`find_elements`:

```python
from selenium.webdriver.common.by import By
 
driver.find_element(By.XPATH,'//button[text()="Some Text"]')
driver.find_elements(By.XPATH,'//button')
```

`By`类的可用属性如下：

```python
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag_name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
```

## 根据Id定位

如果你知道元素的`id`属性，那么就使用id定位吧。在id定位里，会返回第一个id属性匹配的元素，如果没有元素匹配，会抛出`NoSuchElementException`异常。

举个例子，我们来看一个页面:

```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
<html>
```

我们可以这样定位表单元素form:

```
login_form = driver.find_element_by_id('loginForm')
```

## 根据 Name 定位

如果你知道元素的`name`属性，那么就用这个定位吧。在name定位里，会返回第一个name属性匹配的元素，如果没有元素匹配，会抛出`NoSuchElementException`异常。

举例我们再来看一个页面：

```html
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
<html>
```

username 和 password元素 可以这样定位：

```python
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
```

下面这个操作会返回Login按钮，因为它在Clear按钮的前面：

```python
continue = driver.find_element_by_name('continue')
```

### XPath定位

XPath是用来定位XML文档节点的语言。不过HTML可以看成是XML(XHTML)的一种实现。Selenium用户可以使用这个强力的语言来瞄准Web应用的元素。 XPath延伸了用id或者name属性来定位的单一方法，开创了许多可能性，例如定位页面的第三个复选框

用XPath的主要理由之一，就是你想定位的元素没有合适的id或者name属性的时候，你可以用XPath来对元素进行绝对定位(不推荐)或者把这个元素和另外一个有确定id或者name的元素关联起来（即相对定位）。XPath定位器也可以用来找出那些具有id,name以外属性的元素。

绝对的XPath定位包含了从HTML根节点起的所有元素，并且一些轻微的改变就会失效。而用id或者name属性来找到一个靠近的元素(比较理想的是父元素)，这样你就可以依靠他们的相对关系来确定目标元素的位置。这种情况改变的可能就小了很多了，我们写的测试程序也会更可靠。

再来看一个实例：

```python
<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
  </form>
</body>
<html>
```

form元素可以这样定位：

```python
login_form = driver.find_element_by_xpath("/html/body/form[1]")
login_form = driver.find_element_by_xpath("//form[1]")
login_form = driver.find_element_by_xpath("//form[@id='loginForm']")
```

(译者注:这里下标看起来应该是从1开始的)

1. 绝对路径（如果HTML有细微的改变就会失效）

2. HTML的第一个form元素

3. id属性为'loginForm'的form元素

username元素可以这样定位：

```python
username = driver.find_element_by_xpath("//from[input/@name='username']")
username = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
username = driver.find_element_by_xpath("//input[@name='username']")
```

1. 第一个form元素的 name属性是'username'的input子元素

2. id属性为'loginForm'的form元素的第一个input子元素

3. name属性为'username'的第一个input元素

'clear'按钮可以这样定位：

```html
clear_button = driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
clear_button = driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")
```

1. type属性为'button',name属性为'continue'的第一个input元素

2. id为'loginForm'的表单的第四个input子元素

这些例子只覆盖了一些基本的使用情况，如果想学习更具体的，推荐下面这些地方： [*W3School XPath Tutorial*](http://www.w3schools.com/xsl/xpath_intro.asp) [W3C XPath Recommendation](http://www.w3.org/TR/xpath) * [XPath Tutorial](http://www.zvon.org/comp/r/tut-XPath_1.html)

还有几个很有用的插件可以帮助我们测试： [*XPath Checker*](https://addons.mozilla.org/en-US/firefox/addon/1095?id=1095) *(Firefox**浏览器**)**提供**XPath**的建议，并且可以测试**XPath**的结果* [Firebug](https://addons.mozilla.org/en-US/firefox/addon/1843) 提供XPath的建议只是这个插件很有用的功能之一 * [XPath Helper](https://chrome.google.com/webstore/detail/hgimnogjllphhhkhlmebbmlgjoejdpjl)Google Chrome浏览器

## 用链接文本定位超链接

如果你知道一个锚标签使用了什么文本，那么就使用这种方法。在超链接定位里，会返回第一个文本属性匹配的链接，如果没有元素匹配，会抛出`NoSuchElementException`异常。

实例：

```html
<html>
 <body>
  <p>Are you sure you want to do this?</p>
  <a href="continue.html">Continue</a>
  <a href="cancel.html">Cancel</a>
</body>
<html>
```

可以这样定位 continue.html链接：

```
continue_link = driver.find_element_by_link_text('Continue')
continue_link = driver.find_element_by_partial_link_text('Conti')
```

(waiting注：`find_element_by_partial_link_text`使用的**应该**是子串匹配，只要输入自字符串即可匹配，读者最好自行测试)

## 标签名定位

知道元素标签名就使用这个定位，如果没有元素匹配，会抛出`NoSuchElementException`异常。

实例：

```html
<html>
 <body>
  <h1>Welcome</h1>
  <p>Site content goes here.</p>
</body>
<html>
```

可以这样定位标题元素(h1):

```python
heading1 = driver.find_element_by_tag_name('h1')
```

## class定位

知道class就使用这个定位，只返回匹配的第一个，无元素匹配，会抛出`NoSuchElementException`异常。

实例：

```html
<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
<html>
```

定位`p`元素:

```python
content = driver.find_element_by_class_name('content')
```

## css选择器定位

如果你能用css选择器的语法来表述一个元素，那么就选这个，只返回匹配的第一个，无元素匹配，会抛出`NoSuchElementException`异常。

实例：

```
<html>
 <body>
  <p class="content">Site content goes here.</p>
</body>
<html>
```

定位`p`元素：

```
content = driver.find_element_by_css_selector('p.content')
```

关于 CSS选择器，[Sauce 实验室有份很好的文档](http://saucelabs.com/resources/selenium/css-selectors)

 

# 六、等待事件

# Waits

现在很多Web应用都在使用AJAX技术。浏览器载入一个页面时，页面内的元素可能是在不同的时间载入的，这会加大定位元素的困难程度，因为元素不在DOM里，会抛出`ElementNotVisibleException`异常，使用`waits`，我们就可以解决这个问题。Waiting给(页面)动作的执行提供了一些时间间隔-通常是元素定位或者其他对元素的操作。

Selenium WebDriver提供了两类`waits`- 隐式和显式。显式的`waits`会让WebDriver在更深一步的执行前等待一个确定的条件触发，隐式的`waits`则会让WebDriver试图定位元素的时候对DOM进行指定次数的轮询。

## 显式Waits

显式的`waits`等待一个确定的条件触发然后才进行更深一步的执行。最糟糕的的做法是`time.sleep()`，这指定的条件是等待一个指定的时间段。 这里提供一些便利的方法让你编写的代码只等待需要的时间，`WebDriverWait`结合`ExpectedCondition`是一种实现的方法：

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
driver = webdriver.Firefox()
driver.get("http://somedomain/url_that_delay_loading")
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"myDynamicElement"))
    )
finally:
    driver.quit()
```

这段代码会等待10秒，如果10秒内找到元素则立即返回，否则会抛出`TimeoutException`异常，WebDriverWait默认每500毫秒调用一下`ExpectedCondition`直到它返回成功为止。`ExpectedCondition`类型是布尔的，成功的返回值就是true,其他类型的`ExpectedCondition`成功的返回值就是 `not null`

详细的`ExpectedCondition`可以参看 [7.6 浏览器驱动](https://github.com/StephinChou/seleniumDocument/blob/master/7.6 浏览器驱动.md)

### 预期条件

自动化网页操作时，有许多频繁使用到的通用条件。下面列出的是每一个条件的实现。Selenium + Python 提供了许多方便的方法，因此你不需要自己编写`expected_condition`的类，或者创建你自己的通用包。
```
·     title_is

·     title_contains

·     presence_of_element_located

·     visibility_of_element_located

·     visibility_of

·     presence_of_all_elements_located

·     text_to_be_present_in_element

·     text_to_be_present_in_element_value

·     frame_to_be_available_and_switch_to_it

·     invisibility_of_element_located

·     element_to_be_clickable - 元素展示并且可用

·     staleness_of

·     element_to_be_selected

·     element_located_to_be_selected

·     element_selection_state_to_be

·     element_located_selection_state_to_be

·     alert_is_present
```

```python
from selenium.webdriver.support import expected_conditions as EC
 
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))
```

`expected_conditions`模块包含了一系列预定义的条件来和WebDriverWait使用

## 隐式Waits

当我们要找一个或者一些不能立即可用的元素的时候，隐式`waits`会告诉WebDriver轮询DOM指定的次数，默认设置是0次。一旦设定，WebDriver对象实例的整个生命周期的隐式调用也就设定好了。

```python
from selenium import webdriver
 
driver = webdriver.Firefox()
driver.implicitly_wait(10) # seconds
driver.get("http://somedomain/url_that_delays_loading")
myDynamicElement = driver.find_element_by_id('myDynamicElement')
```

以下根据stackoverflow网友回答添加：[原问题链接](http://stackoverflow.com/questions/10404160/when-to-use-explicit-wait-vs-implicit-wait-in-selenium-webdriver) 推荐一直用显式的，忘记还有隐式吧(Always use explicit wait. Forget that implicit wait exists)

显示waits: *明确的行为表现* 在本地的selenium运行(你选择的编程语言) *可以在任何你能想到的条件下工作* 返回成功或者超时 *可以定义元素的缺失为条件* 可以定制重试间隔，可以忽略某些异常

隐式waits: *不明确的行为表现，同一个问题依赖于不同的操作系统，不同的浏览器，不同的**selenium**版本会有各种不同的表现* 在远程的selenium上运行(控制浏览器的那部分). *只能在寻找元素的函数上工作* 返回找到元素或者（在超时以后）没有找到 *如果检查元素缺失那么总是会等待到超时* 除了时间啥都不能指定

# 七、.页面对象

这章是对 页面对象设计模型的特别指导。一个页面对象代表了你要测试的用户接口交互的区域。

使用页面对象模型的好处： *可以写出能在多个测试案例里复用的代码* 减少重复代码 * 如果用户接口更改，只需要在一个地方做相应修改即可

## 测试案例

下面这个测试案例测试了在`python.org`网页上搜索一个单词并确认有相应的搜索结果：

```python
import unittest
from selenium import webdriver
import page
 
class PythonOrgSearch(unittest.TestCase):
    """一个简单展示页面对象如何工作的类"""
 
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")
 
    def test_search_in_python_org(self):
        """
        测试 python.org网站的搜索功能。搜索一个单词“pycon”然后验证某些结果会展示出来。
        注意这个测试不会在搜索结果页里寻找任何细节文本，它只会验证结果为非空
        """
 
        #载入主页面，这个例子里是 Python.org的首页
        main_page = page.MainPage(self.driver)
        #检查页面的标题是否包含"python"单词
        assert main_page.is_title_matches(), "python.org title doesn't match."
        #将搜索框的文本设置为"pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #验证结果页非空
            assert search_results_page.is_results_found(), "No results found."
 
    def tearDown(self):
        self.driver.close()
 
if __name__ == "__main__":
    unittest.main()
```

## 页面对象类

页面对象模型旨在给每一个Web页面创造一个对象。运用这个技术我们可以在测试代码和技术实现之间创建一个分离层，`page.py`会是这样的：

```python
from element import BasePageElement
from locators import MainPageLocators
 
class SearchTextElement(BasePageElement):
    """这个类从指定的定位器里获取到搜索文本"""
 
    #已经输入搜索字符串的搜索框的定位器
    locator = 'q'
 
 
class BasePage(object):
    """初始化所有页面都会调用的基本页类"""
 
    def __init__(self, driver):
        self.driver = driver
 
 
class MainPage(BasePage):
    """主页操作方法放这里"""
 
    #定义一个变量存放检索文本
    search_text_element = SearchTextElement()
 
    def is_title_matches(self):
        """验证硬编码字符"python"出现在页面标题里"""
        return "Python" in self.driver.title
 
    def click_go_button(self):
        """触发搜索功能"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
 
 
class SearchResultsPage(BasePage):
    """搜索结果页操作方法放这里"""
 
    def is_results_found(self):
        # 或许应该在具体的页面元素里搜索文本，不过目前为止这样运行没什么问题
        return "No results found." not in self.driver.page_source
```

## 页面元素

`element.py`类大致是这样的：

```python
from selenium.webdriver.support.ui import WebDriverWait
 
 
class BasePageElement(object):
    """初始化每个页面对象类的基本页类"""
 
    def __set__(self, obj, value):
        """用给定的值设置文本"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).send_keys(value)
 
    def __get__(self, obj, owner):
        """从具体的对象里获取文本"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
```

## 定位器

One of the practices is to separate the locator strings from the place where they are being used.在这个例子里，同页面的定位器是同一个类

The locators.py will look like this:

```
from selenium.webdriver.common.by import By
 
class MainPageLocators(object):
    """一个主页面定位器类，所有的页面定位器应该来自这里"""
    GO_BUTTON = (By.ID, 'submit')
 
class SearchResultsPageLocators(object):
    """一个搜索结果定位器类，所有搜索结果定位器应该来自这里"""
    pass
```

 

# 八、异常

所有的页面驱动代码里都可能抛出异常。

exception selenium.common.exceptions.ElementNotSelectableException(msg=None,screen=None,stacktrace=None)

基于 `selenium.common.exceptions.InvalidElementStateException`

当试图选中一个不能选中的元素时抛出 例如，选中一个`script`元素

exception selenium.common.exceptions.ElementNotVisibleException(msg=None,screen=None,stacktrace=None)

基于 `selenium.common.exceptions.InvalidElementStateException`

当DOM上存在元素但是不可用时，它是不可以进行交互的

最常见的场景是试图点击或者阅读一个隐藏的元素

exception selenium.common.exceptions.ErrorInResponseException(response,msg)

基于 `selenium.common.exception.WebDriverException`

服务端发生错误

这个异常可能会在 和 firefox扩展或者 远程驱动服务交互时产生

exception selenium.common.exceptions.ImeActivationFailedException(msg=None,screen=None,stacktrace=None)

基于 `selenium.common.exceptions.WebDriverException`

激活一个 IME引擎失败

exception selenium.common.exceptions.ImeNotAvailableException(msg=None,screen=None,stacktrace=None)

基于 `selenium.common.exceptions.WebDriverException`

IME支持不可用。 如果 机器上IME支持不可用，这个异常会在所有和IME相关的方法里抛出

exception selenium.common.exceptions.InvalidCookieDomainException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

试图在一个和当前不同的域名下添加cookie

exception selenium.common.exceptions.InvalidElementStateException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

exception selenium.common.exceptions.InvalidSelectorException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.NoSuchElementException`

选择器用来寻找元素，但返回的不是一个 WebElement时。 目前只会在XPath表达式选择器里产生，XPath表达式语法错误或者没有选择WebElement时(例:`count(//input)`)

exception selenium.common.exceptions.InvalidSwitchToTargetException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

要切换的窗口或者框架不存在时

exception selenium.common.exceptions.MoveTargetOutOfBoundsException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

提供给`ActionsChains` move()方法的 目标不可用。

exception selenium.common.exceptions.NoAlertPresentException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

屏幕没有警告框时，切换到警告框

exception selenium.common.exceptions.NoSuchAttributeException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

元素找不到这个属性。

你可能会想在另外一个浏览器上检查某个属性是否存在，有些浏览器相同的属性有不同的属性名（IE8的 innerText和 Firefox的 textContent）

exception selenium.common.exceptions.NoSuchElementException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

找不到元素

如果你发现这个错误，你可能会想要检查下面的东西: *检查你*`*find_by...*`*函数里用的选择器* 查找元素的时候页面上还没有这个元素

（页面正在加载）请查阅`selenium.webdriver.support.wait.WebDriverWait()`来了解如何等待元素的出现

exception selenium.common.exceptions.NoSuchFrameException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.InvalidSwitchToTargetException`

要切换的目标框架不存在

exception selenium.common.exceptions.NoSuchWindowException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.InvalidSwitchToTargetException`

要切换的目标窗口不存在。

要找到当前活动窗口的句柄，你可以用下面的方法来获取一个句柄列表：

```python
print driver.window_handles
```

exception selenium.common.exceptions.RemoteDriverServerException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

exception selenium.common.exceptions.StaleElementReferenceException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

当一个元素的引用`变旧`

变旧的意思是这个元素不在出现在页面的DOM里

可能出现这个异常的原因包括但不限于： *你不在同一个页面，或者你获取到元素之后页面被刷新了*元素被定位后 被移动了又重新加到屏幕上，这样元素就被重置了。典型的例子是javascript框架当值改变，节点就被重建了 * 元素所在的框架或者其他内容被刷新了

exception selenium.common.exceptions.TimeoutException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

规定时间内一个命令没有执行完

exception selenium.common.exceptions.UnableToSetCookieException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

驱动设置cookie失败

exception selenium.common.exceptions.UnexpectedAlertPresentException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

预料之外的警告框。当一个警告框阻塞了webdriver，不能执行任何命令的时候。

exception selenium.common.exceptions.UnexpectedTagNameException(msg=None, screen=None, stacktrace=None)

基于：`selenium.common.exceptions.WebDriverException`

当一个支持的类没有拿到预料的web元素时

exception selenium.common.exceptions.WebDriverException(msg=None, screen=None, stacktrace=None)

基于：`exceptions.Exception`

基本的 webdriver 异常

# 九、行为链

class selenium.webdriver.common.action_chains.ActionChains(driver)

`ActionChains`可以完成简单的交互行为，例如鼠标移动，鼠标点击事件，键盘输入，以及内容菜单交互。这对于模拟那些复杂的类似于鼠标悬停和拖拽行为很有用

产生用户行为

当你在`ActionChains`对象上调用行为方法时，这些行为会存储在`ActionChains`对象的一个队列里。调用`perform()`时，这些动作就以他们队列的顺序来触发

`ActionChains`可以使用链式模型:

```
menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")
 
ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
```

或者也可以一个个排队，然后执行：

```
menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")
 
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
action.perform()
```

不管怎样，这些动作总是一个接一个按他们被调用的顺序执行。

click(on_element=None)

点击一个元素

参数： * on_element:要点击的元素，如果是`None`，点击鼠标当前的位置

click_and_hold(on_element=None)

鼠标左键点击一个元素并且保持

参数： * on_element:同click()类似

double_click(on_element=None)

双击一个元素

参数： * on_element:同click()类似

drag_and_drop(source, target)

鼠标左键点击`source`元素，然后移动到`target`元素释放鼠标按键

参数： *source:**鼠标点击的元素* target:鼠标松开的元素

drag_and_drop_by_offset(source, xoffset,yoffset)

拖拽目标元素到指定的偏移点释放

参数: *source:**点击的参数* xoffset:X偏移量 * yoffset:Y偏移量

key_down(value,element=None)

只按下键盘，不释放。我们应该只对那些功能键使用(Contril,Alt,Shift)

参数： *value**：要发送的键，值在*`*Keys*`*类里有定义* element:发送的目标元素，如果是`None`，value会发到当前聚焦的元素上

例如，我们要按下 ctrl+c:

```
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
```

key_up(value,element=None)

释放键。参考key_down的解释

move_by_offset(xoffset,yoffset)

将当前鼠标的位置进行移动

参数： *xoffset:**要移动的**X**偏移量，可以是正也可以是负* yoffset:要移动的Y偏移量，可以是正也可以是负

move_to_element(to_element)

把鼠标移到一个元素的中间

参数： * to_element:目标元素

move_to_element_with_offset(to_element,xoffset,yoffset)

鼠标移动到元素的指定位置，偏移量以元素的左上角为基准

参数： *to_element:**目标元素* xoffset:要移动的X偏移量 * yoffset:要移动的Y偏移量

perform()

执行所有存储的动作

release(on_element=None)

释放一个元素上的鼠标按键，

参数： * on_element:如果为`None`,在当前鼠标位置上释放

send_keys(*keys_to_send)

向当前的焦点元素发送键

参数: * keys_to_send:要发送的键，修饰键可以到`Keys`类里找到

send_keys_to_element(element,*keys_to_send)

向指定的元素发送键

 

# 十、警告框

class selenium.webdriver.common.alert.Alert(driver)

允许对警告框进行操作

使用这个类和警告提醒框进行交互，这个类包含了 忽略、接受、输入 以及从提示框内获取文本的方法

接受和忽略弹框：

```
Alert(driver).accept()
Alert(driver).dismiss()
```

prompt里输入字符:

```
name_prompt = Alert(driver)
name_prompt.send_keys("Willian Shakephere")
name_prompt.accept()
```

读取prompt的提示字符：

```
alert_text = Alert(driver).text
self.assertEqual("Do you wish to quit?"，alert_text)
```

accept()

确认提示框，用法：

```
Alert(driver).accept() #Confirm a alert dialog
```

authenticate(username,password)

向一个认证的对话框发送用户名和密码，会自动点击确认：

```
driver.switch_to.alert.authenticate('cheese','secretGouda')
```

参数： *username:username**区域要填写的字符串* password:password区域要填写的字符串

dismiss()

忽略提示框

send_keys(KeysToSend)

向对话框输入字符

text

提示框的文本

# 十一、特殊字符

class selenium.webdriver.common.keys.Keys

下面是一些特殊字符的代码：
```
ADD = u'\ue025'

ALT = u'\ue00a'

ARROW_DOWN = u'\ue015'

ARROW_LEFT = u'\ue012'

ARROW_RIGHT = u'\ue014'

ARROW_UP = u'\ue013'

BACKSPACE = u'\ue003'

BACK_SPACE = u'\ue003'

CANCEL = u'\ue001'

CLEAR = u'\ue005'

COMMAND = u'\ue03d'

CONTROL = u'\ue009'

DECIMAL = u'\ue028'

DELETE = u'\ue017'

DIVIDE = u'\ue029'

DOWN = u'\ue015'

END = u'\ue010'

ENTER = u'\ue007'

EQUALS = u'\ue019'

ESCAPE = u'\ue00c'

F1 = u'\ue031'

F10 = u'\ue03a'

F11 = u'\ue03b'

F12 = u'\ue03c'

F2 = u'\ue032'

F3 = u'\ue033'

F4 = u'\ue034'

F5 = u'\ue035'

F6 = u'\ue036'

F7 = u'\ue037'

F8 = u'\ue038'

F9 = u'\ue039'

HELP = u'\ue002'

HOME = u'\ue011'

INSERT = u'\ue016'

LEFT = u'\ue012'

LEFT_ALT = u'\ue00a'

LEFT_CONTROL = u'\ue009'

LEFT_SHIFT = u'\ue008'

META = u'\ue03d'

MULTIPLY = u'\ue024'

NULL = u'\ue000'

NUMPAD0 = u'\ue01a'

NUMPAD1 = u'\ue01b'

NUMPAD2 = u'\ue01c'

NUMPAD3 = u'\ue01d'

NUMPAD4 = u'\ue01e'

NUMPAD5 = u'\ue01f'

NUMPAD6 = u'\ue020'

NUMPAD7 = u'\ue021'

NUMPAD8 = u'\ue022'

NUMPAD9 = u'\ue023'

PAGE_DOWN = u'\ue00f'

PAGE_UP = u'\ue00e'

PAUSE = u'\ue00b'

RETURN = u'\ue006'

RIGHT = u'\ue014'

SEMICOLON = u'\ue018'

SEPARATOR = u'\ue026'

SHIFT = u'\ue008'

SPACE = u'\ue00d'

SUBTRACT = u'\ue027'

TAB = u'\ue004'

UP = u'\ue013'
```

# 十二、用By类定位

许多属性都可以用来定位元素，参看 (4.元素定位)查看更多实例

class selenium.webdriver.common.by.By

支持的定位策略：
```

classmethod is_valid(by)

CLASS_NAME = 'class name'

CSS_SELECTOR = 'css selector'

ID = 'id'

LINK_TEXT = 'link text'

NAME = 'name'

PARTIAL_LINK_TEXT = 'partial link text'

TAG_NAME = 'tag name'

XPATH = 'xpath'
```

# 期望的功能

请到 [2.开始](https://python-selenium-zh.readthedocs.io/zh_CN/latest/7.5 By-期望的功能-实用工具/) 查看期望功能的实例

class selenium.webdriver.common.desired_capabilities.DesiredCapabilities

默认支持的期望功能的集合

在请求远程Web驱动连接selenium server 或者selenium grid时，首先一点要先创建一个期望功能的对象，请看实例：

```python
from selenium import webdriver
selenium_grid_url = "http://198.0.0.1:4444/wd/hub"
 
# Create a desired capabilities object as a start point.
capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['platform'] = "WINDOWS"
capabilities['version'] = "10"
 
# Instantiate an instance of Remote WebDriver with the desired capabilities.
driver = webdriver.Remote(
    desired_capabilities=capabilities,
    command_executor=selenium_grid_url)
```

**注意**，请记得使用在DesiredCapabilities上使用`.copy()`，避免变更全局类实例带来的副作用

ANDROID = {'platform': 'ANDROID', 'browserName': 'android', 'version': '', 'javascriptEnabled': True}

CHROME = {'platform': 'ANY', 'browserName': 'chrome', 'version': '', 'javascriptEnabled': True}

EDGE = {'platform': 'WINDOWS', 'browserName': 'MicrosoftEdge', 'version': ''}

FIREFOX = {'platform': 'ANY', 'browserName': 'firefox', 'version': '', 'marionette': False, 'javascriptEnabled': True}

HTMLUNIT = {'platform': 'ANY', 'browserName': 'htmlunit', 'version': ''}

HTMLUNITWITHJS = {'platform': 'ANY', 'browserName': 'htmlunit', 'version': 'firefox', 'javascriptEnabled': True}

INTERNETEXPLORER = {'platform': 'WINDOWS', 'browserName': 'internet explorer', 'version': '', 'javascriptEnabled': True}

IPAD = {'platform': 'MAC', 'browserName': 'iPad', 'version': '', 'javascriptEnabled': True}

IPHONE = {'platform': 'MAC', 'browserName': 'iPhone', 'version': '', 'javascriptEnabled': True}

OPERA = {'platform': 'ANY', 'browserName': 'opera', 'version': '', 'javascriptEnabled': True}

PHANTOMJS = {'platform': 'ANY', 'browserName': 'phantomjs', 'version': '', 'javascriptEnabled': True}

SAFARI = {'platform': 'ANY', 'browserName': 'safari', 'version': '', 'javascriptEnabled': True}

# 实用工具

一些`Utils`方法。

selenium.webdriver.common.utils.free_port()

用socket开放一个空闲的端口

selenium.webdriver.common.utils.is_connectable(port)

试图连接服务器上的端口看看是否可用

selenium.webdriver.common.utils.is_url_connectable(port)

试图连接一个HTTP服务器的指定端口，看是否成功返回

# 十三、浏览器驱动

# Firefox WebDriver

class selenium.webdriver.firefox.webdriver.WebDriver(firefox_profile=None, firefox_binary=None, timeout=30, capabilities=None, proxy=None, executable_path='wires')

quit()

退出驱动，关闭所有关联的窗口

NATIVE_EVENTS_ALLOWED = True

firefox_profile

# Chrome WebDriver

class selenium.webdriver.chrome.webdriver.WebDriver(executable_path='chromedriver', port=0, chrome_options=None, service_args=None, desired_capabilities=None, service_log_path=None)

控制 ChromeDriver 并且允许你驱动浏览器

你需要先下载ChromeDriver的[可执行驱动](http://chromedriver.storage.googleapis.com/index.html)

create_options()

launch_app(id)

以特定的id 启动 Chrome

quit()

关闭浏览器，关闭开始时启动的ChromeDriver

# Remote WebDriver

class selenium.webdriver.remote.webdriver.WebDriver(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=None, browser_profile=None, proxy=None, keep_alive=False)

通过对远程服务器发送命令来控制浏览器。远程的服务器需要运行[这里](https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol)定义的WebDriver wire 协议

属性： *session_id - WebDriver**控制，浏览器会话产生的一个**String ID* capabilities - 返回浏览器会话的可用功能dict，有关远程服务区，请看https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities *command_executor - remote_connection.RemoteConnection* *对象，用来执行命令* error_handler - errorhandler.ErrorHandler对象，捕获错误

add_cookie(cookie_dict) - 给当前会话加cookie

参数： * cookie_dict:dict对象，需要指定键`name`和`value`，可选的键有:`path`,`domain`,`secure`,`expiry`

用法：

```python
driver.add_cookie({'name':'foo','value':'bar'})
driver.add_cookie({'name':'foo','value':'bar','path':'/'})
driver.add_cookie({'name':'foo','value':'bar','path':'/','secure':True})
```

back() - 在浏览历史中回退一步

例：

```python
driver.back()
```

close() - 关闭当前窗口

例：

```python
driver.close()
```

create_web_element(element_id) - 以指定的元素id创建一个新web元素

delete_all_cookies() - 删除当前会话的所有cookie

例：

```python
driver.delete_all_cookies()
```

delete_cookie(name) - 删除一个指定的cookie

例：

```python
driver.delete_cookie('my_cookie')
```

execute(driver_command, params=None)

给 command.CommandExecutor 发送一个要执行的命令

参数： *driver_command:**要执行的命令名（字符串）* params:命令的参数dict

返回：命令的JSON返回会加载到一个dict对象

execute_async_script(script,*args)

在当前的窗口/框架里异步执行Javascript

参数： *script:**要执行的**js* *args:js的任意合适的参数

例：

```python
driver.execute_async_script('document.title')
```

（这样也算一个例子？参数呢？）

(find_element_*方法，自行参看[原文档](http://selenium-python.readthedocs.org/api.html#module-selenium.webdriver.remote.webdriver))

forward() - 浏览历史里前进一步

get(url) - 用当前的浏览器session加载一个web页面

get_cookie(name) - 返回一个指定的cookie，不存在返回`None`

get_cookies() - 返回一组dict,相当于当前会话的可用cookie

get_log(log_type) - 获取指定类型的日志

例：

```python
driver.get_log('browser')
driver.get_log('driver')
driver.get_log('client')
driver.get_log('server')
```

get_screenshot_as_base64() - 获取当前页面的截图的base64编码字符串，当页面嵌入了图片时这个方法很有用。

get_screenshot_as_file(filename) - 获取当前页面截图，如果有任何 IOError则返回False,正常返回True,文件名记得使用完整的路径

例：

```python
driver.get_screenshot_as_file('/Screenshots/foo.png/')
```

get_screenshot_as_png - 获取当前窗口截图的二进制数据

get_window_position(windowHandle='current') - 获取当前窗口的x,y位置

get_window_size(windowHandle='current') - 获取当前窗口的宽高(width,height)

implicitly_wait(time_to_wait) - 设置一个隐式的等待时间，等待一个元素被发现或者一个命令的完成。

在每次会话里，这个方法只需要被调用一次。超时后要调用 `execute_async_script`，请参看 `set_script_timeout`

例：

```python
driver.implicitly_wait(30)
```

maximize_window() - 将webdriver正在使用的窗口最大化

quit() 退出驱动并关闭所有关联窗口

refresh() - 刷新当前页面

set_page_load_timeout(time_to_wait) - 给载入页面设置一个超时时间，在抛出错误之前会等待到加载完成

set_script_timeout(time_to_wait) - 在一个 `execute_async_script`调用期间，设置脚本等待的时间

set_window_position(x,y,windowHandle='current') - 给页面设置x,y位置

set_window_size(width,height,windowHandle='current') - 给页面设置宽高

start_client() - 在新会话开启之前调用，这个方法可以重载来定制启动行为

start_session(desired_capabilities, browser_profile=None) - 以期望的性能来创建一个新会话

参数： *browser_name -* *要请求的浏览器的名字* version - 要请求的浏览器版本 *platform -* *浏览器平台*javascript_enabled - 新会话是否支持js * browser_profile - 仅在请求Firefox浏览器时使用，selenium.webdriver.firefox.firefox_profile.FirefoxProfile 对象对象

stop_client() - 执行一个退出命令时调用。这个方法可以重写，自己定制关闭时的行为

switch_to_active_element() - 不推荐使用 driver.switch_to.active_element

switch_to_alert() - 不推荐使用 driver.switch_to.alert

switch_to_default_content() - 不推荐使用 driver.switch_to.default_content

switch_to_frame(frame_reference) - 不推荐使用 driver.switch_to.frame

switch_to_window(window_name) - 不推荐使用 driver.switch_to.window

application_cache - 返回一个 ApplicationCache 对象 来和 浏览器应用缓存交互

current_url - 当前页的url

current_window_handle - 当前窗口的句柄

desired_capabilities - 返回当前驱动正在使用的 '期望性能'

file_detector

log_types - 返回可用的日志类型list

mobile

name - 返回当前实例的底层浏览器名

orientation - 获取当前设备的适应情况

page_source - 获取当前页面的来源

switch_to

title - 当前页面的标题

window_handles - 返回当前会话内所有窗口的资源句柄

# 页面元素

class selenium.webdriver.remote.webelement.WebElement(parent,id_,w3c=False)

代表一个DOM元素。通常所有和文档互动的有趣操作都要通过这个接口执行。

所有的方法调用都会做一个 '新鲜检查' 来确认引用的元素仍然可用,这本质上确定了这个元素是否还与DOM相连。如果检测失败，会抛出 `StaleEleementReferenceException`异常，并且下面的所有对这个接口的调用都会失败

(拥有find_element_by_*所有方法，请参看[此处](http://selenium-python.readthedocs.org/api.html#module-selenium.webdriver.remote.webelement))

get_attribute(name) - 返回元素指定的属性

这个方法首先会尝试返回元素指定的属性，如果属性不存在，它会返回和属性名相同的字符串，如果没有属性是这个名字，返回`None`。 被认为是真假的值会返回布尔类型，其他所有的非`None`值都会以字符串的形式返回。属性不存在，返回`None`

例：

```python
# Check if the "active" CSS class is applied to en element
is_active = "active" in target_element.get_attribute("class")
```

is_displayed() - 元素对用户是否可见

is_enabled() - 元素是否可用

is_selected() - 元素是否被选中,可用来检测单选或者复选按钮是否被选中

screenshot(filename) - 获取当前元素的截图，有IOError会返回`False`,文件名要包含完整路径

send_keys(*value) - 模拟向元素输入

使用这个方法发送简单的按键时间或者填充表单字段：

```python
form_textfiled = driver.find_element_by_name("username")
form_textfiled.send_keys("admin")
```

这个方法还可以用来设置文件：

```python
file_input = driver.find_element_by_name('profilePic')
file_input.send_keys('path/to/profilepic.gif')
```

submit() - 提交表单

value_of_css_property(property_name) - CSS属性的值

id - selenium使用的内部ID

这个主要是内部使用，简单的使用案例是用来做类似于检测两个元素是否关联到相同的元素上，可以用`==`来比较：

```python
if element1 == element2:
    print("These 2 are equal")
```

location - 元素在可渲染的画布上的位置

location_once_scrolled_into_view

*这个属性改变不会发出警告*，用这个来检查元素在屏幕的位置以方便我们点击它，这个方法可能造成元素滚动到视图里。 返回屏幕左上角的位置，元素不可见返回`None`

parent - WebDriver实例的内部引用，元素是从哪里发现的

rect - 元素尺寸和位置的dict

screenshot_as_base64 - 当前元素截图的base64编码字符串

screenshot_as_png - 当前元素截图的二进制数据

size - 元素的尺寸

tag_name - 元素的标签名

text - 元素的文本

# UI支持

class selenium.webdriver.support.select.Select(webelement)

deselect_all() - 清除所有的选中输入。仅当选择项支持多选的时候可用，如果不支持多选会抛出`NotImplementedError`。

deselect_by_index(index) - 取消指定索引的选项的选中。这个方法会检查`index`属性，而不仅仅是计数

deselect_by_value(value) - 取消所有选项的值匹配的选中状态。

意思就是，当给出一个'foo'值时，会取消选中一个类似这样的选项：

```html
<option value="foo">Bar</option>
```

deselect_by_visible_text(text) - 取消选中所有文本匹配的选项

给出'Bar'时，匹配：

```html
<option value="foo">Bar</option>
```

select_by_index(index)

select_by_value(value)

select_by_visible_text(text)

上述三个和取消选中用法一样，操作由取选变成选中

all_selected_options - 返回这个选择标签的所有选中选项list

first_selected_option - 选择标签的的第一个选中项(或者一个正常选择框的当前选中项)

options - 选择标签的所有选项list

class selenium.webdriver.support.wait.WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)

until(method, message='')

调用驱动提供的方法名当参数，直到方法返回值 不是 `False`

until_not(method, message='')

调用驱动提供的方法名当参数，直到方法返回值 是 `False`

# 颜色支持

class selenium.webdriver.support.color.Color(red,green,blue,alpha=1)

颜色变换支持类：

```python
from selenium.webdriver.support.color import Color
 
print(Color.from_string('#00fff33').rgba)
print(Color.from_string('rgb(1,255,3)').hex)
print(Color.from_string('blue').rgba)
```

*static* from_string(*str*)

hex

rgb

rgba

# 预期条件支持

*class* selenium.webdriver.support.expected_conditions.alert_is_present

预期出现一个弹框

*class*selenium.webdriver.support.expected_conditions.element_located_selection_state_to_be(*locator, is_selected*)

预期定位一个元素并且检查选中状态是否符合预期，`locator`是一个(by,path)的tuple，`is_selected`是布尔值

*class* selenium.webdriver.support.expected_conditions.element_located_to_be_selected(*locator*)

预期一个定位的元素是选中的

*class*selenium.webdriver.support.expected_conditions.element_selection_state_to_be(*element,is_selected*)

预期元素是否选中

*class* selenium.webdriver.support.expected_conditions.element_to_be_clickable(locator)

预期一个元素是否可见可用，以便可以点击它

*class* selenium.webdriver.support.expected_conditions.element_to_be_selected(element)

预期一个元素是选中的

*class*selenium.webdriver.support.expected_conditions.frame_to_be_available_and_switch_to_it(locator)

检查框架是否可以被切换，如果可以，那么就切换到这个框架

*class* selenium.webdriver.support.expected_conditions.invisibility_of_element_locator(locator)

预期元素不可见或者不在DOM上，`locator`定位元素

*class* selenium.webdriver.support.expected_conditions.presence_of_all_elements_located(locator)

预期至少有一个元素出现在web页面上，`locator`是用来寻找已经被定位了的WebElements list

*class* selenium.webdriver.support.expected_conditions.presence_of_element_located(locator)

预期元素正在页面的DOM上，这不意味着元素是可见的。

*class* selenium.webdriver.support.expected_conditions.staleness_of(element)

等待元素不再附在DOM上，`element`是要等待的元素，如果元素仍然在DOM上返回`False`,否则返回`True`

*class* selenium.webdriver.support.expected_conditions.text_to_be_present_in_element(*locator, text_*)

预期给定的文本会出现在指定的元素上

*class*selenium.webdriver.support.expected_conditions.text_to_be_present_in_element_value(*locator, text_*)

预期给定的文本会出现在指定的元素的value上

*class* selenium.webdriver.support.expected_conditions.title_contains(*title*)

预期标题包含一个指定的字符串（大小写敏感），匹配返回True，否则返回False

*class* selenium.webdriver.support.expected_conditions.title_is(*title*)

预期标题完全匹配一个字符串

*class* selenium.webdriver.support.expected_conditions.visibility_of(*element*)

预期已经在DOM上的一个元素是可见的。可见不仅仅表示元素是显示的，而且长宽都要大于0.参数_element_是一个`WebElement`。如果元素可见，则返回这个元素对象

*class* selenium.webdriver.support.expected_conditions.visibility_of_element_located(*locator*)

和`visibility_of`类似，不同的是通过一个定位器来定位元素。如果元素被定位到并且可见，则返回这个元素对象

# 十四、WebDriver API

注意，这不是官方文档，官方的API文档在[这里](http://selenium.googlecode.com/svn/trunk/docs/api/py/index.html)

这一章涵盖了所有的Selenium WebDriver接口。

### 推荐的引入风格

这一章里面API的定义已经展示了类的绝对位置，不过推荐使用下面引入风格：

```python
from selenium import webdriver
```

然后你就可以这样使用这个类：

```python
webdriver.Firefox
webdriver.FirefoxProfile
webdriver.Chrome
webdriver.ChromeOptions
webdriver.Ie
webdriver.Opera
webdriver.Phantomjs
webdriver.Remote
webdriver.DesiredCapabilities
webdriver.ActionChains
webdriver.TouchActions
webdriver.Proxy
```

特殊的键盘类（`Keys`）可以这样引入：

```python
from selenium.webdriver.common.keys import Keys
```

引入`exception`类（把`TheNameOfTheExceptionClass`替换为你真正需要的类名）：

```python
from selenium.common.exceptions import [TheNameOfTheExceptionClass]
```

### API的常规使用

一些属性(或者方法)是可以调用的，另外一些不可以调用，可以调用的属性是以圆括号结尾的。

下面是属性的一个例子： * current_url 当前载入页面的URL

使用：

```python
driver.current_url
```

下面是方法的一个例子 * close()

关闭当前窗口 使用：

```python
driver.close()
```

# 十五、附录：FAQ

另外一份FAQ:https://code.google.com/p/selenium/wiki/FrequentlyAskedQuestions

## 怎样使用 ChromeDriver

下载最新的[chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads),解压文件：

```shell
unzip chromedriver_linux32_x.x.x.x.zip
```

你应该会看到一个可执行的`chromedriver`，现在你可以像这样创建一个Chrome Driver的实例了：

```
driver - webdriver.Chrome(executable_path="/path/to/chromedriver")
```

使用例子的剩余部分在其他文档里已经给出了

## Selenium 2 支持 XPath 2.0 吗？

相关链接： http://seleniumhq.org/docs/03_webdriver.html#how-xpath-works-in-webdriver

Selenium 委托 XPath 去查询浏览器自己的XPath引擎，因此浏览器支持什么XPath，Selenium就支持什么。在不支持XPath引擎的浏览器里（IE 6，7，8）,Selenium仅支持 XPath 1.0

## 怎么滚动到页面的底部？

相关链接：http://blog.varunin.com/2011/08/scrolling-on-pages-using-selenium.html

你可以使用`execute_script`方法来在载入的页面上执行JS，因此，你可以调用JS的API来滚动到页面的底部或者其他任意位置。

下面是一个滚动到底部的实例：

```python
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
```

DOM的窗口对象有一个 [scrollTo](http://www.w3schools.com/jsref/met_win_scrollto.asp) 方法来在打开的窗口中滚动到任意位置， [scrollHeight](http://www.w3schools.com/jsref/dom_obj_all.asp)是所有元素的一个通用属性，`document.body.scrollHeight`是页面整个`body`的高度

## 怎样使用定制的 Firefox profile自动保存文件

相关链接：http://stackoverflow.com/questions/1176348/access-to-file-download-dialog-in-firefox

http://blog.codecentric.de/en/2010/07/file-downloads-with-selenium-mission-impossible/

第一步：确定你想要自己保存的文件类型。要确认你想自动下载的内容类型，你可以使用 [curl](http://curl.haxx.se/):

```
curl -I URL|grep "Content-Type"
```

另外一个找出内容类型的方法是使用 [requests模块](http://python-requests.org/):

```python
import requests
content_type = requests.head('http://www.python.org').headers['content-type']
print(content_type)
```

一旦你确定了内容类型，你就可以设置 firefox profile相关：`browser.helperApps.neverAsk.saveToDisk`

下面是一个实例：

```python
import os
 
from selenium import webdriver
 
fp = webdriver.FirefoxProfile()
 
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir",os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")
 
browser = webdriver.Firefox(firefox_profile=fp)
browser.get("http://pypi.python.org/pypi/selenium")
browser.find_element_by_partial_link_text("selenium-2").click()
```

上面的例子中，我们用了`application/octet-stream`这个内容类型，`browser.download.dir`指定了你想要保存下载文件的路径

## 怎么向文件上传表单上传文件？

选中``元素，调用`send_keys()`方法，传递文件的路径。可以传递绝对路径或者相对测试脚本的路径。要注意windows和Unix系统路径名的差异

## 如何使用firebug？

首先下载Firebug XPI 文件，然后调用`add_extension`方法：

```python
from selenium import webdriver
 
fp = webdriver.FirefoxProfile()
 
fp.add_extension(extension='firebug-1.8.4.xpi')
fp.set_preference("extension.firebug.currentVersion","1.8.4") # Avoid startup screen
browser = webdriver.Firefox(firefox_profile=fp)
```

## 怎样给当前窗口截图？

使用webdriver提供的`save_screenshot`方法：

```python
from selenium import webdriver
 
driver = webdriver.Firefox()
driver.get('http://www.python.org/')
driver.save_screenshot('screenshot.png')
driver.quit()
```

 

 