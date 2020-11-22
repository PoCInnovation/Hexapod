# Getting started

## Wire everything

To communicate with the Hexapod's board you need to wire:

The power:

-  `VS2+` from the Hexapod to a `5V` pin on your board
-  `VS2-` from the Hexapod to a `GND` pin on your board

The [serial communication](https://learn.sparkfun.com/tutorials/serial-communication/wiring-and-hardware):
-  `TX` from the Hexapod to the `RX` pin of your board
-  `RX` from the Hexapod to the `TX` pin of your board
-  `G` from the Hexapod to a `GND` pin of your board.



## Set up the communication

In order to talk to the hexapod you need to set up a serial communication.

The Hexapod's board reads the serial and interpret commands.

As an example, here is how to do it with Arduino (wtth the SoftwareSerial Library) :

```cpp
#include <SoftwareSerial.h>

SoftwareSerial mySerial(2, 3); // RX, TX

void setup()
{
  // Open serial communications (with pc) and wait for port to open:
  Serial.begin(115200);
  while (!Serial) {
    // wait for serial port to connect
  }
  
  // set the data rate for the SoftwareSerial port
  mySerial.begin(38400);
  
  Serial.println("Goodnight moon!"); // print to pc
  mySerial.println("Hello, world?"); // print to custom serial port (aka hexapod)
}

void loop()
{
}

```



## Commands

**Deplacements:**

In order for the order the hexapod's board to position a servo, you must send a serial command in the following format. 

```
# <ch> P <pw> S <spd> T <time> <cr>
```

-  <ch>: pin / channel to which the servo is connected (0 to 31) in decimal

-  <pw>: desired pulse width (normally 500 to 2500) in microseconds

- *-<spd>*: servo movement speed in microseconds per second*

- *<time>*: time in microseconds to travel from the current position to the desired position. This affects all servos (65535 max)

- <cr>: carriage return (ASCII 13)**

Example:

```
#5P1500S750<cr>
```



You can also combine commands in order to go faster

```
#5P1600#17P750S500#2P2250T2000<cr>
```



**Query movements status**

You can check if a movement was completed with

```
Q<cr>
```

This will return a "." if the previous move is complete, or a "+" if it is still in progress.

It is useful if you want to check if the hexapod movement did not encounter an obstacle. 



## More

For more detailed information you should read the [lynxmotion documentation](./Doc/lynxmotion_ssc-32u_usb_user_guide.pdf)

It has more commands explained and more details about the board, it's a must if you want to know everything about the board.