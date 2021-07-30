#include <stdio.h>
#include <wiringPi.h>
  
#define LED1 14
#define LED2 15

int main(){
    if(wiringPiSetupGpio() < 0){
	printf("Unable to setup wiring Pi");
	return 1;
    }

    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);

    for(;;){
	digitalWrite(LED1, 1);
	delay(1000);
	digitalWrite(LED1, 0);
	delay(1000);
	digitalWrite(LED2, 1);
	delay(1000);
	digitalWrite(LED2, 0);
	delay(1000);
    }
    return 0;
}
