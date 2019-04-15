#define MAX_L_KNEE   2100
#define MIN_L_KNEE   500
#define MAX_R_KNEE  900
#define MIN_R_KNEE  2500

#define MAX_L_VERT   500
#define MIN_L_VERT   2100
#define MAX_R_VERT  2500
#define MIN_R_VERT  1000

#define MAX_L_HORI  500
#define MIN_L_HORI  2100
#define MAX_R_HORI 500
#define MIN_R_HORI 2100


#define FRON_L_KNEE  26
#define FRON_R_KNEE  10
#define MIDD_L_KNEE  22
#define MIDD_R_KNEE  6
#define REAR_L_KNEE  18
#define REAR_R_KNEE  2

#define FRON_L_VERT  25
#define FRON_R_VERT  9
#define MIDD_L_VERT  21
#define MIDD_R_VERT  5
#define REAR_L_VERT  17
#define REAR_R_VERT  1

#define FRON_L_HORI 24
#define FRON_R_HORI 8
#define MIDD_L_HORI 20
#define MIDD_R_HORI 4
#define REAR_L_HORI 16
#define REAR_R_HORI 0

#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void move_knee(int leg, float deg, unsigned int sleep)
{
    if (leg > 15)
        deg = deg * (MAX_L_KNEE - MIN_L_KNEE) + MIN_L_KNEE;
    else
        deg = deg * (MAX_R_KNEE - MIN_R_KNEE) + MIN_R_KNEE;
    printf("#%dP%.0f\n", leg, deg); usleep(sleep);
}

void move_vert(int leg, float deg, unsigned int sleep)
{
    if (leg > 15)
        deg = deg * (MAX_L_VERT - MIN_L_VERT) + MIN_L_VERT;
    else
        deg = deg * (MAX_R_VERT - MIN_R_VERT) + MIN_R_VERT;
    printf("#%dP%.0f\n", leg, deg); usleep(sleep);
}

void do_debout(void)
{
    move_knee(FRON_L_KNEE, 1, 100000);
    move_knee(FRON_R_KNEE, 1, 100000);
    move_knee(MIDD_L_KNEE, 1, 100000);
    move_knee(MIDD_R_KNEE, 1, 100000);
    move_knee(REAR_L_KNEE, 1, 100000);
    move_knee(REAR_R_KNEE, 1, 100000);
    move_vert(FRON_L_VERT, 0, 100000);
    move_vert(FRON_R_VERT, 0, 100000);
    move_vert(MIDD_L_VERT, 0, 100000);
    move_vert(MIDD_R_VERT, 0, 100000);
    move_vert(REAR_L_VERT, 0, 100000);
    move_vert(REAR_R_VERT, 0, 100000);
    printf("#%dP%d\n", MIDD_L_HORI, 2400); usleep(100);
    printf("#%dP%d\n", MIDD_R_HORI, 2100); usleep(100);
}

void do_dab(void)
{
    move_knee(MIDD_L_KNEE, 1, 100000);
    printf("#%dP%d\n", MIDD_L_HORI, 2100); usleep(10000);
    move_knee(MIDD_L_KNEE, 0.9, 100000);
    move_knee(MIDD_R_KNEE, 1, 100000);
    printf("#%dP%d\n", MIDD_R_HORI, 2400); usleep(10000);
    move_knee(MIDD_R_KNEE, 0.9, 100000);
    move_vert(MIDD_L_VERT, 0, 100000);
    printf("#%dP%d\n", FRON_L_VERT, 2100); usleep(10000);
    printf("#%dP%d\n", FRON_L_KNEE, 800); usleep(10000);
    printf("#%dP%d\n", FRON_R_VERT, 2100); usleep(10000);
    printf("#%dP%d\n", FRON_R_KNEE, 1000); usleep(10000);
    move_vert(MIDD_L_VERT, 0, 100000);
}

void do_coucher(void)
{
    printf("#%dP%d\n", FRON_R_VERT, MAX_R_VERT); usleep(100000);
    printf("#%dP%d\n", FRON_L_VERT, MAX_L_VERT); usleep(100000);
    printf("#%dP%d\n", REAR_R_VERT, MAX_R_VERT); usleep(100000);
    printf("#%dP%d\n", REAR_L_VERT, MAX_L_VERT); usleep(100000);
    printf("#%dP%d\n", MIDD_R_VERT, MAX_R_VERT); usleep(100000);
    printf("#%dP%d\n", MIDD_L_VERT, MAX_L_VERT); usleep(100000);
    printf("#%dP%d\n", FRON_R_KNEE, MIN_R_KNEE); usleep(100000);
    printf("#%dP%d\n", FRON_L_KNEE, MIN_L_KNEE); usleep(100000);
    printf("#%dP%d\n", REAR_R_KNEE, MIN_R_KNEE); usleep(100000);
    printf("#%dP%d\n", REAR_L_KNEE, MIN_L_KNEE); usleep(100000);
    printf("#%dP%d\n", MIDD_R_KNEE, MIN_R_KNEE); usleep(100000);
    printf("#%dP%d\n", MIDD_L_KNEE, MIN_L_KNEE); usleep(100000);
}

void do_coucou(void)
{
    do_debout();
    move_vert(FRON_R_VERT, 1, 100000);
    while(1) {
        printf("#%dP%d\n", FRON_R_KNEE, 1700);
        usleep(1000);
        printf("#%dP%d\n", FRON_R_KNEE, MAX_R_KNEE);
        usleep(1000);
    }
}

int main(int ac, char **av)
{
/*
./a.out dab > /dev/ttyUSB0
./a.out coucou > /dev/ttyUSB0
./a.out couché > /dev/ttyUSB0
./a.out stand > /dev/ttyUSB0
*/
    if (av[1] == NULL)
        return 84;
    if (strcmp(av[1], "stand") == 0)
        do_debout();
    if (strcmp(av[1], "dab") == 0)
        do_dab();
    if (strcmp(av[1], "couché") == 0)
        do_coucher();
    if (strcmp(av[1], "coucou") == 0)
        do_coucou();
    return 0;
}
