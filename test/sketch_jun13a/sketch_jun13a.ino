#include <LiquidCrystal.h>

int redled = 12;
int greenled = 2;

void setup()
{
  pinMode(redled, OUTPUT);
  pinMode(greenled, OUTPUT);
}

void loop()
{
  batterylevel();
}

void batterylevel()
{
  //read the voltage and convert it to volt
  double curvolt = double( readVcc() ) / 1000;
  
  // check if voltge is bigger than 4.2 volt so this is a power source
  if(curvolt < 5)
  {
    //batterie déchargée

    //led rouge allumée
    digitalWrite(redled, HIGH);

    //led verte éteinte
    digitalWrite(greenled, LOW);
  }
  else
  {
    //batterie ok
    
    //led verte allumée
    digitalWrite(greenled, HIGH);
    
    //led rouge éteinte
    digitalWrite(redled, LOW);
  }
}

//read internal voltage
long readVcc() {
  long result;
  
  return result;
}
