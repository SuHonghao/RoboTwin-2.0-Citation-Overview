import os

# 图片文件夹路径
img_dir = "img/tab_img"

# 输出的 txt 文件
output_file = "image_paths.txt"

# 遍历文件夹，收集所有 .jpg 文件
paths = []
for filename in sorted(os.listdir(img_dir)):
    if filename.lower().endswith(".jpg"):
        rel_path = os.path.join("..", img_dir, filename)  # 相对路径
        paths.append(rel_path)

# 写入到 txt 文件
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(paths))

print(f"✅ 已生成 {output_file}, 共 {len(paths)} 个路径")
