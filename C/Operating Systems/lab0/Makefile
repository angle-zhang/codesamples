CC=gcc
CFLAGS=-Wall -Wextra

lab0: lab0.c
	$(CC) -o lab0 lab0.c $(CFLAGS)
check: check.sh
	./check.sh	
clean: 
	rm -rf lab0 lab0-705003863.tar.gz
dist:   correct.txt check.sh lab0.c Makefile backtrace.png breakpoint.png README
	tar -czvf lab0-705003863.tar.gz lab0.c Makefile backtrace.png breakpoint.png README check.sh correct.txt
