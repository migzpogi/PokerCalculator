# Poker Calculator

## Introduction
This project was inspired when we joined an AI Poker tournament. There are a lot of libraries out there that helps you calculate the strength of your hand and one of the more famous ones is Deuces. You can find its project page here:[worldveil/deuces](https://github.com/worldveil/deuces) 

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


