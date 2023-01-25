---
# Details front-matter reference: https://hugoloveit.com/zh-cn/theme-documentation-content/#front-matter
title: "{{ replace .Name "-" " " | title }}"
subtitle: ""
summary: ""

slug: {{ substr (md5 (printf "%s%s" .Date (replace .TranslationBaseName "-" " " | title))) 4 8 }}
date: {{ .Date }}
lastmod: {{ .Date }}

tags: []
categories: []

featuredImage: ""
featuredImagePreview: ""

draft: true
---