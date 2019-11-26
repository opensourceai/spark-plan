作者 ：Qiang He

邮箱：1422127065@qq.com

### python数据采集之requests

利用requests库发起get或者post请求 

使用代码范例

```python
import requests
from lxml  import etree
from fake_useragent import UserAgent
import json
import time
#随机请求头
ua=UserAgent()

# get请求
def get_url(url):
    header={
        "User-Agent":ua.random
    }
    res=requests.get(url,headers=header)

    if res.status_code==200:
        html=etree.HTML(res.content)
        # 字段名以及xpath规则添加 可添加多个 返回的字段类型为list
        name=html.xpath("//div[@id='content']/h1/text()")

    else:
        print("error url：%s,状态码"%(url,res.status_code))

# post请求
def post_url(url):
    header = {
        "User-Agent": ua.random
    }
    payload={
        "key1":"value1",
        "key2": "value2",
        "key3": "value3",
        "key4": "value4",

    }
    #请求时视情况而定看是否需要带上数据表单
    # 数据表单的使用   data=json.dumps(payload)
    response=requests.post(url,headers=header)
    try:
        if response.status_code==200:
            #请求内容为转为json
            datas = json.loads(response.text)['data']["list"]
            for data in datas:
                title=data['title']
                print(title)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # url添加 这里以豆瓣top250为例
    geturl='https://movie.douban.com/top250'
    get_url(geturl)
    # csdns 区块链的api
    posturl = 'https://blockchain.csdn.net/m/zone/blockchain/blog_api?page=1'
    post_url(posturl)

```

使用前需要下载 requests、lxml、fake-useragent，json库

此范例可作为requests库爬取数据的一个模板，可根据自己的需求进行相应的扩充

requests中文文档: https://2.python-requests.org//zh_CN/latest/user/quickstart.html 

