#include <fcntl.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <unistd.h>
#include <getopt.h>
#include <stdio.h>
#include <signal.h>

#define BUFFERSIZE 1

struct option args[] = { 
	{"input", 1, NULL, 'i'},
	{"output", 1, NULL, 'o'}, 
	{"segfault", 0, NULL, 's'}, 
	{"catch", 0, NULL, 'c'}, 
	{"dump-core", 0, NULL, 'd'},
	{0,0,0,0}  
}; 

void s_segFault(char* n) { 
	*n = 'h'; 
}

void c_segHandler() { 
	fprintf(stderr, "Segfault caught, exiting program... \n");
	exit(4); 
}


void handleFlags(int *flags, const char* i_file, const char* o_file){
	int ifd = 0; 
	int ofd = 1;
	
	// catch
	if( flags[4] != 0 ) 
		signal(SIGSEGV, c_segHandler);
	
	// dump-core
	if( flags[3] != 0 ){
		signal(SIGINT, SIG_DFL);					
		fprintf(stderr, "Dump-core on segfault"); 
		exit(139);
	}

	// segfault
	if( flags[2] != 0 ) 
		s_segFault((char*)NULL); 
		
	if( flags[1] != 0 ) {	
		if((ifd = open(i_file, O_RDONLY)) >= 0) { 
			close(0); 
			dup(ifd); 
			close(ifd); 
		} 
		else { 
			fprintf(stderr, "Error opening %s. %s \n", optarg, strerror(errno));
			exit(2);
		} 
	} 

	if ( flags[0] != 0 ) {  
		if((ofd = open(o_file, O_TRUNC | O_WRONLY | O_CREAT)) >= 0) { 
			close(1); 
			dup(ofd);
			close(ofd);
		}  
		else {
			fprintf(stderr, "Error opening to %s. %s \n", optarg, strerror(errno)); 
			exit(3);
		} 
	}
     
} 



int main(int argc, char* argv[]) { 
	char buffer[BUFFERSIZE];
 	
	// arg parsing 	
	int opt; 
	int flags[5] = {0};

	const char* i_file; 
	const char* o_file;  
	// file descriptors 
	if(argc > 1) { 
		while((opt=getopt_long(argc, argv, ":i:o:scd", args, NULL)) != -1) { 
			switch(opt) { 
				case 'c': 
					flags[4] = 1;
					break; 
				case 'd': 
					flags[3] = 1; 
					break;
				case 's': 
					flags[2] = 1;
					break;  
				case 'i': 
					flags[1] = 1;
					i_file = optarg;  
					break; 
				case 'o': 
					flags[0] = 1; 
					o_file = optarg;
					break; 
				case ':': 	
					fprintf(stderr, "Argument is required for %s option. Correct usage %s=FILE or %s FILE \n", argv[optind-1], argv[optind - 1], argv[optind-1]); 
					exit(1);
					break; 
				case '?': 
					fprintf(stderr, "Invalid option given. Valid options are: --input=FILE --output=FILE --segfault --catch --dump-core \n"); 
					exit(1);
					break; 	
			}	
		}
		handleFlags(flags, i_file, o_file); 	
	}


	
	int status;	
	
	while(1) {
		status = read(0, buffer, 1);
		if( status <= 0 ) 
			break;
		status = write(1, buffer, 1);
		if( status <= 0 ) 
			break;
	}

	exit(0);

	

} 
