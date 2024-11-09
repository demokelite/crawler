# Weibo Comments Scraper

这是一个用于抓取微博评论的 Python 脚本。它使用 `requests` 库来发送 HTTP 请求，并使用 `csv` 库来将数据保存到 CSV 文件中。

## 功能特点

- 抓取指定微博 ID 的评论。
- 清洗评论内容，移除其中的 URL。
- 将评论数据保存到 CSV 文件中，包括昵称、归属地、点赞数、性别和内容。

## 运行环境

- Python 3.x
- requests 库
- csv 库（Python 标准库）
- re 库（Python 标准库）

## 安装依赖

运行以下命令来安装所需的依赖：

```bash
pip install requests
