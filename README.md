# PDE2400 - Design Engineering Project 2
The project is about creating a Phyton code that can be used to create an animation using 6 strips of leds, each strip include 60 leds, in which makes a total of 360 leds.
I have been working on this code between the period of 4th of jan to 4th of march, by updating my repositories regulary. In this period i developed different kind of animation by making trials and trying to figure out better solutions to make the code looks better.
# I used different types of liberiries for a different porpouses such as:
Import opc is used to call out the simulator, import random to shuffle random colours, import colorsys to intergrate hsv value, import time to display a delay.
To run the code on the simulator we use localhost with port 7890, as you can see below:
# client = opc.Client('localhost:7890')
i used functions at the beginning represent each animation.
# To run the animation:
First you need to open the readopcForStrands to display the animation once you run it.
The code is in the folder called Main, To run it you can simply press on it while the simulator is open. If you would like yo see the code you need to right click on the file and choose edit on IDELE. 
when you press on the file, menu window will display and frm there you can choose a the animation you would like to see by entrying the number next to each of them.
The animation you choose will show in the simulator, if you would like to run a different animation you will need to wait for the current one to end. Once that happened it will asks you to insert a different value to see the next animation.
# types of animation:
I have included 8 different animation in one folder called Main, The first animation is about displaying different collur from right and left. Each coulour will be displyed twice once it reaches the end of second time another colour will take over and keep doing the same until it reaches the end, after that i added a scroll colour that will start from each side and will meet in middle, once its in the middle another scroll will start from there with different colour.
Second animation is adding a different colour pixel in each row, from the left side you will notice a scroll with a different colour once that scroll reaches the last pixel in the row the colour of the scroll will change to the coulour of that pixel and will be displayed in the next row.
third animation is rainbow animation that starts from the left side and moves along all the coloums toghether displaying a different colours until it reaches the end.
fourth animation is crating a star in the middle of the simulator using a colorsys.hsv to assign a colour to it. I created in a way where the right side appears first, then the left side will take over to display the star with the colours assigned to it 
fifth animation will display the netherland flag, using a different scroll in which the the first 2 rows will scroll from lrft to right using a red coulour and the last 2 rows will strat from the right side at the same time using blue colour, one that happend another scroll will start from the midlle with white colour.
sixth animation presents the american flag, using scroll for blue bit from the left, red and white rows for each row until it reachs the end.
seventh animation is the italian flag using the scroll technique similar to one used in the previous animation.
eighth animation will display a red background and three different squares, the colour of the squares will keep changing, i also added a fading to these squares when the back ground start to be become white.
I hope you enjoyed the animation, to end the the simulation you need to exit the code file and the simulator.



