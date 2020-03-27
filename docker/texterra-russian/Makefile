
IMAGE = natasha/texterra-russian

image:
	docker build -t $(IMAGE) .

push:
	docker push $(IMAGE)

run:
	docker run -it --rm -p 8082:8080 --name texterra $(IMAGE)
