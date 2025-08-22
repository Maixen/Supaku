import os
from PIL import Image

# Eingabe- und Ausgabeordner
input_dir = "assets/originals"
output_dirs = {
    "large": ("assets/large", (1600, 900), 85),
    "medium": ("assets/medium", (800, 450), 82),
    "thumbs": ("assets/thumbs", (420, 236), 80),
}

# Falls Ausgabeordner fehlen → erstellen
for out_dir, _, _ in output_dirs.values():
    os.makedirs(out_dir, exist_ok=True)

def resize_and_crop(img, target_size):
    """Bild proportional skalieren und dann mittig zuschneiden auf target_size"""
    target_w, target_h = target_size
    src_w, src_h = img.size

    # Skalierungsfaktor berechnen (wie ^ in magick → cover, nicht contain)
    scale = max(target_w / src_w, target_h / src_h)
    new_size = (int(src_w * scale), int(src_h * scale))
    img_resized = img.resize(new_size, Image.LANCZOS)

    # Mittelpunkt-Crop
    left = (img_resized.width - target_w) // 2
    top = (img_resized.height - target_h) // 2
    right = left + target_w
    bottom = top + target_h

    return img_resized.crop((left, top, right, bottom))

# Alle Bilder durchgehen
for filename in os.listdir(input_dir):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    filepath = os.path.join(input_dir, filename)
    with Image.open(filepath) as img:
        for name, (out_dir, size, quality) in output_dirs.items():
            processed = resize_and_crop(img, size)

            out_path = os.path.join(out_dir, filename)
            processed.save(out_path, quality=quality)

            print(f"✔ {filename} → {name} ({out_path})")
