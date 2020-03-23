
IMAGE = natasha/maru

image:
	docker build -t $(IMAGE) .

push:
	docker push $(IMAGE)

run:
	docker run -it --rm -e TAGGER=rnn -e LEMMATIZER=pymorphy -p 8081:8080 $(IMAGE)

