---
title: "【Hugo】基于 Github Action 自动部署 Hugo Blog"
subtitle: ""
summary: ""

slug: 4105e44f
date: 2023-01-25T17:09:50+08:00
lastmod: 2023-01-25T17:09:50+08:00

tags: [Github, Blog]
categories: [Planning]

featuredImage: ""
featuredImagePreview: ""

draft: false
---

真的快要被这一堆红色的 error & not successful 烦死了, 照猫画虎半天, 出现一点小问题就没法解决, 这篇记录下从理解 Github Action 到成功自动化部署博客的过程

![](/assets/【Hugo】基于%20Github%20Action%20自动部署%20Hugo%20Blog/1.png)

---

### 不同部署方式的优劣势

传统部署方式
1. 使用 `hugo` 命令生成 public 文件夹
2. 将 public 文件夹提交至 Github
3. 由 Github Pages 提供 Web 服务

Github Action 部署方式
1. 将整个站点文件夹上传至 Github
2. Github Actions 生成静态文件, 并提交到其他分支
3. Github 使用另一分支提供 Web 服务

相比较之下使用 Github Action 方式部署的站点, 方便对文件进行备份, 允许多台设备操作博客源文件。并且允许直接在 Github 仓库直接修改文件, 本地只需要 `git pull` 拉取变更的内容即可。

缺点在于使用 Github ACtion 时 Markdown 文件透明, 如想要设置访问密码那将形同虚设。任何人想要获取你的源文件仅需要进入 contents 对应目录, 直接查看即可。

### 部署 Github Action

参考链接: [GitHub Actions 快速入门 - GitHub Docs](https://docs.github.com/zh/actions/quickstart)

假设你已经完成了 Github Action 快速入门, 现在可以将你的博客文件夹直接 push 到你的仓库, 当然此时还无法自动构建

我的库名称为 `hit0ris/hit0ris.github.io` 现在跟着我做一些操作。

首先在仓库 `.github/workflows/` 目录下新建 `gh-pages.yml` 文件, 并填入以下内容

```yml
name: GitHub Pages

on:
  push:
    branches:
      - main  # main 分支收到推送后部署
  pull_request:

jobs:
  deploy:
    runs-on: ubuntu-22.04
    permissions:
      contents: write
    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}
    steps:
      - uses: actions/checkout@v3
        with:
          submodules: true  # Fetch Hugo themes (true OR recursive)
          fetch-depth: 0    # Fetch all history for .GitInfo and .Lastmod

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: '0.101.0'

      - name: Build
        run: hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        # If you're changing the branch from main,
        # also change the `main` in `refs/heads/main`
        # below accordingly.
        if: ${{ github.ref == 'refs/heads/main' }}
        with:
          github_token: ${{ secrets.WORKFLOWS_TOKEN }}
          publish_dir: ./public
```

注意其中 `WORKFLOWS_TOKEN` 是一个变量, 需要手动设置, 在那之前, 先点击右上角头像, 进入个人主页, 生成你的 TOKEN

1. 进入你的个人设置 https://github.com/settings/profile
2. 侧边栏选择 Developer settings -> Personal access tokens -> Tokens (classic)
3. 点击 Generate new token (classic), **Note** 输入任意字段, **Expiration** 可以选择 No expiration 代表不会过去, **Select scopes** 勾选 workflow, 下拉至底部点击 **Create token**
4. 记住这个 `ghp_` 开头的 TOKEN, 它只会出现这一次, 并且之后会用到它

现在, 保证你的 `gh-pages.yml` 文件已在仓库之中, 为仓库设置 `WORKFLOWS_TOKEN` 变量的值

1. 进入仓库 https://github.com/Hit0ris/hit0ris.github.io, 点击导航栏 Settings
2. 侧边栏选择 **Secrets and variables** -> **Actions**
3. 点击 **New repository secret**, Name 输入 `WORKFLOWS_TOKEN`, Secret 输入刚才生成的 Token, 完成后点击 **Add secret**

注意, 完成操作步骤后, 因提交 ACTIONS 要早于添加 `WORKFLOWS_TOKEN` 所以可能导致第一次构建因找不到 TOKEN 而出错, 根据以下步骤, 手动再次进行部署

1. 进入仓库 https://github.com/Hit0ris/hit0ris.github.io/, 点击导航栏 Actions
2. 点击失败的构建记录 `Create gh=pages.yml`
3. 点击 Jobs 下, 右侧的 Re-run jobs 按钮, 确认重新运行
![](assets/【Hugo】基于%20Github%20Action%20自动部署%20Hugo%20Blog/2.png)

完成后返回仓库 Settings, 左侧点击 **Pages**,  **Source** 设置为 Deploy from a branch, Branch 设置为 gh-pages 分支, 点击 Save。

到此为止已经大功告成啦, 对应的 yml 文件也可以进行一些修改, 如果想通过修改部分内容, 在每天的某个时刻自动构建静态页面, 那么继续往下看。

上面的 `gh-pages.yml` 通过下面的代码明确规定当 main 分支收到 push 请求或收到 pull 请求后, 将会自动构建页面

```yml
on:
  push:
    branches:
      - main  # main 分支收到推送后部署
  pull_request:
```

同时也支持多种方式触发部署请求, 如定时在每天早上八点构建, 保留原先的基础, 修改后如下

```yml
on:
  push:
    branches:
      - main
  schedule:
    - cron: '0 0 * * *'
```

注意这里第二个 0 代表的是国际时间, 北京时间需要 +8, 这里就代表每天北京时间早 8 点自动执行

最后, 使用自动定时构建方式可能会导致 Github 热力图全绿的情况, 并不是很推荐这么去做

[在 GitHub 上保持 365 天全绿是怎样一种体验？](https://www.zhihu.com/question/34043434/answer/57826281)
