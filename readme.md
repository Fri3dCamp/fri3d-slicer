# Fri3d Camp 2020 pattern slicer

This Python3 script slices up the Fri3d Camp pattern into tiles which you can use in creative ways. It can also easily be adapted to slice any image.

![pattern](pattern.png)

## Requirements

- Python 3.x, you can probably make the syntax compatible with Python 2.7, but why would you?
- Pillow is the Python 3 compatible PIL fork. You can install it with `pip3 install Pillow` (in cases where `pip` is specific to ye olde Python)

## Howto

Basically, you just do `python3 slicer.py` (or `python slicer.py`) in the project's directory (where this readme is) and if all files are where they should be, you should see this output:

```
creating tileset 'baseset' 
Creating tile:tiles/baseset-0-0.png
Creating tile:tiles/baseset-600-0.png
Creating tile:tiles/baseset-1200-0.png
Creating tile:tiles/baseset-1800-0.png
Creating tile:tiles/baseset-2400-0.png
Creating tile:tiles/baseset-3000-0.png
...
```

The `tiles` dir in project's directory should be created if it doesn't yet exist. And you will see it fill up with png files as the script runs. The files in this directory are *not* deleted when the script is run, but newer files with the same name will overwrite the older ones.

The input file (`pattern.png`) and output path (`tiles`) are set at the top of `slicer.py`, so you can change them there easily. Support for command line parameters or a config file is planned, or you can add it yourself (and send me a PR please 🙏).

## Slice map

The file `slicemap.py` contains the actual slicing parameters, in the form of a Dict. For starters, it contains a `baseset` array. This array consists of couples of coördinates, each defining a rectangular slice by its top left and bottom right corners. You can create other named sets within the slicemap dict, defining other areas for slicing. These will also be created when `slicer.py` is run. The set's name is prefixed to the file names.