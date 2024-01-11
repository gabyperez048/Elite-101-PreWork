def welcoming_user():
  print("Hello, this is Milo your digital assisstant!")

def user_info():
  user_name = input("What's your name?")
  print("Hello " + user_name + "!" + " Nice to meet you!")
  age = input(user_name + " how old are you?")
  print("Wow!")
  return user_name, age

def questions(user_name):
  
  print("How can I help you today " + user_name + "?")
  print("1. Ask me a question")
  print("2. Provide information")
  print("3. End this coversation TT")
  choice = input("Please select an option (1/2/3) :D")
  return choice

def ask_me_a_question(user_name):
  question = input("Sure! What would you like to ask" + user_name +     "?")
  print("I'm sorry, I don't know the answer to that" + question +".")

def provide_information(user_name):
  input("What information would you like to prorvide" + user_name + "?")

def end_this_conversation(user_name):
  print("Aw. I'm sorry to hear that" + user_name + "I hope you have a great day!")
        
def main():

  welcoming_user()
  user_name, age = user_info()

  while True:
        user_choice = questions(user_name)

        if user_choice == '1':
            ask_me_a_question(user_name)
            
          
        elif user_choice == '2':
            provide_information(user_name)
            
        elif user_choice == '3':
            end_this_conversation(user_name)
            break
        else:
            print("Invalid choice. Please choose a valid option.")

            questions(user_name)

if __name__ == "__main__":
  main()

