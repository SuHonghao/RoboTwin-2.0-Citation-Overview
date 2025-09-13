import pandas as pd
import os
import json
from datetime import datetime

# 读取 Excel 文件
df = pd.read_excel("generate_cards/papers.xlsx")

html_cards = []

for _, row in df.iterrows():
    card = f"""
    <article class="cite-card">
      <a class="thumb" href="{row['link']}" target="_blank" rel="noopener">
        <img src="{row['image']}" alt="cover image" />
      </a>
      <div class="content">
        <h4 class="cite-title">
          <a href="{row['link']}" target="_blank" rel="noopener">{row['title']}</a>
        </h4>
        <p class="cite-brief">{row['abstract']}</p>
        <div class="tagbar" aria-label="tags">
          {''.join(f'<span class="tag">{tag.strip()}</span>' for tag in str(row['tags']).split(';'))}
        </div>
      </div>
    </article>
    """
    html_cards.append(card)

# 包装成完整网页
html_page = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <title>card</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <section class="card-list">
    {"".join(html_cards)}
  </section>
</body>
</html>
"""

# 输出到 generate_cards 文件夹
output_path = os.path.join("generate_cards", "card.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_page)

print(f"✅ Done：{output_path}")



# --- 统计并导出 stats.json ---

# 建议：仅统计“有效行”（有 title & link）
valid_df = df.dropna(subset=["title", "link"])
num_papers = int(len(valid_df))

stats = {
    "num_papers": num_papers,
    "source": "generate_cards/papers.xlsx",   # 按你的实际文件名/路径改
    "last_updated": datetime.now().strftime("%Y-%m-%d")
}

# 存在 generate_cards/ 下（和你的表同目录）
stats_path = os.path.join("generate_cards", "stats.json")
with open(stats_path, "w", encoding="utf-8") as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)

print(f"✅ Stats written: {stats_path}")

