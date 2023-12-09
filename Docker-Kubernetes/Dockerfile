#1st build
FROM golang:1.21.5
WORKDIR /home/jack/dev/General/Docker-Kubernetes

COPY go.mod .
COPY main.go .

RUN  go build -o bin .

ENTRYPOINT ["/home/jack/dev/General/Docker-Kubernetes"]
