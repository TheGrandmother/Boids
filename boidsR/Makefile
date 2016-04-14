CC = gcc
LD = gcc

MAKE    = make
ENCORE  = encorec
PYTHON  = python

MAIN    = Main
FILE    = $(MAIN).enc
BOIDS   = ../boids.py

all: main

clean: tidy   
	rm -f $(MAIN)

main: Main.enc Boid.enc Vector.enc Util.enc
	$(ENCORE) -nogc $(FILE)

c:
	$(ENCORE) -nogc -c $(FILE)

run: main
	./$(MAIN) 75 10000 | $(PYTHON) $(BOIDS)

single: main
	./$(MAIN) --ponythreads 1 75 10000 | $(PYTHON) $(BOIDS)

.PHONY: all clean main c test
