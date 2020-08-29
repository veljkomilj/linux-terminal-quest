# Terminal Quest Linux Port

This is port of Terminal Quest application from Kano OS which should be able to run on any Linux distribution.

Terminal question is an introduction to terminal commands in the style of text adventure game.

## How to use install it

Install requirements:  
```pip install -r requirements.txt```

Run the game:  
```python2 ./bin/linux-story-gui```

## Repository for the original project
https://github.com/KanoComputing/terminal-quest


## Options

```
linux-story-gui launches the application Terminal Quest at different points in the story.

Usage:
  linux-story-gui [-d | --debug]
  linux-story-gui challenge <challenge> <step> [-d | --debug]

Options:
   -h, --help       Show this message.
   -d, --debug      Debug mode, don't hide the terminal and spellbook widgets by default at the start.
```

Make sure your environment exposes `PYTHONIOENCODING=UTF-8` for correct i18n translations throughout the adventure.
