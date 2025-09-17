import random
användarpoäng = 0
datorpoäng = 0
någonharvunnit = False

while någonharvunnit == False:

  #importerar random i projektet
  användarens_val = input ("Välj sten, sax eller påse: ")
  #Printar ut text och ber användaren om ett svar.

  datorns_val = random.randint(1,3)
  #väljer ett slumpmässigt tal mellan 1-3
  if datorns_val == 1:
    datorns_val = ("sten")
    #

  elif datorns_val == 2:
    datorns_val = ("sax")

  else:
    datorns_val = ("påse")

  #############################################
  if användarens_val == "sten" and datorns_val == "sax":
    användarpoäng += 1

  elif användarens_val == "sten" and datorns_val == "påse":
    datorpoäng += 1

  if användarens_val == "sax" and datorns_val == "sten":
    datorpoäng += 1

  elif användarens_val == "sax" and datorns_val == "påse":
    användarpoäng += 1

  if användarens_val == "påse" and datorns_val == "sten":
    användarpoäng += 1

  elif användarens_val == "påse" and datorns_val == "sax":
    datorpoäng += 1

  else:
    print("ingen vann denna runda")

  print("användarens poäng: " + str(användarpoäng))
  print("datorns poäng: " + str(datorpoäng))

  if användarpoäng == 2:
    någonharvunnit = True
    print("Användaren har vunnit")

  elif datorpoäng == 2:
    någonharvunnit = True
    print("Datorn har vunnit")
