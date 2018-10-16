# Poker Calculator

## Introduction
Poker Calculator computes the strength of your hand in a Texas Hold'em Poker game.

## Background
This project was inspired when we joined an AI Poker tournament. There are a lot of libraries out there that helps you calculate the strength of your hand, and one of the more famous ones is Deuces. You can find its project page here: [worldveil/deuces](https://github.com/worldveil/deuces)

Deuces gives you a numerical score based on your hole cards and the community cards. A Royal Flush is scored as **"1"** and an unsuited 7-5-4-3-2 as **"7462"**.  

What this Poker Calculator aims to do is to get your Deuces score and run a Monte Carlo simulation out of it. For example: 
  * You have a Queen of Spades and Ten of Hearts
  * The board is Ace of Hearts, King of Diamonds, and Jack of Clubs
  * Your Deuces score is: 1600
  * What do you do? Call? Raise? Fold?
  
Sometimes knowing your Deuces score is not enough, so we will be fighting an "imaginary opponent".
  * We will be drawing cards from the deck that are still available. 
  * We will compute its Deuces score.
  * We will compare the score and if you have the lower one, you get a point. If not, you receive nothing.
  * Repeat as many times as you want. You count your points and divide it to the number of games you had. 
  * That is your winning percentage. 
  
Now you have a Deuces score and a winning percentage. Making a move will be much easier.

## Requirements
  * Python 3.x


## Running the Application

Poker Calculator can be ran in two ways:
1. Console application
2. Web API

### Console Application
Running the console application will display your winning percentage in the terminal.
```
python PokerCalculatorMain.py --board As Tc 3d --hand Ah Ad
(1646, 'Three of a Kind')
0.964
```
  * Three board cards are required to run.
  * Two hand cards are required to run.
  * Card format is `Rs` where `R` is the rank (A for ace, 2 to 9, T for 10, JQK for Jack, Queen, and King respectively) and 's' is the suit (d for diamonds, h for hearts, c for clubs and s for spades)
  * `1646` is the Deuces score. The lower the number, the better.
  * `0.964` is the winning percentage.

### Web API
Running the Web API will make Poker Calculator available via web calls.
```
python WebApp.py
```
  * Default settings will run the Web API at 0.0.0.0:8080
  * Address is: `poker?board={}&hand={}`
  * Three board cards are required to run.
  * Two hand cards are required to run.
  * Card format is `Rs` where `R` is the rank (A for ace, 2 to 9, T for 10, JQK for Jack, Queen, and King respectively) and 's' is the suit (d for diamonds, h for hearts, c for clubs and s for spades)
  * Sample API call: `http://127.0.0.1:8080/poker?board=AsAdAcQsKd&hand=Kh2d`