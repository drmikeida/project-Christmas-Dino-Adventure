import pyxel
import random

class App:
    def __init__(self):
        # Initialize the Pyxel window (width, height)
        pyxel.init(180, 120)

        # Set the initial position of the square
        self.x = 51
        self.y = 10
        self.score = 0

      
        # Set the initial position and velocity of the sprite
        self.sprite_x = 40
        self.sprite_y = 10
        self.sprite_dx = 4
        self.sprite_dy = 4
        self.sprite_2x = 43
        self.sprite_2y = 12
        self.sprite_2dx = 3
        self.sprite_2dy = 3
      

        
        # Start the game loop
        pyxel.run(self.update, self.draw)

    def update(self):
        # Update the square's position based on arrow keys
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2

        # Simple interaction: Increase score when square reaches top-left corner
        

        # Update the sprite's position
        self.sprite_x += self.sprite_dx
        self.sprite_y += self.sprite_dy

        #code for cactus
        self.sprite_2x += self.sprite_2dx
        self.sprite_2y += self.sprite_2dy

        # Bounce the sprite off the edges of the screen
        if self.sprite_x <= 0 or self.sprite_x >= 180:
            self.sprite_dx *= -1
        if self.sprite_y <= 0 or self.sprite_y >= 120:
            self.sprite_dy *= -1
        
    # Bounce the cactus sprite off the edges of the screen
        if self.sprite_2x <= 0 or self.sprite_2x >= 180:
             self.sprite_2dx *= -1
        if self.sprite_2y <= 0 or self.sprite_2y >= 120:
             self.sprite_2dy *= -1
# when dino goes near coin, increase score
     
        if abs(self.x - self.sprite_x) <= 20 and abs(self.y - self.sprite_y) <= 20:
            self.score += 1
        # when dino goes near cactus, down by 1
        if abs(self.x - self.sprite_2x) <= 20 and abs(self.y - self.sprite_2y) <= 20:
            self.score -= 1
    def draw(self):
        # Clear the screen with black (color 0)
        pyxel.cls(5)

        # Draw dino (color 9)
        
        pyxel.load("my_resource.pyxres")
        pyxel.blt(self.x, self.y, 0, 0, 0, 200, 206, 0)

        # Draw the moving sprite (coin) (color 11)
       
        # pyxel.circ(self.sprite_x, self.sprite_y, 5, 11)
        
        pyxel.blt(self.sprite_x, self.sprite_y, 1, 0, 0, 200, 206, 0)



        
        

        # Display the score 
        pyxel.text(5, 5, f"Score: {self.score}", 7)
        # display game rules
       
        pyxel.text(5, 10, "touch the coin to increase your score", 3)
        pyxel.text(5, 15, "cactus = -1 score deduction", 3)
        

        # Display a message when score is high, cactus will appear when player gets 50 or higher points.
        if self.score >= 5:
            pyxel.text(50, 50, "new level unlocked!", 8) 
        
        if self.score >= 5:
            pyxel.blt(self.sprite_2x, self.sprite_2y, 2, 0, 0, 20, 20, 0)

       
        
        






# Run the game
App()

