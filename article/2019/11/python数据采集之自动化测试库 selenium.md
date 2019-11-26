作者 ：Qiang He

邮箱：1422127065@qq.com



### python数据采集之自动化测试库 selenium

使用selenium之前需要搭建selenium的环境：python3环境，selenium环境(推荐谷歌驱动，火狐也可以)，浏览器（推荐谷歌浏览器）需要注意的是selenium的版本需要和浏览器版本相对应

详情及下载 https://www.cnblogs.com/yfacesclub/p/8482681.html 

selenium安装 https://blog.csdn.net/seedinspring/article/details/89850331 

优点：能模拟浏览器点击，获取渲染js加载后的内容    

缺点：慢，耗内存

代码示例：

```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options=Options()
options.headless=True
driver=webdriver.Firefox(options=options)

#通过selenium获取豆瓣top250首页的所有标题
url="https://movie.douban.com/top250"
driver.get(url)
# 因为所有的内容都在ol标签下的li标签下面 所有可以用此方法拿到所有的li标签,返回类型为list
titles=driver.find_elements_by_xpath("//ol[@class='grid_view']/li")

for info  in titles:
    			      movie_title=info.find_element_by_xpath(".//div[@class='hd']/a/span[@class='title']").text
    movie_url=info.find_element_by_xpath(".//div[@class='hd']/a").get_attribute("href")
    print("电影的名字是：{0}，链接为：{1}".format(movie_title,movie_url))
driver.close()
```

本案例爬取的是豆瓣top250的内容 爬取这个纯粹为了示例其用法，没有特地的去找用js加载的网站。案例中使用了无头浏览器，意思就是不打开浏览器

使用之前需要下载selenium 库 

代码解释：

```
driver.find_elements_by_xpath#抓取所有的标签 注意是elements
```



```
info.find_element_by_xpath(".//div[@class='hd']/a/span[@class='title']").text#当前标签下的电影名字 是文本，获取内容用.text
info.find_element_by_xpath(".//div[@class='hd']/a").get_attribute("href")#获取当前标签下的链接 是属性内的值 用.get_attribute("href")
```

使用完后需要关闭

