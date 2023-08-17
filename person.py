import picture

class Person:
  '''Defines a Person'''
  def structure():
    '''Creates a structure for the Hangman'''
    #setting pen info
    picture.set_pen_width(10)
    picture.set_position(30, 350)
    picture.set_fill_color("brown")
    picture.set_outline_color("brown")
  
    #drawing the base
    picture.draw_forward(225)
  
    #vertical piece
    picture.set_position(80, 350)
    picture.set_direction(-90)
    picture.draw_forward(300)
  
    #base triangle (left)
    picture.set_position(40, 350)
    picture.set_direction(-60)
    picture.draw_forward(77)
  
    #base triangle (right)
    picture.set_position(120, 350)
    picture.set_direction(-120)
    picture.draw_forward(77)
  
    #horizontal top
    picture.set_position(55, 50)
    picture.set_direction(0)
    picture.draw_forward(250)
  
    #upper triangle
    picture.set_position(150, 50)
    picture.set_direction(150)
    picture.draw_forward(80)
  
    #head holder?
    picture.set_position(255, 50)
    picture.set_direction(90)
    picture.draw_forward(25)
  
  def head():
    '''Draws the head of the hangman (1/6)'''
    #set pen values for our hangman 
    picture.set_pen_width(8)
    picture.set_outline_color("black")
  
    #draw the head
    picture.draw_circle(255, 115, 40)
  
  def body():
    '''Draws the body of the hangman (2/6)'''
    #set pen values
    picture.set_position(255, 155)
    picture.set_direction(90)
  
    #draw the body
    picture.draw_forward(100)
  
  
  def left_arm():
    '''Draws the left arm of the hangman (3/6)'''
    #set pen values
    picture.set_position(255, 200)
    picture.set_direction(-150)
  
    #draw the arm
    picture.draw_forward(80)
  
  def right_arm():
    '''Draws the right arm of the hangman (4/6)'''
    #set pen values
    picture.set_position(255, 200)
    picture.set_direction(-30)
  
    #draw the arm
    picture.draw_forward(80)
  
  def left_leg():
    '''Draws the left leg of the hangman (5/6)'''
    #set pen values 
    picture.set_position(255, 253)
    picture.set_direction(150)
  
    #draw the leg
    picture.draw_forward(80)
  
  def right_leg():
    '''Draws the right leg of the hangman (6/6)'''
    #set pen values
    picture.set_position(255, 253)
    picture.set_direction(30)
  
    #draw the leg
    picture.draw_forward(80)
    

