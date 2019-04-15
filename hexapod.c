#define MAX_LEFT_KNEE   "2500"
#define MIN_LEFT_KNEE   "500"
#define MAX_RIGHT_KNEE  "2500"
#define MIN_RIGHT_KNEE  "500"

#define MAX_LEFT_VERT   "500"
#define MIN_LEFT_VERT   "2500"
#define MAX_RIGHT_VERT  "2500"
#define MIN_RIGHT_VERT  "500"

#define MAX_LEFT_HORIZ  "500"
#define MIN_LEFT_HORIZ  "2500"
#define MAX_RIGHT_HORIZ "2500"
#define MIN_RIGHT_HORIZ "500"


#define FRONT__LEFT__KNEE  "26"
#define FRONT__RIGHT_KNEE  "10"
#define MIDDLE_LEFT__KNEE  "22"
#define MIDDLE_RIGHT_KNEE  "06"
#define REAR___LEFT__KNEE  "18"
#define REAR___RIGHT_KNEE  "02"

#define FRONT__LEFT__VERT  "25"
#define FRONT__RIGHT_VERT  "09"
#define MIDDLE_LEFT__VERT  "21"
#define MIDDLE_RIGHT_VERT  "05"
#define REAR___LEFT__VERT  "17"
#define REAR___RIGHT_VERT  "01"

#define FRONT__LEFT__HORIZ "24"
#define FRONT__RIGHT_HORIZ "08"
#define MIDDLE_LEFT__HORIZ "20"
#define MIDDLE_RIGHT_HORIZ "04"
#define REAR___LEFT__HORIZ "16"
#define REAR___RIGHT_HORIZ "00"

#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    char str[24];

    sprintf(str, "echo '#%sP%sT%s'", FRONT__LEFT__KNEE, MAX_LEFT_KNEE, "1000");
    system(str);
}
