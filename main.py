def run_action():
  import time
  q=input("Hello, do you want a prize? (Yes or No): ")
  if q=="Yes" or q=="yes":
      print("Here is an award for being great!")
      time.sleep(1.5)
      print("""                           ___________ 
                          '._==_==_=_.' 
                          .-\:      /-. 
                         | (|:.     |) | 
                          '-|:.     |-' 
                            \::.    / 
                             '::. .' 
                               ) ( 
                             _.' '._ 
                           _/_______\_ 
                          /___________\ 
              """)
  time.sleep(2)
  q2=input("Do you want another prize? (Yes or No): ")
  if q2=="Yes" or q2=="yes":
      print("First, I need your name.")
      name = input("Can you write your name: ")
      print("Great! Just give me a second and I will get your prize ready.")
      time.sleep(3)
      print("LOADING...")
      time.sleep(2.5)
      print(f"""
          Dear {name},
          I love you so much for being so great.
          You are hardworking and you don't want
          me to fail. You care about me so much
          and I hope you had a great day today!
          Happy Fathers Day {name}!
          """)

  time.sleep(1.5)
  print(f"""
  I hope you enjoyed your prizes {name}!
  I hope to see you again next year!
  """)
