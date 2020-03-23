
IMAGE = natasha/udpipe-ru
SRC_URL = https://github.com/ufal/udpipe/archive/v1.2.0.zip
MODEL_URL = https://lindat.mff.cuni.cz/repository/xmlui/bitstream/handle/11234/1-2998/russian-syntagrus-ud-2.4-190531.udpipe

src.zip:
	wget $(SRC_URL) -O src.zip

model.udpipe:
	wget $(MODEL_URL) -O model.udpipe

image: model.udpipe src.zip
	docker build -t $(IMAGE) .

push:
	docker push $(IMAGE)

run:
	docker run -it --rm -p 8084:8080 $(IMAGE)

clean:
	rm src.zip model.udpipe
