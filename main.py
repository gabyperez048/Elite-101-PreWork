def welcoming_user():
  print("Hello, this is Milo your digital assisstant!")
  welcoming_user()
  user_name, user_age = user_info()

def user_info():
  name = input("What's your name?")
  print("Hello " + name + "!" + " Nice to meet you!")
  age = input(name + " how old are you?")
  return name, age

def questions():
  print("How can I ihelp you today" + user_name + "?")
  print("1. Ask me a question")
  print("2. Provide information")
  print("3. End this coversation TT")
  choice = input("Please select an option (1/2/3) :D")
  return choice 

def ask_me_a_question():
  input("Sure! What would you like to ask" + name +     "?")
  print("I'm sorry, I don't know the answer to that question.")

def provide_information():
  print("What information would you like to prorvide" + name +     "?")

def end_this_conversation():
  print("Aw. I'm sorry to hear that" + name + "I hope you have a great day!")
        
def main():
    

    while True:
        user_choice = questions()

        if user_choice == '1':
            ask_me_a_question()
        elif user_choice == '2':
            provide_information()
        elif user_choice == '3':
            end_this_conversation()
        else:
            print("Invalid choice. Please choose a valid option.")


