
import random

# Define your Coin class here
class Coin():
  def __init__(self):
    self.face = random.choice(["heads", "tails"])

  def get_face(self):
    return self.face

  def flip(self):
    return random.choice(["heads", "tails"])


if __name__ == '__main__':
  coin1 = Coin()
  coin1_heads = 0
  coin1_tails = 0

  for i in range(1000):
    coin1.flip()
    if coin1.get_face() == "heads":
      coin1_heads += 1
    else:
      coin1_tails += 1
  print(coin1_heads)
  print(coin1_tails)



  
