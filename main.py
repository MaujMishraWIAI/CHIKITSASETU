import os
import streamlit as st
from PIL import Image

from src.image_preprocessing import image_to_base64
from src.model import extract_prescription
from src.common_meds import load_common_meds, correct_name

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

def app():
    st.title("🩺  CHIKITSASETU")
    image = st.file_uploader("Upload a doctor's prescription image", type=["png", "jpg", "jpeg"])

    if image:
        img = Image.open(image)
        st.image(img, caption="Uploaded Prescription", width=300)

    if st.button("Extract Medicines"):
        imgb64 = image_to_base64(img)
        output, usage = extract_prescription(imgb64) 

        st.subheader("🧾 Output:")
        st.text(output)

        print(usage)

if __name__ == "__main__":
    app()