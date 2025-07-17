from PIL import Image

image_folder = r"C:\Python\image"
image_files = [f"{image_folder}/GG{i}.png" for i in range(1, 22)]

frames = []
for img in image_files:
    im = Image.open(img).convert("RGBA")

    background = Image.new("RGB", im.size, (255, 255, 255))
    background.paste(im, mask=im.split()[3])

    frames.append(background)

# Resize (ถ้าจำเป็น)
width, height = frames[0].size
frames = [frame.resize((width, height), Image.LANCZOS) for frame in frames]

# ❌ ไม่แปลงเป็นโหมด P เพื่อรักษาคุณภาพภาพ
# ✅ ใช้ optimize=True เพื่อไม่ลดสีเกินจำเป็น

frames[0].save(
    "output_hd.gif",
    save_all=True,
    append_images=frames[1:],
    duration=100,
    loop=0,
    optimize=True  # พยายามรักษาคุณภาพ
)

print("✅ output_hd.gif สร้างแล้วแบบคมชัด")

