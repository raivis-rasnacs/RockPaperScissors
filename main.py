player1 = input("akmens/šķēres/papīrs")
player2 = input("akmens/šķēres/papīrs")

if player1 == player2:
  print("neizšķirts")
elif player1 == "akmens" and player2 == "šķēres":
  print("Uzvara 1. spēlētājam")
elif player1 == "šķēres" and player2 == "papīrs":
  print("Uzvara 1. spēlētājam")
elif player1 == "papīrs" and player2 == "akmens":
  print("Uzvara 1. spēlētājam")
else:
  print("Uzvara 2. spēlētājam")