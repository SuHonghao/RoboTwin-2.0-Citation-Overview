import os
from PIL import Image

# 设置路径
input_dir = "img/tab_img"          # 原始图片所在文件夹
output_dir = "img/tab_img"   # 输出文件夹
max_size = 50 * 1024               # 50 KB

os.makedirs(output_dir, exist_ok=True)

def compress_image(input_path, output_path, max_size):
    """压缩图片到指定大小（字节数以下）"""
    img = Image.open(input_path)
    
    # 转换为RGB，避免PNG是RGBA不能直接保存为JPEG
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    quality = 95
    img.save(output_path, "JPEG", quality=quality, optimize=True)

    # 循环降低质量直到满足大小
    while os.path.getsize(output_path) > max_size and quality > 5:
        quality -= 5
        img.save(output_path, "JPEG", quality=quality, optimize=True)

    # 如果还太大，再缩小尺寸
    while os.path.getsize(output_path) > max_size:
        w, h = img.size
        img = img.resize((w // 2, h // 2), Image.LANCZOS)
        img.save(output_path, "JPEG", quality=quality, optimize=True)

# 遍历文件夹
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".jpg")
        
        compress_image(input_path, output_path, max_size)
        print(f"✅ 压缩完成: {filename} → {os.path.getsize(output_path)/1024:.1f} KB")

        # 如果是 PNG，压缩完成后删除原始文件
        if filename.lower().endswith(".png"):
            os.remove(input_path)
            print(f"🗑️ 已删除原 PNG: {filename}")

print("🎉 全部图片压缩完成！")
