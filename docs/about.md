# 关于本网站制作方式

## 安装mkdocs

需要有一定python基础。

```shell
# 创建文档目录
mkdir xxx_doc

# 先确保机器上有python3, 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安全mkdocs
pip install mkdocs
```

## 安装Material主题

参考网站: <https://squidfunk.github.io/mkdocs-material/>

```shell
# 安装主题, 参考: https://squidfunk.github.io/mkdocs-material/getting-started/
pip install mkdocs-material

# 配置主题，在mkdocs.yml文件下
# theme:
#   name: material
```

## 部署

需要先配置好github地址，然后才行。

```shell
# 部署静态文档到github-pages
mkdocs gh-deploy
```
