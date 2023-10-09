The code I have written uses the tkinter library for creating the graphical user interface/canvas for the gamne and the random library for generating random numbers.

The variables written in uppercase are constants which define various settings for the game, such as the width and height of the game window, the speed of the snake, the size of each game space, the initial length of the snake, and colors for the snake, food, and background. The space size represents how much space the snake and the food occupies, the larger the space size, the less boxes we have to move.

The Snake class represents the snake in the game. It has a constructor which initializes the body_size, coordinates and squares of the instance. We use the constant 'BODY_PARTS' to set the starting body_size for our snake. We use nested python lists to store the coordinates of our snake as we need to store the x and y value. We create a list for squares that stores references to the graphical rectangles (squares) drawn on the game canvas to represent each segment of the snake's body. The relationship between coordinates and squares is that each pair of coordinates in the coordinates list corresponds to a graphical square in the squares list. The first for loop is used to put the default snake position to 0, 0. The second for loop is used to loop through the coordinates and fill each square for the coordinates given.

for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

The create_rectangle method takes in the coordiantes for the two opposites corners of the rectangle, so we give in the x and y coordinate and then we add SPACE_SIZE to the x and y coordinate to get the other corner of our rectangle since that is the size we want each of our rectangle to be.


The Food class represents the food that the snake needs to eat. 

x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

We randomly generate a random integer using the random library which has a range of 0 to (GAME_WIDTH / SPACE_SIZE - 1) which is basically dividing the canvas into a bunch of squares which is then multiplied into the space size so we get a coordinate number. We then use the create_oval() method to draw the food onto the canvas.

The next_turn(snake, food) function is responsible for advancing the game by one turn. We first store the snake coordinates into variables x and y. We then add or subtract SPACE_SIZE from our x and y values depending on what movement is made by the player to move the head of our snake to that direction. After this is done we update the snakes coordinates by insterting the new coordinates into the 0th index of our list of coordinates. We then create a new square using the create_rectangle() method on the updated coordinates and add the square into our list of squares. Then we use if and else statements to check for collision with food, i.e if the x coordinate of our snake is equal to the food.coordinate[0] (x coordinate of the food is stored) and the y coordinate of our snake is also equal to the food.coordinate[1] (y coordinate of the food is stored) then those two are on the same block hence our snake has eaten the food so we add the score and delete the food and then create a new food and the else statement happens if there is no collision with food, in which case we delete the last coordinate of the snake and delete the last square of the snake. Then pass an if and else statement which calls the check_collision() method to check for collision of the snake with the frame of our canvas, if the check_collision() method returns true then we invoke the game_over() method, else we keep refreshing the window using the after() method schedules the next_turn function to run again after a delay specified by SPEED. This creates a loop that continuously updates the game state, allowing the snake to move in the chosen direction. It takes the parameteres of time in miliseconds, function to be called and other args which might be needed. 

The change_direction() function allows the player to change the direction of the snake by pressing arrow keys. We define a global variable called direction. We then use nested if and else ifs to stop the snake from taking a 180 degree turn and if the conditions are met, the direction is changed.

The check_collision() function checks if the snake has collided with the game window's boundaries or itself. It loops through all body_parts in the snake.coordinates[] list and checks if x and y are equal to the bodypart[0] (body_part's x coordinate) and body_part[1] (body_part's y coordinate). It returns True if a collision is detected.

The game_over() function is called when the game is over, and it displays a "GAME OVER" message on the screen.