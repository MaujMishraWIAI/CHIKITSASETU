from PIL import Image
import base64
import io

def image_to_base64(img):
    img = img.resize((1000, 1000))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()