import person as ps
import random as rd
import wordtest as wd
import picture
from PIL import ImageFont

def choose_word(word_len):
  '''Chooses a random word of length defined by the user
  Parameter: User specified length of word
  Returns: random word from list of gpt generated and program validated words'''

#calling the read to list method on the csv file of that particular word length and choosing a random word from that list to play with
  word_list = wd.read_words(word_len)
  word = rd.choice(word_list)
  #print(word)

  return word

def split_word(word):
  '''Splits the randomly chosen word into a list of its component letters
  Parameter: Randomly chosen word of length specified by user
  Returns: list of letters in the word that is to be guessed'''

  #use list to split word into component letters
  split = list(word)

  return split

def dis_vowel(split):
  '''Filters out the vowels in the word, displays vowels and consonants are replaced with "_"
  Parameter: list of letters in the word
  Returns: word as a list of letters with either "_" for consonants and vowels are displayed'''

  #list of vowels
  vowels = ['a', 'e', 'i', 'o', 'u']

  #the starting display word (before guessing begins)
  dis_start = []

  for i in split:
    if i in vowels:
      dis_start.append(i)
    else:
      dis_start.append("_")

  return dis_start
  

def update_word(guess, split, curr_word):
  '''Based on the (correct) guess made by the user, this function updates the current word to display the word after the guess
  Parameters: 
  Guess: the guessed letter 
  split: the word that the user is guessing, in list form
  curr_word: the state of the word right now, given the past guesses
  
  Returns: the updated word with the guessed letter'''

  #noting the index/indices of the letter in the word
  index = []

  #curr index keeps track of the index number at which the guessed letter occurs
  curr_index = 0
  for x in split:
    if guess == x:
      index.append(curr_index)
      curr_index += 1

    else:
      curr_index += 1

  #edits the current word by replacing the "_" with the guessed letter
  for i in index:
    curr_word[i] = guess
    
  return curr_word

def img_txt(curr_word):
  '''Displays the current state of the word in the picture created
  Parameter: current word, given the guesses made
  Returns: None'''
  #setting font
  font = ImageFont.truetype('Roboto-Medium.ttf', size=35)
  
  x_curr = 50

  #for loop to place each letter of the word at a given distance from the previous letter
  for i in curr_word:
    picture.DRAW.text((x_curr, 6), i, font=font, fill="black", width=1)
    x_curr += 40


def img_part(guess_left):
  '''Calls the methods from the Person Class for different parts of the body for each incorrect guess that is made
  Parameter: number of guesses left
  Returns: None'''
  if guess_left == 5:
    ps.Person.right_leg()

  elif guess_left == 4:
    ps.Person.left_leg()
    
  elif guess_left == 3:  
    ps.Person.right_arm()
    
  elif guess_left == 2:
    ps.Person.left_arm()
  
  elif guess_left == 1:
    ps.Person.body()

  elif guess_left == 0:
    ps.Person.head()

 
def main():
  #prints rules of the game for the user
  print("Welcome to Hangman!")
  print("The rules of the game are simple: guess the incomplete word before the Hangman is complete! Only guess consonants, the vowels of the word have already been filled in for you. Best of luck!")
  print()
  print("Word lengths: 5, 6, 7 and 8!")

  #while loop to account for user input being beyond the scope of the program
  while True:
    #try except block to account for user input being not an integer
    try:
      word_len = int(input("Length of the word with which you'd like to play: "))
      
      if word_len == 5 or word_len == 6 or word_len == 7 or word_len == 8:
        word = choose_word(word_len)
        break
      else:
        print("Invalid choice! Please choose a number between 5 and 8!")
    except:
      print("Invalid input! Please choose a number between 5 and 8!")
  
  #setting up the canvas
  picture.new_picture(400, 400)

  #drawing a background and the structure
  picture.set_fill_color("white")
  picture.set_outline_color("white")
  picture.draw_filled_square(0,0, 400)
  ps.Person.structure()
  
  #splitting the randomly chosen word into it's letters
  split = split_word(word)

  #displaying the guess word with only the vowels
  display = dis_vowel(split)

  #current word before guessing is the word with only vowels
  curr_word = display

  #producing text in the image to display the word that needs to be guessed
  img_txt(curr_word)
  
  picture.display()

  #listing a list of consonants (valid user input)
  consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

  #setting guess parameters
  guess_lim = 6
  current = 0

  #creating a list of the letters that have already been guessed
  guessed = []
  
  guess_left = guess_lim - current

  #while loop to ensure the guess prompt is repeatedly asked until the guesses left are 0 or the word has been guessed by the user
  while guess_left != 0 and curr_word != split:
      while True:
        guess = input("Guess a letter: ")
        if guess in consonants:
          break
        else:
          print("Invalid guess! Please guess a consonant!")
    
      if guess in split:
        print("Your guess was corrct :)")
        current = current 
        guess_left = guess_lim - current
        #updates the word based on the correct guess
        update = update_word(guess, split, curr_word)
        #sets the current word as the updated word
        curr_word = update
        img_txt(curr_word)

        
      else:
        print("Your guess was incorrct :(")
        #calls the img_part funtion to add an additional body part on the hangman after an incorrect guess
        img_part(current)
        picture.display()
        current += 1
        guess_left = guess_lim - current
        
        curr_word = curr_word
        img_txt(curr_word)

      
      #adds the guessed letter to the list of letters that have already been guessed
      print(guessed)
      guessed.append(guess)
      

      print("You have", guess_left, "incorrect guesses left!")
      print()
      print("You have already guessed the following: ", guessed)
      picture.display()
    
    

  if curr_word == split:
    print("Congratulations! You guessed the word!")

  else:
    print("You were unable to guess the word! The word was", word)

if __name__ == "__main__":
  main()

  