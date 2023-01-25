
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import fire
from lib.mdtrees import mdtrees

content_path = '/Users/kylin/Mind/blogpages/content'

def add_pic_prefix(article_list):
    old_str = "](assets/"
    new_str = "](/assets/"
    for article in article_list:
        with open(article, "r") as file:
            content = file.read()
            content = content.replace(old_str, new_str)

        with open(article, "w") as file:
            file.write(content)

def contents(action):
    article_list = mdtrees(content_path)
    
    
    if action == "add_pic_prefix":
        add_pic_prefix(article_list)

if __name__ == '__main__':
    fire.Fire(contents)