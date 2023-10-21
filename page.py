import streamlit as st
from prediction import predict_result
import imageio.v3 as iio
from PIL import Image


st.title("Image Forgery Detection")


file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if file is not None:
    img = iio.imread(file)
    image = Image.fromarray(img)

    if st.button("Predict"):
        
        st.write(predict_result(image))
        st.image(image, use_column_width=True)
