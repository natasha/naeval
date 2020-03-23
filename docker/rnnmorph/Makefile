
IMAGE = natasha/rnnmorph

image:
	docker build -t $(IMAGE) .

push:
	docker push $(IMAGE)

run:
	docker run -it --rm -p 8082:8080 $(IMAGE)

