import random
tickets = [random.randint(1, 100) for i in range(15)]
print(f"Lottery Tickets = {tickets}\n")
p1 = tickets[0:5]
p2 = tickets[5:10]
p3 = tickets[10:15]

s1 = sum(p1)
print(f"Player 1 Tickets = {p1}\nTotal = {s1}")

s2 = sum(p2)
print(f"Player 2 Tickets = {p2}\nTotal = {s2}")

s3 = sum(p3)
print(f"Player 3 Tickets = {p3}\nTotal = {s3}")

if (s1 > s2) and (s1 > s3):
 print("Winner = Player 1")

elif (s2 > s1) and (s2 > s3):
 print("Winner = Player 2")

elif (s3 > s1) and (s3 > s2):
 print("Winner = Player 3")
 
else:
 print(" It's a tie!")
