#!/usr/bin/env python3
# 博客readme生成脚本!
import os

base_dir = "/Users/rocky/self/blog"
github_base_url = "https://github.com/hellorocky/blog/blob/master/"
readme = open(os.path.join(base_dir, "readme.md"), "w")
readme.write("# 我的博客")

for directory in os.scandir(base_dir):
    # 不包含隐藏的目录
    if not directory.name.startswith(".") and directory.is_dir():
        readme.write("\n#### {dirname}\n\n".format(dirname=directory.name))
        for mdfile in os.scandir(directory.path):
            if mdfile.is_file():
                # 处理名字中含有点的情况
                title = ".".join(mdfile.name.split(".")[1:-1])
                link = os.path.join(github_base_url, directory.name, mdfile.name)
                readme.write("* [{title}]({link})\n".format(title=title, link=link))


readme.close()
