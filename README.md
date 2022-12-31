# slidingPuzzleAnimation
Makes a video of sliding puzzle solve using ffmpeg and image_gen (3x3 - 10x10 supported)

requires 2.0 beta executable of image_gen program https://github.com/dphdmn/image_gen/releases/tag/release2.0

requires ffmpeg installed

tested on windows only, but probably does not matter if you compile image_gen yourself and call it image_gen.exe

usage example:

python main.py "1 6 8 2/5 10 0 7/9 15 11 4/13 12 14 3" "LU2RD3LURULDRURD2LULURURDLULDR2UL2" 30

- makes a video of solve at 30 tps

supported sizes: 3x3 - 10x10, autodetected
