
IMAGE = natasha/spacy-ru2
SRC_URL = https://github.com/buriy/spacy-ru/archive/v2.2.zip

src.zip:
	wget $(SRC_URL) -O src.zip

image: src.zip
	docker build -t $(IMAGE) .

push:
	docker push $(IMAGE)

run:
	docker run -it --rm -p 8085:8080 $(IMAGE)

clean:
	rm src.zip
