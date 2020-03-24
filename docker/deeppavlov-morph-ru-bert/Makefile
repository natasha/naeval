
IMAGE = natasha/deeppavlov-morph-ru-bert

image:
	docker build -t $(IMAGE) .

push:
	docker push $(IMAGE)

run:
	docker run -it --rm -p 8083:5000 $(IMAGE)

