# Abstract
This repo is created to work together for Programming with Python course midterm project.

# Required Features
- Displaying unnamed.gif (unnamed map) on the screen. (we used turtle module for that.)
- Displaying a text box on the screen. Then asking province name in Turkey. (we used a turtle module function for that as well.)
- User enters a province name and then:
  - The province name appears on the corresponding position on the map.
  - If the province name is already entered, displaying a warning message.
  - If the province name does not exists, displaying a warning message.
- When all province names are entered correctly, ending the game.
- We used a dict list to store provinces details.
- On top of the screen placing a text indicating how many states are guessed correctly and how many states are total.

# Extra Features
- When user enters a duplicate entry (the province is already exists) the program draws an ellipse/circle to show the exists province.
- There is a score algorithm to make the game more efficieny.
  - If the user guessed province minimum 2 times in a row, the stack increases linearly.
  - Score calc is easy. if stack is > 1 `added_score = ((stack-1) * 5) + 10` else `added_score = 10`
  - There is a motivation words such as "Amazing", "You are on fire!!!" which is displaying according to stack.
- We are displaying score and added_score on the top of the screen.
- There is a wildcards feature.
  - User has only 5 wildcards.
  - User can use it by typing 'h' as input
  - If the user stucks, can use the wildcards.
  - If the user uses it, they will get the score but he/she will lost the stacks.

# Contributors
- [Ilayda Bakırcıoğlu](https://github.com/ilaydabkrc)
- [Mehmet Ali Mergen](https://github.com/mehmetali10)
- [Burak Taşçı](https://github.com/tscburak)
