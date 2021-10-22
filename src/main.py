from random import randint
print("Carta, Forbici, Sasso contro Samael")
print("\nInserisci un nickname prima di iniziare")
nome = input()
print("Buona fortuna " + nome)
punteggio_giocatore = 0
punteggio_bot = 0
comando = ""

def gg():
      return """_____________________________________________________
|                         |                         |
|    _____________________|    _____________________|
|    |                    |    |
|    |                    |    |
|    |                    |    |
|    |                    |    |
|    |         ___________|    |         ____________
|    |         |          |    |         |          |
|    |         |_____     |    |         |_____     |
|    |              |     |    |              |     |
|    |______________|     |    |______________|     |
|                         |                         |
|_________________________|_________________________|"""


while (comando != "ora basta"):
  vinto = False
 
  print("\n Quale arma scegli?")
  armi = ["carta 0", "forbice 1", "sasso 2"]
  for arma in armi:
      print(arma)
  numero_scelto = int(input())
  arma_scelta = armi[numero_scelto]
  print("Hai scelto: " + arma_scelta)
  print("\nOra attendi la scelta di Samael")
  arma_bot = ""
  numero_bot = randint(0, 2)
  arma_bot = armi[numero_bot]
  print("\n Anche Samael ha fatto la sua scelta")
  verdetto = ""
  if(arma_scelta == "carta 0" and arma_bot == "sasso 2"):
      verdetto = "Bravo hai vinto!!!!"
      punteggio_giocatore = punteggio_giocatore + 50
  if (arma_scelta == "forbice 1" and arma_bot == "carta 0"):
      verdetto = "Bravo hai vinto!!!!"
      punteggio_giocatore = punteggio_giocatore + 50
  if (arma_scelta == "sasso 2" and arma_bot == "forbice 1"):
      verdetto = "Bravo hai vinto!!!!"
      punteggio_giocatore = punteggio_giocatore + 50
  if (arma_scelta == arma_bot):
      verdetto = "Pareggio"
  if (verdetto == ""):
      verdetto = "Samael ti ha battuto"
      punteggio_bot = punteggio_bot + 50  
  if(arma_scelta == "carta 0" and arma_bot == "sasso 2"):
      vinto = True
  if (arma_scelta == "forbice 1" and arma_bot == "carta 0"):
      vinto = True
  if (arma_scelta == "sasso 2" and arma_bot == "forbice 1"):
      vinto = True
  print("\n Premi invio per scoprire se hai vinto")
  input()
  print(verdetto)
 
  print(gg() if vinto == True else '')
 
  print("\nPUNTEGGIO:")
  print(nome + "-Samael : " + str(punteggio_giocatore) + "-" + str(punteggio_bot))
  print("\nScrivi ora basta per terminare il gioco mentre se vuoi continuare premi invio")
  comando = input()
print("\nGIOCO TERMINATO")