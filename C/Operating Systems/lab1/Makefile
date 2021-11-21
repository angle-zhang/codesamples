CC=gcc
CFLAGS=-Wall -Wextra
SRC=simpsh.c
PROG=simpsh
TAR=lab1-705003863.tar.gz

simpsh: $(SRC) 
	gcc -o $(PROG) $(SRC) $(CFLAGS) 
clean: 
	rm -rf $(PROG) $(TAR) 705003863 
dist:   $(SRC) Makefile README c.sh 
	tar -cvzf $(TAR) $(SRC) Makefile README c.sh 
debug:  $(SRC) 
	gcc -g $(SRC)
check: 
	./c.sh 705003863
