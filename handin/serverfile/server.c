#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <unistd.h> 
#include <time.h>
#include <sys/stat.h>

#define PORTNUM 3327
#define PORTNUM2 3328

int main()
{
    char buf[BUFSIZ] = {0,};
    struct sockaddr_in sin,cli;
    int sd,ns,clientlen = sizeof(cli);
    FILE *fp;
    FILE *fp1;
    int a;
    int ind=0;
    char buf1[500] = {0,};
//    int sd1;
    time_t now;
    char filename[512] = {0,};
    char filename1[512] = {0,};
    char inst[550] = {0,};
    char xx[50] = {0,};
    char hw[100];
    FILE *fp2;
    char xxx[550];
    FILE *fp3;
    char sol,res;
    int bbb=0;
    int i;
    char ip[16];
//    int ind;

//    printf("input server ip : ");
//    scanf("%s",ip);
    memset((char *)&sin,'\0',sizeof(sin));
    sin.sin_family = AF_INET;
    sin.sin_port = htons(PORTNUM);
    sin.sin_addr.s_addr = inet_addr("192.168.133.134");

    if((sd = socket(AF_INET,SOCK_STREAM,0)) == -1)
    {
        perror("socket");
        exit(1);
    }



    if(bind(sd,(struct sockaddr *)&sin,sizeof(sin)))
    {
        perror("bind");
        exit(1);
    }


    if(listen(sd,5))
    {
        perror("listen");
        exit(1);
    }


    while(1)
    {
        if((ns = accept(sd,(struct sockaddr *)&cli,&clientlen)) == -1)
        {
            perror("accept");
            exit(1);
        }


        recv(ns,buf,sizeof(buf),0);




        if(strcmp(buf,"1") == 0)
        {
            printf("---send HW list---\n");
            fp = fopen("HWList","r");
            fread(buf,BUFSIZ,1,fp);
            send(ns,buf,strlen(buf)+1,0);
            printf("%s",buf);
            close(ns);
        }
        
        else if(strcmp(buf,"0") == 0)
        {
            memset(buf,'\0',BUFSIZ);
            recv(ns,buf,sizeof(buf),0);
            chdir("/home/minsu/Documents/handin/serverfile");
            if(chdir("HWStore") == -1)
            {
                mkdir("HWStore",0755);
                chdir("HWStore");
            }
            now = time(NULL);
            sprintf(xx,"%d",(int)now);
            strcat(buf,xx);
            strcat(buf,".c");
            strcpy(filename,buf);
            fp = fopen(buf,"w");
            recv(ns,hw,sizeof(hw),0);
            while(1)
            {
                recv(ns,buf,sizeof(buf),0);
                printf("%s",buf);
                fputs(buf,fp);
                if(strlen(buf) == 0)
                    break;
                memset(buf,0x00,BUFSIZ);
            }


            memset(buf,0x00,BUFSIZ);


            fclose(fp);
            strcpy(filename1,filename);
            ind = strlen(filename1);
            filename1[ind-1] = 0x00;
            filename1[ind-2] = 0x00;
            sprintf(inst,
                    "gcc -o %s %s 2> ~/Documents/handin/serverfile/stdout",
                    filename1,filename);
            system(inst);


            fp1 = fopen(
                    "/home/minsu/Documents/handin/serverfile/stdout","r");
            fread(buf,BUFSIZ,1,fp1);
            system("rm /home/minsu/Documents/handin/serverfile/stdout");


            if(strlen(buf) == 0)
            {
                send(ns,"Compile : Success",19,0);
                memset(inst,0x00,550);
                bbb = 0;


                for(i=1 ; i<=5 ; i++)
                {
                    memset(inst,0x00,550);
                    memset(xxx,0x00,550);
                    sprintf(inst,
                            "~/Documents/handin/serverfile/HWStore/%s < ~/Documents/handin/serverfile/TC/%s/%d > x",
                            filename1,hw,i);
                    system(inst);
                    sprintf(xxx,
                            "/home/minsu/Documents/handin/serverfile/SOLUTION/%s/%d",
                            hw,i);
                    printf("\n\n%s\n\n",xxx);
                    fp2 = fopen("x","rt");
                    fp3 = fopen(xxx,"rt");
                    if(fp2 == NULL)
                    {
                        perror("fopen in executing fp2");
                        exit(1);
                    }
                    if(fp3 == NULL)
                    {
                        perror("fopen in executing fp3");
                        exit(1);
                    }
                    while(1)
                    {
                        if(feof(fp2) == 0 && feof(fp2) == 0)
                        {
                            res = fgetc(fp2);
                            sol = fgetc(fp3);
                            if(res != sol)
                            {
                                send(ns,"wrong answer",13,0);
                                bbb = 1;
                                break;
                            }
                        }
                        else if(feof(fp2) != 0 && feof(fp3) == 0)
                        {
                            send(ns,"wrong answer",13,0);
                            bbb = 1;
                            break;
                        }
                        else if(feof(fp2) == 0 && feof(fp3) != 0)
                        {
                            send(ns,"wrong answer",13,0);
                            bbb = 1;
                            break;
                        }
                        else
                        {
                            break;
                        }
                    }
                    if(bbb)
                    {
                        break;
                    }
                    system("rm x");
                }
                if(bbb == 0)
                {
                    send(ns,"Correct answer",15,0);
                }
            }
            else
            {
                send(ns,buf,strlen(buf)+1,0);
            }
            fclose(fp1);
            chdir("~/Documents/handin/serverfile");
        }
        else
        {
        }
        close(ns);
    }
    close(sd);
}
