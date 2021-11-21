// to do: 
// add common malloc and realloc function/handler
// io redir function
// change fds to command to array passed in
#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h> 
#include <unistd.h> 
#include <fcntl.h>
#include <errno.h>
#include <string.h>

#define FD_INCR 5;

//struct option {
//    const char *name;
//    int         has_arg;
//    int        *flag; pointer to flag var
//    int         val;
//};

// array of file flags initialized by val

struct option args[] = {
    // fd options
	{"rdonly", 1, NULL, 'r'}, 
	{"wronly", 1, NULL, 'w'},
    {"close", 1, NULL, 'e'},
	{"command", 1, NULL, 's'},
    {"chdir", 1, NULL, 'c'},
    
    // print options
    {"wait", 0, NULL, 't'},
	{"verbose", 0, NULL, 'v'},
    
    // signal options
    {"catch", 1, NULL, 'h'},
    {"ignore", 1, NULL, 'i'},
    {"default", 1, NULL, 'd'},
    {"pause", 1, NULL, 'p'},
    
    {"abort", 1, NULL, 'a'},
    m
    {0,0,0,0}
};


//print errno 
void print_err() { 
	fprintf(stderr, "Error: %s\n", strerror(errno)); 
} 


// check if neext element is an option
int is_opt(char* str){
    return (str[0] == '-' && str[1] == '-');
}

// malloc or realloc done cleanly
void* malloc_array(size_t size) {
    void* temp = malloc(size);
    if(temp == NULL)
        print_err();
    return temp;
}

void io_redir(int fd, int stream) {
    if(dup2(fd, stream) == -1) {
        print_err();
    }
    close(fd);
}

// option functions
void exec_command(char** argv, int i_fd, int o_fd, int e_fd) {
	int ret = fork();
	
	if(ret == 0) { 
		// does IO redirection
        io_redir(i_fd, 0);
        io_redir(o_fd, 1);
        io_redir(e_fd, 2);
		// if not correct (execlp fails) print errror
		// executes file and argument list
		// only returns if there's an error 
		if( execvp(argv[0], argv) == -1 ) 
			print_err(); 	
		exit(0);
	}
	else if(ret > 0) { 
	// wait for process to change state 
	// waitpid suspends calling process execution until child changes "state"
	//	if( WIFEXITED(status) )
	//		fprintf(stdout, "Child exited with code: %d\n", WEXITSTATUS(status)); 	
	//	else if( WIFSIGNALED(status) ) 
	//		fprintf(stdout, "Child exited with signal: %d\n", WEXITSTATUS(status)); 
	}
} 

int main(int argc, char* argv[]) { 
	int exit_code = 0; 
	if(argc>1) {
		int opt; 
		// verbose flag
		// opt flags
		int vrb_flag = 0;
        	int fd_flag; // permissions flag
        
        	// opt args
        	int* fds;
        	size_t fds_size = 0; // size of array fds
        	size_t fd_num = FD_INCR;
		size_t file_size = fd_num*sizeof(int); // bytes

		// command arg parsing
		size_t i_idx, o_idx, e_idx;
		int noptind = 0; 
		int argv_size = 0;
        
		while((opt = getopt_long(argc, argv, "-:r:w:c:v", args, NULL)) != -1) { 
			switch(opt) {
				case 'v': 
					vrb_flag = 1; 
				break;		
				case 'w': 
				case 'r':
					// get flag 
					// store fd 
					if( vrb_flag ) 
						fprintf(stdout,"%s %s\n", argv[optind-2], optarg);

                    
                    // allocate array for fds
                    ifds = (int*) malloc_array(file_size);
					// files
                    if ( (fds[fds_size] = open(optarg, fd_flag)) < 0 ) {
						 print_err();	
						 fds_size++;
						 exit_code++;
					}
					else {
						fds_size++;
						if(fd_num <= fds_size){
							fd_num += FD_INCR;
							file_size += fd_num*sizeof(int);
							fds = (int*)realloc(fds, file_size);
						}
					
					}
				break;
				case 's':
					// initialize fd indexes
					optind--;

					if( (i_dx = atoi(argv[optind++])) >= fds_size) {
						fprintf(stderr, "Wrong argument");
						exit_code++; 	
						exit(exit_code);
					}

					if( (o_idx = atoi(argv[optind++])) >= fds_size){
						fprintf(stderr, "Wrong argument");
						exit_code++; 	
						exit(exit_code);
					}
					if( (e_idx = atoi(argv[optind++])) >= fds_size){
						fprintf(stderr,"Wrong argument");
						exit_code++; 	
						exit(exit_code);
					}
					// count arguments and initialize null terminated array
					for( noptind = optind; noptind < argc; noptind++ ) { 
						// reaches end of arg list
						if(is_opt(argv[noptind])) 
							break;  
						argv_size++; 
					}
                    
					// arguments for command 
					// copy from argv
					// first 3 are i o e indexes (for fds)
					// ones after are cmd and args
					char** new_argv;

					int i = 0;
					int j = 0;  
	
					size_t arg_length = argv_size * sizeof(char*);
	
                    // malloc argv to pass to exec
					new_argv = (char**) malloc_array(arg_length+1)
					for(i = optind; i<noptind; i++,j++) { 
						size_t length = strlen(argv[i])+1;
        					new_argv[j] = (char*) malloc_array(length);
        					memcpy(new_argv[j], argv[i], length);

					}
                    
					new_argv[j] = NULL; 
					
					if( vrb_flag ) {
						fprintf(stdout, "--command %u %u %u", (unsigned)i_idx, (unsigned)o_idx, (unsigned)e_idx);
						for( i = optind, j = 0; i<noptind; i++, j++)
							fprintf(stdout, " %s", new_argv[j]);
                        fprintf(stdout, "\n");
					}
                    
					optind = noptind;	
					exec_command(new_argv, fds[i_idx], fds[o_idx], fds[e_idx]);
					free(new_argv); 
				break;
				case ':': 
					fprintf(stderr, "Argument is required for %s option. Correct usage is %s i o e cmd args\n", argv[optind-1], argv[optind - 1]); 
					exit(1);
				case '?': 
					fprintf(stderr, "Invalid option given: %s. Valid options are: --command i o e cmd args --rdonly file --wronly file \n", argv[optind]); 
					exit(1);
				break;
			}
		}
		free(fds); 
	}
	exit(exit_code); 
} 
