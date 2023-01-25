import os

def foldertrees(rootdir): # 递归查找路径下所有 md 文件
    """递归搜索目录下所有文件夹

    Args:
        rootdir (_type_): 需要搜索的根目录

    Returns:
        _folder: 文件夹列表
    """
    
    _folder = []
    l1 = os.listdir(rootdir)# 列出文件夹下的所有目录和文件
    for i in range(0,len(l1)):
        path = os.path.join(rootdir, l1[i])
        if os.path.isdir(path):
            _folder.append(path)
        if os.path.isfile(path):
            _folder.extend(foldertrees(path))

    return _folder
