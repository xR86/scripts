# Make executable out of python script

+ `pip3 install pyinstaller`
+ `pyinstaller script.py`

```bash
pyinstaller --onefile --icon [icon file] [script file]
# Using the --onefile option bundles everything in a single executable file instead of having a bunch of other files
# Using the --icon option adds a custom icon (.ico file) for the executable file
```
