.POSIX:
.SUFFIXES:
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail
SHELL := /bin/bash

NAME=example

CC?=gcc
CFLAGS=-std=c99 -Wall -Wextra -pedantic
DEBUG_CFLAGS=-O0 -g3 -ggdb3 -pg -save-temps
RELEASE_CFLAGS=-O3 -Werror -Wshadow -Wfloat-equal -Wformat=2 -Wswitch-default -Wconversion -Wunreachable-code -Wcast-qual -Wwrite-strings
LDLIBS=-lm

ifdef DEBUG
CFLAGS+=${DEBUG_CFLAGS}
endif

OBJ=${NAME}.o

all: CFLAGS+=${RELEASE_CFLAGS}
all: clean ${NAME}

${NAME}: ${OBJ}
	$(CC) $^ -o $@ ${LDLIBS}

%.o: %.c
	$(CC) ${CFLAGS} -o $@ -c $<

clean:
	rm -rf *.o ${NAME}

.PHONY: all clean

# Makefile from Quickstart
# qkst.io/makefile/clang
