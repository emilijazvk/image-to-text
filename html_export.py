import os
import shutil

def export_file(image_path: str, text: str, save_path:str)->None:
    image_name = os.path.basename(image_path)
    target_img_path = os.path.join(os.path.dirname(save_path), image_name)

    if os.path.abspath(image_path)!= os.path.abspath(target_img_path):
        shutil.copy(image_path, target_img_path)

    html_cont = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>OCR Result></title>

</head>
<body>
    <h2>Original image:</h2>
    <img src="{image_name}" alt="OCR Image" style="max-width:100%;">
    <h2>Recognized text: </h2>
    <pre>{text}</pre>
</body>
</html>
"""

    with open(save_path, "w", encoding="utf-8") as f:
            f.write(html_cont)