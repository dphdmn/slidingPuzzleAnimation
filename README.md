# slidingPuzzleAnimation
Makes a video of sliding puzzle solve using ffmpeg and image_gen (3x3 - 10x10 supported)

# requires 

2.0 beta executable of image_gen program https://github.com/dphdmn/image_gen/releases/tag/release2.0

ffmpeg installed

# supported customizations

sizes: 3x3 - 10x10, autodetected

tps: any reasonable value

color schemes: hardcoded fringe with rainbow without border at 30 font size (sorry i'm lazy)

# problems
to make it work on windows you may have to fix dependecy issues with svg converter:
```
pip install pipwin
pipwin install cairocffi
```
tested on windows only, but probably does not matter if you compile image_gen yourself and call it image_gen.exe

if you have troubles with losed frames or something, try changing WAITING_TIME_PER_FRAME to higher value, also you can change it to lower value if you are risky (yes i don't want to handle subporcess properly)

# usage example:
```
python main.py "1 6 8 2/5 10 0 7/9 15 11 4/13 12 14 3" "LU2RD3LURULDRURD2LULURURDLULDR2UL2" 30
```
- makes a video of solve at 30 tps

