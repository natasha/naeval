
IMAGE = natasha/deeppavlov-morph-ru

image:
	docker build -t $(IMAGE) .

push:
	docker push $(IMAGE)

run:
	docker run -it --rm -p 8083:8080 $(IMAGE)

