setup:
	echo "Installation started ...."
	docker-compose up
	python src/import-data.py
download:
	cd data/images
	pip install kaggle
	kaggle datasets download -d kuchhbhi/stylish-product-image-dataset
    