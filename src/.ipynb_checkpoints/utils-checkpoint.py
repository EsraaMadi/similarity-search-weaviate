import weaviate
import uuid
import datetime, time, os


def generate_uuid(class_name: str, identifier: str,
                  test: str = 'teststrong') -> str:
    """ Generate a uuid based on an identifier
    :param identifier: characters used to generate the uuid
    :type identifier: str, required
    :param class_name: classname of the object to create a uuid for
    :type class_name: str, required
    """
    test = 'overwritten'
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, class_name + identifier))

def init_weaviate_schema(client):

#     client.schema.delete_all()

    class_obj = {
        "class": "Item",
            "description": "A class to implement CLIP example",
            "moduleConfig": {
            "multi2vec-clip": {
              "imageFields": [
                  "image"
              ],
              "textFields": [
                  "text"
              ],
              "weights": {
                "textFields": [0.7],
                "imageFields": [0.3]
              }
            }
          },
            "vectorIndexType": "hnsw",
            "vectorizer": "multi2vec-clip",
            "properties": [
                {
                "dataType": [
                    "string"
                ],
                "name": "text"
                },
                {
                "dataType": [
                    "blob"
                ],
                "name": "image"
                }
            ]
        }

    client.schema.create_class(class_obj)
    print("Schema class created")


def import_images_text(image_path,
                       store_df,
                       id_column,
                       description_column,
                       batch_size=199):
    
    no_items_in_batch = 0
    imported_items_count = 0
    before=time.time()
    
    # Adding all images from folder
    for img in os.listdir(image_path):
        try:
            # get text description for image
            img_ref = store_df[store_df[id_column]==int(img.split('.')[0])]
            
            # encode the image
            encoded_image = weaviate.util.image_encoder_b64(f"{image_path}{img}")

            # add image and text to the batch
            data_properties = {
                "image": encoded_image,
                "text":img_ref[description_column].values[0]
            }
            client.batch.add_data_object(data_properties,
                                         "Item",
                                         generate_uuid('Item',img))
            no_items_in_batch += 1
            imported_items_count += 1

            # check batch size to insert it in database
            if no_items_in_batch >= batch_size:
                results = client.batch.create_objects()
                print('finished uploaded images', imported_items_count, 'so far')
                no_items_in_batch = 0
        except:
            pass
            

    client.batch.create_objects()
    after=time.time()
    
    uploaded_time = round((after-before)/60, 2)
    print("{} images added in {}min".format(len(os.listdir(image_path)),
                                            uploaded_time))
    
    

def testText(nearText, client):
    res = client.query.get("Item",
                           ["image",
                            "text",
                            "_additional {certainty} "]
                          ).with_near_text(nearText).do()
    
    return res['data']['Get']['Item']


def testImage(nearImage, client):
    imres = client.query.get("Item",
                             ["image",
                              "text",
                              "_additional {certainty}"]
                             ).with_near_image(nearImage).do()
            
    return imres['data']['Get']['Item']
