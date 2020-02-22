import time
import busio
import digitalio
import board

from adafruit_rgb_display import color565
import adafruit_rgb_display.st7789 as driver

CS_PIN = board.CE0
DC_PIN = board.D25
reset_pin = None
BAUDRATE = 6400000
spi = board.SPI()

display = driver.ST7789(spi, cs=digitalio.DigitalInOut(CS_PIN), dc=digitalio.DigitalInOut(DC_PIN), rst=reset_pin, baudrate=BAUDRATE, width=240, height=240, x_offset=0, y_offset=80)


green = color565(0,0,255)

#display.pixel(120,120,green)
#for i in range(0,200):
#	for j in range(0,200):
#		display.pixel(i,j,green)
slider = 0
foward=True
while True:
	time.sleep(0.03)
	if(slider == 255):
		forward=False
	if(slider == 0):
		forward=True
	display.fill(color565(255-slider,slider,0))
	slider = slider + 1 if forward else slider - 1
