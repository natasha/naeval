
IMAGE = natasha/rupostagger

image:
	docker build -t $(IMAGE) .

push:
	dockern push $(IMAGE)

run:
	docker run -it --rm -p 8081:8080 $(IMAGE)
