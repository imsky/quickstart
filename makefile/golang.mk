.POSIX:
.SUFFIXES:
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
SHELL := /bin/bash

NAME=example
COMMIT=$(shell git rev-parse --short=16 HEAD)
TIMESTAMP=$(shell date -u '+%Y-%m-%dT%I:%M:%SZ')

LDFLAGS=
# LDFLAGS += -X main.BuildTime=${TIMESTAMP}
# LDFLAGS += -X main.BuildSHA=${COMMIT}

PREFIX?=${PWD}/
TEST_FLAGS?=-race

all: quality test build

quality:
	go vet
	go fmt
	go mod tidy

test:
	go test ${TEST_FLAGS} -coverprofile=coverage

clean:
	rm -f ${PREFIX}${NAME}*

build: clean build-darwin build-linux

build-%:
	GOOS=$* GOARCH=386 go build -ldflags '${LDFLAGS}' -o ${PREFIX}${NAME}-$*

.PHONY: all quality test clean build

# Makefile from Quickstart
# qkst.io/makefile/golang
