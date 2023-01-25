import os

def mdtrees(rootdir): # 递归查找路径下所有 md 文件
    """递归搜索目录下所有 .md 的文件

    Args:
        rootdir (_type_): 需要搜索的根目录

    Returns:
        list: md 文件列表
    """
    
    _files = []
    l1 = os.listdir(rootdir)# 列出文件夹下的所有目录和文件
    for i in range(0,len(l1)):
        path = os.path.join(rootdir, l1[i])
        if os.path.isdir(path):
            _files.extend(mdtrees(path))
        if os.path.isfile(path):
            if ".md" in str(path):
                _files.append(path)

    return _files