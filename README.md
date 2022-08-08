# Search for similar products
#### Text/Image search for similar products using Weaviate   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Weaviate_logo_%28no_text%29.svg/1280px-Weaviate_logo_%28no_text%29.svg.png" width="30" height="25" />


<p align="center">
  <img width="460" height="300" src="data/repo%20pics/Animation3.gif">
</p>


This is an application spins up a [Weaviate](https://weaviate.io/) instance to search for similar products across the market. This could help stores to know if their products was also in their competitor’s offering. The app use [62k images of products](https://www.kaggle.com/datasets/kuchhbhi/stylish-product-image-dataset) combined with their text description to build vectors for the data we intend to search.

## How to run with your own images

> Prerequisites to run it yourself
- [Docker & Docker-Compose](https://docs.docker.com/compose/install/compose-desktop/)

*Then follow steps below:*
1. Clone the repository in your local machine

<p align="center">
  <img width="460" height="300" src="data/repo%20pics/step1.gif">
</p>

2. Add your images to the `data/images` folder with any format (png, jpg, jpeg )

<p align="center">
  <img width="460" height="300" src="data/repo%20pics/step2.gif">
</p>

3. Add your text that descripe each image to the `data/text` folder
    - Hint:
        - The current script accept csv file.
        - The csv file should has 2 columns (`id`: image name, `title`: text description for image)

<p align="center">
  <img width="460" height="300" src="data/repo%20pics/step3.gif">
</p>

4. Start up Weaviate and import images in the vector database using
``` console
make setup
```

<p align="center">
  <img width="460" height="300" src="data/repo%20pics/step4.gif">
</p>

5. To run the streamlit app, open for your browser at `http://localhost:8084`

<p align="center">
  <img width="460" height="300" src="data/repo%20pics/step5.gif">
</p>
