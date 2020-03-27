
IMAGE = natasha/udpipe-ru

image:
	docker build -t $(IMAGE) .

push:
	docker push $(IMAGE)

run:
	docker run -it --rm -p 8084:8080 $(IMAGE)
