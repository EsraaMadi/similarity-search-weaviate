import streamlit as st
import weaviate
import utils
from PIL import Image
import tempfile
import os
import pandas as pd
pd.set_option('display.max_colwidth', None)




client = weaviate.Client("http://localhost:8080")
# st.write(client.is_ready())



def load_image(image_file):
    img = Image.open(image_file)
    return img

st.subheader("Let's find similar image 😉")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

st.markdown("""---""")
if image_file is not None:

    # To View Uploaded Image
    img = load_image(image_file)
    col1, col2, col3 = st.columns(3)

    with col2:
        
        st.image(img,width=300)   
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        with open(os.path.join(tmpdirname,image_file.name),"wb") as f:
            f.write(image_file.getbuffer())
        match_lst = utils.testImage({"image":os.path.join(tmpdirname,
                                                          image_file.name)},
                                    client) 

    # parse images
    images = [weaviate.util.image_decoder_b64(match_lst[i]['image']
                                             ) for i in range(5) ]
    st.success('Most similar product images in other stores')
    
    #parse text
    txt_lst = [match_lst[i]['text'] for i in range(5)]

    st.image(images[0], width=200, caption=txt_lst[0])
    st.markdown("""---""")


    st.image(images[1], width=200, caption=txt_lst[1])
    st.markdown("""---""")

    st.image(images[2], width=200, caption=txt_lst[2])
    st.markdown("""---""")

    st.image(images[3], width=200, caption=txt_lst[3])
    st.markdown("""---""")
    
    st.image(images[4], width=200, caption=txt_lst[4])
    st.markdown("""---""")
