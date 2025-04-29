from PIL import Image, ImageChops

def compare_images(img1_path, img2_path, diff_output_path=None) -> bool:
    with Image.open(img1_path) as img1, Image.open(img2_path) as img2:
        diff = ImageChops.difference(img1, img2)

        if diff.getbbox():  # если есть различия
            if diff_output_path:
                # Создаем красный оверлей на отличиях
                red_overlay = Image.new("RGB", img1.size, (255, 0, 0))
                diff_mask = diff.convert("L").point(lambda x: 255 if x > 0 else 0)
                highlighted = Image.composite(red_overlay, img2, diff_mask)
                highlighted.save(diff_output_path)
            return False
        return True
