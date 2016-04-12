CC = gcc
LD = gcc

MAKE    = make
ENCORE  = encorec
PYTHON  = python-32

MAIN    = Main
FILE    = $(MAIN).enc
BOIDS   = boids.py

all: main

clean: tidy   
	rm -f $(MAIN)

main:
	$(ENCORE) $(FILE)

c:
	$(ENCORE) -c $(FILE)

test:
	./$(MAIN) | $(PYTHON) $(BOIDS)

.PHONY: all clean main c test