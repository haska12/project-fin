#include<sys/types.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>

#define LECTURE 0
#define ECRITURE 1
int main(int argc, char *argv[]) {
int tuyau[2], nb, i;
char donnees[10];

if (pipe(tuyau) == -1) { /* creation du pipe */
	perror("Erreur dans pipe()");
	exit(EXIT_FAILURE);
}

switch (fork()){ /* les deux processus partagent le pipe */

case -1 : /* erreur */
	perror("Erreur dans fork()");
	exit(EXIT_FAILURE);

case 0 : /* processus fils, lecteur */
	close(tuyau[ECRITURE]); /* on ferme le cote ecriture */
	
	/* on peut alors lire dans le pipe */
	nb = read(tuyau[LECTURE], donnees, sizeof(donnees));
	printf("\n Fils : Mon père a envoyé : ");
puts(donnees);
	
	close(tuyau[LECTURE]);
	exit(EXIT_SUCCESS);
	
	default : /* processus pere, ecrivain */
	close(tuyau[LECTURE]); /* on ferme le cote lecture */
	strncpy(donnees, "bonjour", sizeof(donnees));

	/* on peut ecrire dans le pipe */
	write(tuyau[ECRITURE], donnees, strlen(donnees));
	close(tuyau[ECRITURE]);
	exit(EXIT_SUCCESS);
}
}	