import numpy


#card3 is gonna be card 1 and 2 added.

cash = 100
cash = int(cash)

# this function checks to see if anyone
# wins OR overshoots 21 in round 1
def t1Check(cash, cashbet): #checks to see if anyone won in turn 1
  if (playerCard3 and compCard3 > 21):
    print("no one wins")
  
    

  elif (playerCard3 > 21):
    print("ops, you are over 21, computer wins")
    int(cash, cashbet)
    cash = cash - cashbet
    
    

  elif (compCard3 > 21):
    print("gg you win, computer has over 21")
    int(cash, cashbet)
    cash = cash + cashbet
    
    

  elif (playerCard3 == 21):
    print("gg you win")
    int(cash)
    int(cashbet)
    cash = cash + cashbet
    
    
  
  elif (compCard3 == 21):
    print("gg comp wins")
    int(cash)
    int(cashbet)
    cash = cash - cashbet
    

  return(cash)
    

def standCheck(cash, cashbet): #check to see who won after stand
  if (playerCard3 > compCard3 and playerCard3 < 22):
    print("Player wins")
    int(cash)
    int(cashbet)
    cash = cash + cashbet
    
    
  elif (playerCard3 < compCard3 and compCard3 < 22):
    print("Computer wins")
    int(cash)
    int(cashbet)
    cash = cash - cashbet
    
    
  elif (playerCard3 == compCard3):
    print("It's a tie!!")
    int(cash)
    cash = cash
    

  return(cash)
    



print("Welcome to Black Jack. \n Your goal is to get  closer to 21, or get 21, than the computer. \n You get two cards and will have a total. \n You can hit to get one more card or stand to compare who has more: you or the computer. \n")



game = 1
while(game == 1):

  print("You have ", cash, "dollars to bet.")
  
  cashbet = input("I want to bet: ")
  cashbet = int(cashbet)
  print("\n")

  m = 1
  while(m == 1):
    
    if(cashbet > cash):
      print("Sorry but you don't have that much cash to bet.")
      m = 0

    elif(cash ==0):
      print("You have no more cash left. Game over!")
      m = 0
      exit()

    answer = input("Would u like to start? y/n ").lower()
    if (answer == "n"):
      print("\nBooo u suck")
      m = 0
      game = 0
      #exit()
    
    elif (answer == "y"):

      playerCard1 = numpy.random.rand()
      playerCard1 = playerCard1*10 + 1
      playerCard1 = round(playerCard1)
      playerCard1 = int(playerCard1)
      
      playerCard2 = numpy.random.rand()
      playerCard2 = playerCard2*10 + 1
      playerCard2 = round(playerCard2)
      playerCard2 = int(playerCard2)
      
      playerCard3 = playerCard1 + playerCard2
      playerCard3 = int(playerCard3)
      #card3 is gonna be card 1 and 2 added.
      
      compCard1 = numpy.random.rand()
      compCard1 = compCard1*10 + 1
      compCard1 = round(compCard1)
      
      compCard2 = numpy.random.rand()
      compCard2 = compCard2*10 + 1
      compCard2 = round(compCard2)
      compCard2 = int(compCard2)
    
      compCard3 = compCard1 + compCard2
      compCard3 = int(compCard3)
      print("\n Your cards: ", playerCard1,",", playerCard2, "\n Total: ", playerCard3)
      m = 0

  
  if (compCard3 < 20):
    b = numpy.random.rand()
    b = b*9 + 1
    b = round(b)
    if (b > 5):
      compCard3 = compCard3 + (round(numpy.random.rand() * 10 + 1))
    
    elif (b <= 5):
      compCard3 = compCard3
  
  
  h = 1
  while(h == 1):
    answer = input("\n Would you like to Hit or Stand? h/s: ").lower()
    if (answer == "s"):
      t1Check(cash, cashbet)
      cash = t1Check(cash, cashbet)
      cash = standCheck(cash, cashbet)
      cash = standCheck(cash, cashbet)
      print("The computer had: ", compCard3)
      print("The player had: ", playerCard3)
      h = 0
      #checking to see 
    
    elif (answer == "h"):
      playerCard3 = playerCard3 + round(numpy.random.rand() * 10 + 1)
      print(playerCard3)
      t1Check(cash, cashbet)
      cash = t1Check(cash, cashbet)
      if (playerCard3 > 21):
        h = 0
      if (playerCard3 == 21):
        h = 0
