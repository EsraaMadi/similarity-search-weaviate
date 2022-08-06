import weaviate
import base64, json, os
import pandas as pd 
import utils as ut


# check text file
csv_file = os.listdir("../data/text/")
if len(csv_file) != 1:
    print('please upload one csv file')
elif csv_file[0].split('.')[1]!= 'csv':
    print('please upload a csv file')
elif len(os.listdir("../data/images"))==0:
    print('please upload images files')
else:
    # read file
    store_df = pd.read_csv(f"../data/text/{csv_file}")

    # create instance from weaviate client
    # should change host to local host
    client = weaviate.Client("http://172.20.121.78:8080")
    print(client.is_ready())

    # build schema
    ut.init_weaviate_schema(client)

    # import images and text
    ut.import_images_text(image_path='../data/images/',
                          store_df,
                          id_column= 'id',
                          description_column = 'title')
