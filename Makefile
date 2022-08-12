setup:
	echo "Installation started ...."
	docker-compose up
	python src/import-data.py
download:
	cd data
    cd images
	kaggle datasets download -d kuchhbhi/stylish-product-image-dataset
    unzip stylish-product-image-dataset.zip
    