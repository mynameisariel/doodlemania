# Doodlemania

Doodlemania is a charades or pictionary style drawing game designed for two players.

## Features

In this game, two players play as a team, and try to get as many points as possible, while enjoying artistic features of the game.

- They can take turns receiving a randomly generated prompt, then drawing it on a canvas while the other player tries to guess the prompt
- There is a timer for the amount of time it takes for the prompt to be guessed
- The less time it takes, the more points the players get
- Six screens: Welcome, Instructions, Attention, Prompt, Drawing, and Finish

## Installation

**Pygame package** is needed to run the game GUI and visuals. The [pip](https://pip.pypa.io/en/stable/) package manager can be used.

```python
pip install pygame
```

Other library imports are also needed:

- **time** library
- **random** library
- **ctypes** library
- **datetime** library
- **sys** library

Imports should look like the following:

```python
from datetime import datetime
import sys
import pygame
import ctypes
import random
```

## Known Bugs

**Drawing bug:** This is a bug that occurs on the school computer, but not on my personal device at home, so I am not sure what the issue it. At home, it runs fine on Visual Studio Code, but on the school device using Thonny, this bug will happen. When holding down the mouse to the left of the canvas, a horizontal line will appear on the canvas.

## Cheat Codes

At the prompt screen, look at the prompt and click the "next" button. Then, enter the prompt that you saw into the text box during the drawing phase to avoid wasting time drawing and guessing.

## Support

Please contact the developer, Ariel Liu, at aliu11@ocdsb.ca for support or feature requests.

## Sources

[1] R. Sharma, “42 exciting Python Project Ideas & Topics for beginners in 2023 [latest],” upGrad blog, https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/ (accessed Jun. 3, 2023).

[2] S. Gyger, “How to make a drawing program in Python,” Python Code, https://www.thepythoncode.com/article/make-a-drawing-program-with-python (accessed Jun. 3, 2023).

[3] M. Maeder, “How to make buttons in PyGame,” Python Code, https://www.thepythoncode.com/article/make-a-button-using-pygame-in-python (accessed Jun. 3, 2023).

[4] G. A. Hjelle, “Python timer functions: Three ways to monitor your code,” Real Python, https://realpython.com/python-timer/ (accessed Jun. 3, 2023).

[5] D. Potato, “Menus - pygame tutorial,” YouTube, https://www.youtube.com/watch?v=0RryiSjpJn0 (accessed Jun. 3, 2023).

[6] B. Tech, “How to make a menu screen in PYGAME!,” YouTube, https://www.youtube.com/watch?v=GMBqjxcKogA (accessed Jun. 3, 2023).

[7] Ankthon, “Python: Display text to Pygame Window,” GeeksforGeeks, https://www.geeksforgeeks.org/python-display-text-to-pygame-window/ (accessed Jun. 3, 2023).

[8] “Welcome to making apps with Pygame!,” Welcome to making apps with Pygame! - Pygame tutorial 2019 documentation, https://pygame.readthedocs.io/en/latest/index.html (accessed Jun. 3, 2023).

[9] “HTML color codes,” HTML Color Codes, https://htmlcolorcodes.com/ (accessed Jun. 4, 2023).

[10] B. Weber, “Python enumerate(): Simplify looping with counters,” Real Python, https://realpython.com/python-enumerate/ (accessed Jun. 4, 2023).

[11] “More sugar font,” 1001 Free Fonts, https://www.1001freefonts.com/more-sugar.font (accessed Jun. 4, 2023).

[12] Edu GrandoEdu Grando 41511 gold badge44 silver badges55 bronze badges et al., “What fonts can I use with pygame.font.font?,” Stack Overflow, https://stackoverflow.com/questions/38001898/what-fonts-can-i-use-with-pygame-font-font (accessed Jun. 4, 2023).

[13] “HANGMAN CODE,” Chapter 8 - writing the Hangman Code, https://inventwithpython.com/invent4thed/chapter8.html (accessed Jun. 4, 2023).

[14] C. Edwards, “changeScreens.py,” Google drive, https://drive.google.com/file/d/1r77x1Sm-X_ze-i3m8iXF8kXYSBgdek8u/view?pli=1 (accessed Jun. 4, 2023).

[15] C. Edwards, “Pygamebuttons,” replit, https://replit.com/@CourtneyEdwards/pygameButtons#main.py (accessed Jun. 4, 2023).

[16] C. Code, “Python / pygame tutorial: Getting text input,” YouTube, https://www.youtube.com/watch?v=Rvcyf4HsWiw&ab_channel=ClearCode (accessed Jun. 4, 2023).

[17] C. Edwards, “Timerpause,” replit, https://replit.com/@CourtneyEdwards/timerPause#main.py (accessed Jun. 4, 2023).

[18] Canva, “Free design tool: Presentations, video, social media | CANVA,” Canva, https://www.canva.com/ (accessed Jun. 5, 2023).
