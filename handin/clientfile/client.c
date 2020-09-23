#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <unistd.h>

#define PORTNUM 3327
#define PORTNUM2 3328
#define DSTN 201514649
#define DHW 1

void showMenu()
{
    printf("**************************************\n");
    printf("*           HandIn Client            *\n");
    printf("*-h : Help                           *\n");
    printf("*-f : File Select                    *\n");
    printf("*-n : Student number                 *\n");
    printf("*-w : Select homework                *\n");
    printf("*-s : show homework                  *\n");
    printf("**************************************\n");
    exit(0);
}
void showHomework(char *ip)
{
    char buf[BUFSIZ];
    struct sockaddr_in sin,sin1,cli;
    int sd,sd1,ns1,clientlen = sizeof(cli);
    memset((char *)&sin,'\0',sizeof(sin));
    sin.sin_family = AF_INET;
    sin.sin_port = htons(PORTNUM);
    sin.sin_addr.s_addr = inet_addr("192.168.133.134");

    if((sd = socket(AF_INET,SOCK_STREAM,0)) == -1)
    {
        perror("socket");
        exit(1);
    }
    if(connect(sd,(struct sockaddr *)&sin,sizeof(sin)))
    {
        perror("connect");
        exit(1);
    }
    send(sd,"1",2,0);
    memset(buf,0,BUFSIZ);

    recv(sd,buf,sizeof(buf),0);
    printf("%s",buf);
    close(sd);
    exit(0);
}

int main(int argc, char *argv[])
{
    char buf[BUFSIZ];
    struct sockaddr_in sin;
    int sd;
    FILE *fp;
    extern char *optarg;
    extern int optind,opterr,optopt;
    int stdn;
    char hw[100];
    int n;
    char filename[512];
    char ip[25];

    if(argc < 2)
    {
        printf("too few arguments");
        exit(1);
    }
//    printf("input server ip : ");
//    scanf("%s",ip);

    while((n = getopt(argc,argv,"hf:n:w:s")) != -1)
    {
        switch(n)
        {
        case 'h':
            showMenu();
            break;
        case 'f':
            fp = fopen(optarg,"r");
            strcpy(filename,optarg);
            break;
        case 'n':
            stdn = atoi(optarg);
            break;
        case 'w':
            strcpy(hw,optarg);
            break;
        case 's':
            showHomework(ip);
            break;
        }
    }


    if((sd = socket(AF_INET,SOCK_STREAM,0)) == -1)
    {
        perror("socket");
        exit(1);
    }

    memset((char *)&sin,'\0',sizeof(sin));
    sin.sin_family = AF_INET;
    sin.sin_port = htons(PORTNUM);
    sin.sin_addr.s_addr = inet_addr("192.168.133.134");

    if(connect(sd,(struct sockaddr *)&sin,sizeof(sin)))
    {
        perror("connect");
        exit(1);
    }

    send(sd,"0",2,0);
    send(sd,filename,strlen(filename)+1,0);
    send(sd,hw,strlen(hw)+1,0);

    while(1)
    {
        fgets(buf,BUFSIZ,fp);
        printf("%s",buf);
        send(sd,buf,strlen(buf)+1,0);
        if(strlen(buf) == 0)
            break;
        memset(buf,0x00,BUFSIZ);
    }
    recv(sd,buf,sizeof(buf),0);
    printf("%s\n",buf);
    memset(buf,0x00,BUFSIZ);
    recv(sd,buf,sizeof(buf),0);
    printf("%s\n",buf);

    return 0;
}
