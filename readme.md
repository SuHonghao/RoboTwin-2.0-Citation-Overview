# 🧠 RoboTwin 2.0 Citation Overview

用于展示 **RoboTwin** 相关论文的引用信息与展示网页。


## 🚀 更新网页方法

若需更新网页中的论文数据，请按照以下步骤操作：


### 🧩 环境依赖


```bash
pip install pandas openpyxl
```


### 1️⃣ 编辑数据文件
打开文件：
```
generate_cards/papers.xlsx
````

在表格中填写或修改论文信息，常见字段包括：

| 字段 | 说明 |
|------|------|
| Title | 论文标题 |
| Year | 发表年份 |
| DOI / URL | 论文链接 |

保存修改后退出 Excel。

---

### 2️⃣ 生成网页数据
运行以下命令（确保当前路径在仓库根目录）：

```bash
python generate_cards/generate_cards.py
````

该脚本将自动读取 `papers.xlsx` 文件，生成更新后的网页内容（HTML 文件及静态资源）。

---

### 3️⃣ 上传至 GitHub

执行以下命令，将更新后的网页推送到 GitHub：

```bash
git add .
git commit -m "update website data"
git push origin main
```

上传完成后，刷新你的仓库网页（例如 GitHub Pages 或部署地址）即可查看最新更新。

---


## 📄 目录结构

```
.
├── generate_cards/
│   ├── papers.xlsx               # 论文数据文件
│   ├── generate_cards.py         # 自动生成网页脚本
│   ├── stats.json                # 论文数量/更新日期等
│   └── card.html                 # 被引用论文卡片
├── index.html                    # 网页入口文件
├── styles.css                    # 页面样式
├── app.js                        # 
└── README.md                     # 使用说明
```


