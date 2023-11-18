#1st build
FROM golang:1.21.4
WORKDIR /Docker-Kubernetes

COPY cli ./cli

RUN CGO_ENABLED=0 GOOS=linux go install ./cli/server

#2nd Stage

FROM alpine:latest
WORKDIR /app/

COPY --from=0 /go/bin/server ./binary

CMD ./binary