# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

#This secret code as well as the cheat action needs to be removed to close the backdoor vulnerability.

p_hp = 50
b_hp = 50
MAX_HP = 50

#This attack() function is missing the calculation to subtract 10 from the b_hp variable. To fix this, add a line subtracting 10 from b_hp.
def attack():
  global b_hp
  b_hp -= 10
  #There is an unexpected indentation before the print statement, remove this.
  print("You deal 10 damage!")

#The heal function lacks any boundary checks, which allows the player to heal past 50 health or heal when they are at 0 health. To fix this, add some boundary checks (if statement) and a MAX_HP variable.
def heal():
  global p_hp
  if p_hp > 0:
    p_hp += 20
    if p_hp > MAX_HP:
      p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")
  elif p_hp <= 0:
    print("Player is dead and cannot be healed!")


# --- Simple Game Loop ---
#When the boss is at 0 or less hp and the loop terminates, the game over message is displayed. 
#There needs to be a check for both hp values, if the player is at 0 display game over, if the boss is at 0 display a Victory message
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  
  if b_hp > 0:
    p_hp -= 10

if p_hp < 0:
  print("Game Over!")
elif b_hp < 0:
  print("Victory!")
