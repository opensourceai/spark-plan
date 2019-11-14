import glob
import os

temple = """<!-- 由 python 自动生成 -->
# spark-plan
星火计划-做AI领域的独家，所有文章旨在技术传播和交流学习，非商业用途。


## 目录
### 文章
{}
### 论文
{}

## LICENSE
[Apache License](LICENSE)

## 目的
> 为了督促自己学习知识，学习英语，翻译整理优质的中英文技术文章或者论文。

## 生成目录列表
```shell
python gen_list.py
```
"""


def gen_list(path:str):

    url_temple = "[{}]({})"

    paths = glob.glob("./{}/**/**.md".format(path), recursive=True)
    paths = [url_temple.format(os.path.basename(path)[:-3], path) for path in
             [path.replace("\\", "/")[2:] for path in paths if "README" not in path]]

    list_info = ""
    for path in paths:
        list_info += "- {}\n".format(path)
    return list_info


if __name__ == "__main__":
    article_list = gen_list("article")
    paper_list = gen_list("paper")
    md = temple.format(article_list, paper_list)
    f = open("README.md", "w", encoding="UTF-8")
    f.write(md)
    f.close()
    print(md)
