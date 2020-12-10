# CWG Utimate Warrior game
****
|Authors|Chao Cui, Nandi Guo, Hao Wu
|---|---
|Group|CWG
|Game name|Utimate Running
|Language|Python
|Version|1.0
****

## Background
The game is a parkour type game, developed in python and uses mainly pygame content.

## Environment
* macOS or Windows
* python (3.6+)
* pip

## Contents
* pycache
* Images
* Sounds

****
* CONTRIB.pdf
  * Individual contribution to the project
* DISTRIPTION.pdf
  * Discription of the game
* README.md
  * Installation instructions
****

* Game_Modes.py
  * Assign different difficulty levels to the game. And when the easy, normal and hard three difficulty levels of gems are collected enough 100 or more, you can unlock the    ultimate level.
* How_to_play.py
  * The player is taught how to operate the game and is told the background of the game and the conditions of the game.
* Start_Screen.py
  * Generate characters, obstacles and gems for the game. 
* Congratulation.py
  * When the goals of the game are all achieved, the pop-up interface tells the player that the game passes.
* Main_Game.py
  * Generate characters, obstacles and gems for the game and allow players to play the game
* Open.py
  * Start the entire game program

## Instruction
After completing the environment configuration and dependency installation, you can run the Open.py File mode to run the project.
## Install pygame in Window 10 
### Step 1: PIP installation and upgrade
* Checking if PIP is installed
Type PIP into cmd and if a large field of characters appears, it means that PIP is installed.
* Raise and lower pip to the latest
```cmd
$ python -m install pip --upgrade pip
```

### Step 2: Install Pygame
* Open the cmd and copy and execute :
```cmd
$ python -m pip install pygame --user
```
* The PIP will then automatically download and install Pygame.
* Once the installation is complete, you will be prompted with a successful installation.
#### [Important tips]
* If typing "python -m pip install pygame --user" does not solve the problem, try changing the code from pip to pip3, or removing --user.
* Alternatively, run:
```cmd
$ pip install pygame
```
#### To check if Pygame is installed successfully
1, open cmd and type python
2, type import pygame. if no error is reported, the installation is successful and the Pygame version number will be indicated.


