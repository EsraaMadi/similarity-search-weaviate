import streamlit as st
import weaviate
import utils
from PIL import Image
import tempfile
import os
import pandas as pd
pd.set_option('display.max_colwidth', None)




# client = weaviate.Client("http://localhost:8080")
client = weaviate.Client("http://172.20.121.78:8080")
# st.write(client.is_ready())



def load_image(image_file):
    img = Image.open(image_file)
    return img

st.subheader("Let's find similar image 😉")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

if image_file is not None:

    # To View Uploaded Image
    img = load_image(image_file)
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write(" ")

    with col2:
        st.image(img,width=300)

    with col3:
        st.write(" ")
    
    
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        with open(os.path.join(tmpdirname,image_file.name),"wb") as f:
            f.write(image_file.getbuffer())
        match_lst = utils.testImage({"image":os.path.join(tmpdirname,
                                                          image_file.name)},
                                    client) 

    # parse images
    images = [weaviate.util.image_decoder_b64(match_lst[i]['image']
                                             ) for i in range(3) ]
    st.success('Most related / similar product images in the market')
    st.image(images, width=200)
    
    #parse text
    txt_lst = [match_lst[i]['text'] for i in range(3)]
    txt_df = pd.DataFrame (txt_lst,
                           columns = ['Description'])
    st.dataframe(txt_df, 1000)

