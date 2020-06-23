
IMAGE = natasha/stanza-ru

image:
	docker build -t $(IMAGE) .

push:
	docker push $(IMAGE)

run:
	docker run -it --rm -p 8086:8080 $(IMAGE)
