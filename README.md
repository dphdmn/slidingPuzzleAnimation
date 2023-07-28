# Sliding Puzzle Animation with ffmpeg and image_gen

SlidingPuzzleAnimation is a Python script that creates captivating videos of sliding puzzle solutions using ffmpeg and image_gen. This versatile script supports various puzzle sizes, ranging from 3x3 to 10x10, with automatic detection of the dimensions. The animation's smoothness is adjustable, allowing you to set any reasonable value for turns per second (tps).

## Requirements

Before running the script, ensure you have the following dependencies installed:

1. **image_gen 2.0 beta executable**: Obtain it from [here](https://github.com/dphdmn/image_gen/releases/tag/release2.0)

2. **ffmpeg**: Ensure ffmpeg is installed on your system.

## Supported Customizations

The SlidingPuzzleAnimation script offers several customization options to tailor your videos:

- **Sizes**: Create sliding puzzles with dimensions ranging from 3x3 to 10x10. The script automatically detects the size based on your input.

- **Turns Per Second (tps)**: Control the smoothness of the animation by specifying any reasonable value for the ticks per second.

- **Color Schemes**: The script currently supports a hardcoded fringe with a rainbow, without borders, at a font size of 30. Note that additional color schemes can be added in the future.

## Known Issues

For Windows users, you may encounter dependency issues with the SVG converter. To resolve this, execute the following commands:

```
pip install pipwin
pipwin install cairocffi
```

The script has been primarily tested on Windows. However, it should work on other platforms if you manually compile image_gen into an executable named "image_gen.exe."

If you experience dropped frames or other issues during video generation, adjusting the WAITING_TIME_PER_FRAME variable may help. Increase its value for better results or decrease it if you prefer a riskier approach. Please be aware that proper subprocess handling has not been implemented in this version.

## Usage Example

To create a video of a sliding puzzle solution at 30 tps, use the following command:

```
python main.py "1 6 8 2/5 10 0 7/9 15 11 4/13 12 14 3" "LU2RD3LURULDRURD2LULURURDLULDR2UL2" 30
```

Unlock the potential of your favorite sliding puzzles with SlidingPuzzleAnimation and share your mesmerizing solutions with the world!
