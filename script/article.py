import os
from lib.foldertrees import foldertrees

def newposts(article_name):
    newpost_command = f"/opt/homebrew/bin/hugo -s ~/Mind/blogpages new ~/Mind/blogpages/content/posts/{article_name}.md"
    os.popen(newpost_command).read().strip()

def del_empty_assets_folder():
    assets_path = "/Users/kylin/Mind/blogpages/content/assets"
    folder_list = foldertrees(assets_path)
    for folder in folder_list:
        if os.path.exists(folder):
            os.rmdir(folder)


def articles(action):
    if action == "del_empty_assets_folder":
        del_empty_assets_folder()