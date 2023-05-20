#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int tmax= 100;


typedef struct dat {
	int day;
	int mounth;
	int year;
}dat;


typedef  struct produit {
	int num;
	char nom[20];
	float prix;
	dat dat_epx;
}produit;

void saisir(produit *p){
	printf("\npoduit");
	printf("\n\t num : ");
	scanf("%d",&p->num);
	printf("\n\t nom : ");
	scanf("%s",p->nom);
	printf("\n\t prix: ");
	scanf("%f",&p->prix);
	printf("\n\t expair day : ");
	       printf("\n\t\t day : ");
	       scanf("%d",&p->dat_epx.day);
	       printf("\n\t\t mount: ");
	       scanf("%d",&p->dat_epx.mounth);
	       printf("\n\t\t year :");
	       scanf("%d",&p->dat_epx.year);
}

void saisirtab(produit  t[],int n){
	produit p;
	int i;
	for(i=0;i<n;i++){
		saisir(&t[i]);
	}
}

void affich(produit p){
	printf("\nproduit");
	    printf("\n\t num : %d ",p.num);
	    printf("\n\t nom : %s ",p.nom);
	    printf("\n\t prix : %f ",p.prix);
	    printf("\n\t expair day : ");
	                 printf("\n\t\t day : %d",p.dat_epx.day);
			 printf("\n\t\t mount : %d",p.dat_epx.mounth);
			 printf("\n\t\t year :  %d",p.dat_epx.year);
}

void affichtab (produit t[],int n){
	int i;

	for(i<0;i<n;i++){
		affich(t[i]);
	}
}

float somdeprix(produit t[],int n){
	int i;
	float s=0;
	for(i=0;i<n;i++){
		s+=t[i].prix;
	}
	return s;
}

int compardat(dat day,dat dexp){
	if(day.day==dexp.day && day.mounth==dexp.mounth && day.year==dexp.year)
		return 0;
	else if((day.year>dexp.year)||((day.year==dexp.year)&&(day.mounth>dexp.mounth))||((day.year==dexp.year)&&(day.mounth==dexp.mounth)&&(day.day>day.day)))
		return -1;
	else 
		return 1;
}


void affichdexp(produit t[],int n, dat dexp){
	int i;

	for(i=0;i<n;i++){
		if(compardat(t[i].dat_epx,dexp)==1)
			affich(t[i]);
	}
}

produit rech(produit t[], int n,char nam[]){
	int i;
	for (i=0;i<n;i++){
		if(!strcmp(t[i].nom,nam))
			return t[i];
	}
}

int rechdec (produit t[],char nam[],int deb,int fin){
	int n;
	if(deb>fin)
		return -1;
	else {
		n=(deb +fin)/2;
		if(!strcmp(t[n].nom,nam)){

			return n;
		}
		else if(strcmp(t[n].nom,nam)>0){
			return rechdec(t,nam,n+1,fin);
		}
		else {
			return rechdec (t, nam,deb,n-1);
		}
	}
	
}

void SaveProduit(produit p[],char filnam[],int i){
	FILE *fp=fopen(filnam,"wb");
	char buffer[100];
	if(fp==NULL){
		printf("fopen erour");
		exit(0);
	}
	int a=5;
	fwrite(p,i*sizeof(produit),1,fp);
	printf("\nsave scses");
	fclose(fp);
	}
	
void mondre(char filnam[]){
         produit p;
         int i=0;
        	FILE *fp=fopen(filnam,"rb");
	char buffer[100];
	if(fp==NULL){
		printf("fopen erour");
		exit(0);
	}
	fread(&p,sizeof(produit),1,fp);
	while(1){
	if(feof(fp))
	break;
	i++;
	fread(&p,sizeof(produit),1,fp);
	affich(p);
	
	}
		printf("\nnombre %d ",  i);
	fclose(fp);
	}

void  main(){
	produit t[100],p={12,"sdfg",456,{35,56.6}};
	int i;
	float s;
	dat day={10,10,10};
	saisirtab(t,5);
	i=rechdec(t,"123",0,5);
        SaveProduit(t,"produit.txt",5);
        mondre("produit.txt");
	//affich(t[i]);
	s=somdeprix(t,5);
	//printf("\n s= %f",s);

}


		


