// Adafruit NeoPixel - Version: 1.2.3
#include <Adafruit_NeoPixel.h>

/*

 */

#define LED_PIN 6
#define LED_COUNT 6

#define pSpace 0
#define rSpace 0    
#define gSpace 0
#define bSpace 255 

#define pReality 1
#define rReality 255    
#define gReality 0     
#define bReality 0    

#define pPower 2
#define rPower 100
#define gPower 0
#define bPower 100

#define pMind 3
#define rMind 255  
#define gMind 200   
#define bMind 0    

#define pTime 4
#define rTime 0    
#define gTime 255  
#define bTime 0    

#define pSoul 5
#define rSoul 255
#define gSoul 150
#define bSoul 0

char buf[80];  //serial buffer?
Adafruit_NeoPixel pixels(LED_COUNT, LED_PIN, NEO_GRB); //declaring the NeoPixel object

int flashLoops = 3;
int flashOn = 500;  // in milliseconds
int flasOff = 200;  // in milliseconds

void setup() {

  pixels.begin();
  pixels.show();
  Serial.begin(115200);

}

void loop() {
  if (readline(Serial.read(), buf, 80) > 0) {
    doLights(atoi(buf));
  }
}

void flashPixels(int rColor, int gColor, int bColor)
{


  for (int i = 1; i <= 3; i++)  {
    pixels.fill(pixels.Color(rColor, gColor, bColor));
    pixels.show();
    delay(500);
    pixels.fill(pixels.Color(0, 0, 0));
    pixels.show();
    delay(200);
  }
}

void doLights(int fromPi)
{
  switch (fromPi) {
  case 70:  //flash Space
    flashPixels(rSpace, gSpace, bSpace);
    break;
  case 71: //flash Reality
    flashPixels(rReality, gReality, bReality);
    break;
  case 72: //flash Power
    flashPixels(rPower, gPower, bPower);
    break;
  case 73: //flash Mind
    flashPixels(rMind, gMind, bMind);
    break;
  case 74: //flash Time
    flashPixels(rTime, gTime, bTime);
    break;
  case 75: //flash Soul
    flashPixels(rSoul, gSoul, bSoul);
    break;
  case 90:
    rainbow(5);
    break;
  case 99: //turn off the pixels
    pixels.fill(pixels.Color(0,0,0));
    pixels.show();
    break;
  default:
    if (fromPi % 2)  //start with the 1 bit, Space
      pixels.setPixelColor(pSpace,pixels.gamma32(pixels.Color(rSpace, gSpace, bSpace)));
    else
      pixels.setPixelColor(pSpace, 0, 0, 0);

    fromPi = fromPi / 2 ; //shift to the 2 bit, Reality
    if (fromPi % 2)
      pixels.setPixelColor(pReality,pixels.gamma32(pixels.Color(rReality, gReality, bReality)));
    else
      pixels.setPixelColor(pReality, 0, 0, 0);

    fromPi = fromPi / 2 ; //shift to the 4 bit, Power
    if (fromPi % 2)
      pixels.setPixelColor(pPower,pixels.gamma32(pixels.Color(rPower, gPower, bPower)));
    else
      pixels.setPixelColor(pPower, 0, 0, 0);

    fromPi = fromPi / 2 ; //shift to the 8 bit, Mind
    if (fromPi % 2)
      pixels.setPixelColor(pMind,pixels.gamma32(pixels.Color(rMind, gMind, bMind)));
    else
      pixels.setPixelColor(pMind, 0, 0, 0);

    fromPi = fromPi / 2 ; //shift to the 16 bit, Time
    if (fromPi % 2)
      pixels.setPixelColor(pTime,pixels.gamma32(pixels.Color(rTime, gTime, bTime)));
    else
      pixels.setPixelColor(pTime, 0, 0, 0);

    fromPi = fromPi / 2 ; //shift to the last bit (32), Soul
    if (fromPi % 2)
      pixels.setPixelColor(pSoul,pixels.gamma32(pixels.Color(rSoul, gSoul, bSoul)));
    else
      pixels.setPixelColor(pSoul, 0, 0, 0);

    //Now show the pixels
    pixels.show();
  }
}

//yeah, I *borrowed* this code from someone.

int readline(int readch, char *buffer, int len) {
  static int pos = 0;
  int rpos;

  if (readch > 0) {
    switch (readch) {
    case '\r': // Ignore CR
      break;
    case '\n': // Return on new-line
      rpos = pos;
      pos = 0;  // Reset position index ready for next time
      return rpos;
    default:
      if (pos < len - 1) {
        buffer[pos++] = readch;
        buffer[pos] = 0;
      }
    }
  }
  return 0;
}

// Rainbow cycle along whole strip. Pass delay time (in ms) between frames.
void rainbow(int wait) {
  // Hue of first pixel runs 5 complete loops through the color wheel.
  // Color wheel has a range of 65536 but it's OK if we roll over, so
  // just count from 0 to 5*65536. Adding 256 to firstPixelHue each time
  // means we'll make 5*65536/256 = 1280 passes through this outer loop:
  for(long firstPixelHue = 0; firstPixelHue < 5*65536; firstPixelHue += 256) {
    for(int i=0; i<pixels.numPixels(); i++) { // For each pixel in strip...
      // Offset pixel hue by an amount to make one full revolution of the
      // color wheel (range of 65536) along the length of the strip
      // (strip.numPixels() steps):
      int pixelHue = firstPixelHue + (i * 65536L / pixels.numPixels());
      // strip.ColorHSV() can take 1 or 3 arguments: a hue (0 to 65535) or
      // optionally add saturation and value (brightness) (each 0 to 255).
      // Here we're using just the single-argument hue variant. The result
      // is passed through strip.gamma32() to provide 'truer' colors
      // before assigning to each pixel:
      pixels.setPixelColor(i, pixels.gamma32(pixels.ColorHSV(pixelHue)));
    }
    pixels.show(); // Update strip with new contents
    delay(wait);  // Pause for a moment
  }
} 

