#include<sys/types.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>

#define LECTURE 0
#define ECRITURE 1

int main(int argc, char *argv[]) {
int fd[2];

if (pipe(fd) == -1) {
		perror("Erreur dans pipe()");
		exit(EXIT_FAILURE);
}

switch (fork()) {
case -1 : /* erreur */
		perror("Erreur dans fork()");
		exit(EXIT_FAILURE);
case 0 : /* processus fils, ls , ecrivain */
		//Etape 1.1
		close(fd[LECTURE]);
		/* dup2 va brancher le cote ecriture du tuyau */
		/* comme sortie standard du processus courant */
		//Etape 1.2
		if (dup2(fd[ECRITURE], STDOUT_FILENO) == -1) { 
			perror("Erreur dans dup2()");
		} 
		/* on ferme le descripteur qui reste pour */
		/* << eviter les fuites >> ! */
		close(fd[ECRITURE]);
		/* ls en ecrivant sur stdout envoie en fait dans le */
		/* tuyau sans le savoir */
		if (execlp("ls", "ls", NULL) == -1) {
			perror("Erreur dans execlp()");
			exit(EXIT_FAILURE);
		}
default : /* processus pere, wc , lecteur */
	//Etape 2.1
	close(fd[ECRITURE]);
	/* dup2 va brancher le cote lecture du tuyau */
	/* comme entree standard du processus courant */
	//Etape 2.2
	if (dup2(fd[LECTURE], STDIN_FILENO) == -1) {
		perror("Erreur dans dup2()");
	} 
	/* on ferme le descripteur qui reste */
	close(fd[LECTURE]);
	/* wc lit l’entree standard, et les donnees */
	/* qu’il recoit proviennent du tuyau */
	if (execlp("wc", "wc", "-l", NULL) == -1) {
		perror("Erreur dans execlp()");
		exit(EXIT_FAILURE);
	}
}
exit(EXIT_SUCCESS);
}
