from tkinter import *
import random

# GAME SETTINGS GO HERE
# CONSTANTS ARE NAMED USING CAPITAL LETTERS SINCE PYTHON DOES NOT HAVE INBUILT CONSTANT DATATYPE WE JUST ASSIGN THEM TO NORMAL VARIABLES
GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#FFFFFF"
FOOD_COLOR = "#EE3344"
BACKGROUND_COLOR = "#000000"

game_running = False

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        
        # Puts default snake coordinates to 0, 0
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
            
        # Draws the snake and appends the starting square
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)
class Food:
    def __init__(self):
        # Generates a random number between 0 and total number of spaces available from our resolution and space size
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        
        self.coordinates = [x, y]
        
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]
    
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    
    # Inserts the new snake coordinate
    snake.coordinates.insert(0, (x, y))
    
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)
    
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        
        score += 1
        
        label.config(text="Score:{}".format(score))
        
        canvas.delete("food")
        
        food = Food()
    
    else:
        # Deletes the last coordinate of the snake
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        
        del snake.squares[-1]
        
    if check_collisions(snake):
        game_over(snake, food)
    else:
         # Loop for refreshing the window
        window.after(SPEED, next_turn, snake, food)
    
def change_direction(new_direction):
    global direction
    
    # Checks if the direction is not a 180 degree turn or not and then changes direction
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction        
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction        

def check_collisions(snake):
    x, y = snake.coordinates[0]
    
    if x < 0 or x >= GAME_WIDTH:
        return True
    if y < 0 or y >= GAME_HEIGHT:
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    
    return False
    
def start_game(snake, food):
    global game_running
    game_running = True
    print("game running", game_running)
    
    next_turn(snake, food)

def restart_game(snake, food):
    if game_running == False:
        canvas.delete(ALL)
                
        snake = Snake()
        food = Food()        
        start_game(snake, food)

def game_over(snake, food):
    global game_running
    game_running = False
    print("game running", game_running)

    del snake
    del food
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=('consolas', 70), text="GAME OVER", fill="white", tag="game_over")

# Creating a window using tkinter
window = Tk()
window.title("Snek")
window.resizable(False, False)

score = 0
direction = 'down'

# The score label
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

# The game canvas
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Centering the window when it appears first on screen
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Keybinds
window.bind("<Left>", lambda event: change_direction('left'))
window.bind("<Right>", lambda event: change_direction('right'))
window.bind("<Up>", lambda event: change_direction('up'))
window.bind("<Down>", lambda event: change_direction('down'))
window.bind("<space>", lambda event: restart_game(snake, food))

snake = Snake()
food = Food()
start_game(snake, food)

window.mainloop()