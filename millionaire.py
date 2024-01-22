#################################### QUEM QUER SER MILIONÁRIO ####################################
##################################################################################################
# This is a project for CodeCademy Computer Science Career! 
##################################################################################################

# Let's create a Who Want to Be a Millionaire quiz using classes. 

import random

class WhoWantsToBeaMillionaire:
# We're gonna need:
# - We first need to print() a string presenting the show and that the user must have to answer all questions in order to win the prize
  # of 1 million euros. 
# - To begin with 0
# - We need to create an array with the questions
    # We have to divide the question from easy to hard
    # For each one we need an array of answers being one of them correct 
# - We must have the user interaction to give us the answer
# - Computer must give feedback if the user lost or not and if lost he will lose money
  easy_questions = [
    {
        'question': 'What is the largest ocean in the world?',
        'options': ['A. Atlantic Ocean', 'B. Indian Ocean', 'C. Southern Ocean', 'D. Pacific Ocean'],
        'correct_answer': 'D'
    },
    {
        'question': 'Which country is known as the Land of the Rising Sun?',
        'options': ['A. China', 'B. South Korea', 'C. Japan', 'D. Vietnam'],
        'correct_answer': 'C'
    },
    {
        'question': 'Who painted the Mona Lisa?',
        'options': ['A. Pablo Picasso', 'B. Leonardo da Vinci', 'C. Vincent van Gogh', 'D. Michelangelo'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the currency of Australia?',
        'options': ['A. Dollar', 'B. Euro', 'C. Peso', 'D. Yen'],
        'correct_answer': 'A'
    },
    {
        'question': 'Which planet is known as the "Blue Planet"?',
        'options': ['A. Earth', 'B. Neptune', 'C. Uranus', 'D. Mercury'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who wrote "To Kill a Mockingbird"?',
        'options': ['A. J.K. Rowling', 'B. Harper Lee', 'C. George Orwell', 'D. Ernest Hemingway'],
        'correct_answer': 'B'
    },
    {
        'question': 'In which year did the Titanic sink?',
        'options': ['A. 1912', 'B. 1920', 'C. 1905', 'D. 1931'],
        'correct_answer': 'A'
    },
    {
        'question': 'What is the world\'s largest desert?',
        'options': ['A. Sahara Desert', 'B. Gobi Desert', 'C. Antarctica', 'D. Arabian Desert'],
        'correct_answer': 'C'
    }
]
  intermediate_questions = [
    {
        'question': 'Which chemical element has the symbol "Fe" on the periodic table?',
        'options': ['A. Iron', 'B. Gold', 'C. Silver', 'D. Copper'],
        'correct_answer': 'A'
    },
    {
        'question': 'In which year did World War II end?',
        'options': ['A. 1945', 'B. 1939', 'C. 1951', 'D. 1941'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who was the first woman to win a Nobel Prize?',
        'options': ['A. Marie Curie', 'B. Mother Teresa', 'C. Amelia Earhart', 'D. Jane Goodall'],
        'correct_answer': 'A'
    },
    {
        'question': 'Which famous physicist developed the theory of relativity?',
        'options': ['A. Isaac Newton', 'B. Albert Einstein', 'C. Galileo Galilei', 'D. Stephen Hawking'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the capital of Brazil?',
        'options': ['A. Brasília', 'B. Rio de Janeiro', 'C. São Paulo', 'D. Buenos Aires'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who wrote "1984"?',
        'options': ['A. George Orwell', 'B. Aldous Huxley', 'C. Ray Bradbury', 'D. J.D. Salinger'],
        'correct_answer': 'A'
    },
    {
        'question': 'Which famous artist painted "Starry Night"?',
        'options': ['A. Pablo Picasso', 'B. Vincent van Gogh', 'C. Claude Monet', 'D. Salvador Dalí'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the world\'s second-largest continent by land area?',
        'options': ['A. Europe', 'B. Asia', 'C. Africa', 'D. North America'],
        'correct_answer': 'C'
    }
]
  hard_questions = [
    {
        'question': 'Which war is often referred to as the "Great War"?',
        'options': ['A. World War I', 'B. World War II', 'C. Korean War', 'D. Vietnam War'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who is the author of the epic poem "The Iliad"?',
        'options': ['A. Homer', 'B. Virgil', 'C. Sophocles', 'D. Aesop'],
        'correct_answer': 'A'
    },
    {
        'question': 'In what year did the Industrial Revolution begin?',
        'options': ['A. 1765', 'B. 1800', 'C. 1850', 'D. 1700'],
        'correct_answer': 'A'
    },
    {
        'question': 'Which element has the chemical symbol "W"?',
        'options': ['A. Tungsten', 'B. Tin', 'C. Titanium', 'D. Thallium'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who was the first woman to receive a Ph.D. in computer science?',
        'options': ['A. Ada Lovelace', 'B. Grace Hopper', 'C. Radia Perlman', 'D. Karen Sparck Jones'],
        'correct_answer': 'B'
    },
    {
        'question': 'In what year did the Berlin Wall fall?',
        'options': ['A. 1989', 'B. 1979', 'C. 1991', 'D. 1961'],
        'correct_answer': 'A'
    },
    {
        'question': 'Which philosopher is known for his work on existentialism?',
        'options': ['A. Søren Kierkegaard', 'B. Friedrich Nietzsche', 'C. Jean-Paul Sartre', 'D. Albert Camus'],
        'correct_answer': 'C'
    },
    {
        'question': 'What is the largest moon of Saturn?',
        'options': ['A. Titan', 'B. Enceladus', 'C. Mimas', 'D. Rhea'],
        'correct_answer': 'A'
    },  {
        'question': 'Which element has the chemical symbol "K"?',
        'options': ['A. Potassium', 'B. Krypton', 'C. Kryptonite', 'D. Calcium'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who is the author of the novel "One Hundred Years of Solitude"?',
        'options': ['A. Gabriel Garcia Marquez', 'B. Isabel Allende', 'C. Julio Cortázar', 'D. Pablo Neruda'],
        'correct_answer': 'A'
    },
    {
        'question': 'In which year did the Chernobyl nuclear disaster occur?',
        'options': ['A. 1986', 'B. 1979', 'C. 1991', 'D. 1969'],
        'correct_answer': 'A'
    },
    {
        'question': 'What is the speed of sound in air (approximately)?',
        'options': ['A. 343 meters per second', 'B. 123 meters per second', 'C. 567 meters per second', 'D. 789 meters per second'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who formulated the laws of motion and universal gravitation?',
        'options': ['A. Isaac Newton', 'B. Albert Einstein', 'C. Galileo Galilei', 'D. Johannes Kepler'],
        'correct_answer': 'A'
    },
    {
        'question': 'Which African country was formerly known as Abyssinia?',
        'options': ['A. Ethiopia', 'B. Kenya', 'C. Nigeria', 'D. Sudan'],
        'correct_answer': 'A'
    },
    {
        'question': 'What is the chemical symbol for the element named after the planet Uranus?',
        'options': ['A. Uuq', 'B. Uup', 'C. Uus', 'D. Uuo'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who was the first woman to win a Nobel Prize in Physics?',
        'options': ['A. Marie Curie', 'B. Dorothy Crowfoot Hodgkin', 'C. Lise Meitner', 'D. Maria Goeppert Mayer'],
        'correct_answer': 'A'
    }
]
  challenging_questions = [
    {
        'question': 'Which celestial object is known as the "Diamond Planet" due to its high carbon content?',
        'options': ['A. Venus', 'B. Saturn', 'C. Jupiter', 'D. 55 Cancri e'],
        'correct_answer': 'D'
    },
    {
        'question': 'Who is the physicist known for proposing the concept of black holes in the early 20th century?',
        'options': ['A. Albert Einstein', 'B. Niels Bohr', 'C. Stephen Hawking', 'D. Karl Schwarzschild'],
        'correct_answer': 'D'
    },
    {
        'question': 'Which American film director is known for the movies "Pulp Fiction" and "Reservoir Dogs"?',
        'options': ['A. Christopher Nolan', 'B. Quentin Tarantino', 'C. Martin Scorsese', 'D. Steven Spielberg'],
        'correct_answer': 'B'
    },
    {
        'question': 'What is the chemical symbol for the element named after the physicist who developed the theory of relativity?',
        'options': ['A. Rn', 'B. Es', 'C. Md', 'D. Mt'],
        'correct_answer': 'B'
    },
    {
        'question': 'In the film "2001: A Space Odyssey," who is the artificial intelligence that malfunctions?',
        'options': ['A. HAL 9000', 'B. R2-D2', 'C. Jarvis', 'D. Skynet'],
        'correct_answer': 'A'
    },
    {
        'question': 'Which scientist is credited with the discovery of the first antibiotic, penicillin?',
        'options': ['A. Louis Pasteur', 'B. Alexander Fleming', 'C. Jonas Salk', 'D. Marie Curie'],
        'correct_answer': 'B'
    },
    {
        'question': 'In the field of astrophysics, what does the acronym "SETI" stand for?',
        'options': ['A. Search for Extraterrestrial Intelligence', 'B. Solar and Exoplanetary Terrestrial Investigation', 'C. Space Exploration and Technology Initiative', 'D. Scientific Exploration of Terrestrial Inhabitants'],
        'correct_answer': 'A'
    },
    {
        'question': 'Who directed the science fiction film "Blade Runner"?',
        'options': ['A. Stanley Kubrick', 'B. Ridley Scott', 'C. James Cameron', 'D. George Lucas'],
        'correct_answer': 'B'
    }
]


  # here we initiate the class setting the prize to 0€
  def __init__(self):
    self.prize = 0
    self.current_question_index = 0
    self.question_number = 0
    self.game_on = True
    self.lifeline = input("Press ok to continue")

  # this introduces the game and the presentor
  def __repr__(self) -> str:
    print("Welcome to Who Wants To Be a Millionaire! \n My name is Vasco Palmeirim. Leeeeeet's Begiiin!")

  def play(self):
    print("Welcome to Who Wants To Be a Millionaire! \n My name is Vasco Palmeirim. Leeeeeet's Begiiin!")
    print("If you want to get a lifeline just write 'help'")
    

    while self.prize < 20000 and self.game_on:
      if self.prize < 500:
            self.easy_game()
    
      elif 500 <= self.prize < 5000:
            self.intermediate_game()
      elif 5000 <= self.prize < 15000:
            self.hard_game()
      elif 15000 <= self.prize < 20000:
            self.challenging_game()



  #This is the function for easy questions being prompted to the user
  #We get a random quention from the easy_questions array and we work with that. 
  #If the answer is correct we had 100 to the prize, otherwise we set the prize to 0    
  def easy_game(self):
    random_question = random.choice(self.easy_questions)
    question_text = random_question['question']
    answers = random_question['options']
    
    print(question_text)
    self.current_question = question_text

    for answer in answers:
      print(answer)

    print("This is the current question " + self.current_question)
    get_user_input = input("Which answer is the correct one: ")
    
    if get_user_input.lower() == "help":
        self.use_lifeline(random_question)  # Pass the index

    if random_question["correct_answer"] == get_user_input.upper():

        self.question_number += 1
        self.prize += 100
        print(f"Congratulations! Your prize is now in {self.prize}")
    else:
        self.prize = 0
        self.question_number = 0

        print(f"Oh noo! You lost your progress! The correct one was {random_question['correct_answer']}! Your prize is now in {self.prize}")
            # Save the index of the current question for later use
    current_index = self.easy_questions.index(random_question)
    self.current_question_index = current_index
    self.easy_questions.remove(random_question)
    print(self.current_question_index)
        
  def intermediate_game(self):
      print("Well done! We are now playing for 5000 euros!")
      random_question = random.choice(self.intermediate_questions)
      question_text = random_question['question']
      answers = random_question['options']
      
      print(question_text)

      for answer in answers:
        print(answer)

      get_user_input = input("Which answer is the correct one: ")
      if get_user_input.lower() == "help":
        self.use_lifeline()      

      if random_question["correct_answer"] == get_user_input.upper():
          self.prize += 900
          self.question_number += 1

          print(f"Congratulations! Your prize is now in {self.prize}")
      else:
          self.prize = 0
          self.question_number = 0

          print(f"Oh noo! You lost your progress! The correct one was {random_question['correct_answer']}! Your prize is now in {self.prize}")
      
      self.intermediate_questions.remove(random_question)
           
  def hard_game(self):
      print("Well done! We are now playing for 15000 euros!")

      random_question = random.choice(self.hard_questions)
      question_text = random_question['question']
      answers = random_question['options']
      
      print(question_text)

      for answer in answers:
        print(answer)

      get_user_input = input("Which answer is the correct one: ")
      
      if get_user_input.lower() == "help":
        self.use_lifeline()
      if random_question["correct_answer"] == get_user_input.upper():
          self.question_number += 1

          self.prize += 2000
          print(f"Congratulations! Your prize is now in {self.prize}")
      else:
          self.question_number = 0
          self.prize = 0
          print(f"Oh noo! You lost your progress! The correct one was {random_question['correct_answer']}! Your prize is now in {self.prize}")
      
      self.hard_questions.remove(random_question)
           
  def challenging_game(self):
    
      if self.prize == 50000:
          print("This is the 1 million dollar question, literally! ")   
             
      random_question = random.choice(self.challenging_questions)
      question_text = random_question['question']
      answers = random_question['options']
      self.game_on = False
      print(question_text)

      for answer in answers:
        print(answer)

      get_user_input = input("Which answer is the correct one: ")
      if get_user_input.lower() == "help":
        self.use_lifeline()
      if self.prize == 50000 and random_question['correct_answer'] == get_user_input.upper():
          self.prize = 1000000
          print("OH MY GOOOOD! YOU JUST WOOOON ONE MILLION EUROS! CONGRATULATIONS! What are you going to do with the money?")
      elif random_question["correct_answer"] == get_user_input.upper():
          self.question_number += 1
          self.prize += 10000
          print(f"Congratulations! Your prize is now in {self.prize}")
      else:
          self.prize = 10000
          self.question_number = 0

          print(f"Oh noo! You lost your progress! The correct one was {random_question['correct_answer']}! Your prize is now in {self.prize}")
      
      self.challenging_questions.remove(random_question)

  def use_lifeline(self, current_question):
      print("Choose a lifeline:")
      print("1. 50/50")
      print("2. Phone a friend")
      print("3. Ask the audience")

      lifeline_choice = input("Enter the number of the lifeline you want to use: ")

      if lifeline_choice == "1":
          self.fifty_fifty(current_question)
      elif lifeline_choice == "2":
          self.phone_a_friend(current_question)
      elif lifeline_choice == "3":
          self.ask_the_audience(current_question)
          
  def fifty_fifty(self, current_question):
        correct_answer = current_question['correct_answer']
        incorrect_answers = [option for option in current_question['options'] \
                             if option != correct_answer]
        shown_option = random.choice(incorrect_answers)
        print(f"The 50/50 lifeline leaves you with the following options: {correct_answer}, {shown_option}")  


  def phone_a_friend(self, current_question):
        # Assume the friend has a 60% chance of giving the correct answer
        if random.random() <= 0.6:
            print("Your friend suggests that the correct answer is:")
            print(self.get_current_question()['correct_answer'])
        else:
            # Randomly choose an incorrect answer
            incorrect_answers = list(set(self.get_current_question()['options']) - set(self.get_current_question()['correct_answer']))
            random_incorrect_answer = random.choice(incorrect_answers)
            print(f"Your friend suggests that the answer is:")
            print(random_incorrect_answer)

  def ask_the_audience(self, current_question):
        # Assume the audience has a 70% chance of giving the correct answer
        if random.random() <= 0.7:
            print("The audience voted, and the majority believes the correct answer is:")
            print(self.get_current_question()['correct_answer'])
        else:
            # Randomly choose an incorrect answer
            incorrect_answers = list(set(self.get_current_question()['options']) - set(self.get_current_question()['correct_answer']))
            random_incorrect_answer = random.choice(incorrect_answers)
            print(f"The audience voted, and the majority believes the answer is:")
            print(random_incorrect_answer)  


teste = WhoWantsToBeaMillionaire()

print(teste.play())
