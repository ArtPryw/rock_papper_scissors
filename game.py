import random

class Game:
    
    def computer_input(self):
        
        computer_choice = random.randint(0,2)
        
        if computer_choice == 0:
            computer_choice = 'K'
        elif computer_choice == 1:
            computer_choice = 'P'
        elif computer_choice == 2:
            computer_choice = 'N'
            
        print("Komputer wybrał!")
        
        return computer_choice
    
    
    def user_input(self):
        
        user_choice = input("Jaki symbol chcesz wybrać? K, P, N?")
    
        return user_choice 
            
    
    def run(self,wybor1, wybor2):
        #wybór2 to komputer
        print("GRA SIĘ ROZPOCZYNA")
        
        if wybor1 == wybor2:
            print("REMIS")
        elif wybor1 == 'K' and wybor2 == 'P':
            print(f"{wybor1} - {wybor2}!")
            print("Wygrał komputer!")
        elif wybor1 == 'P' and wybor2 == 'N':
            print(f"{wybor1} - {wybor2}!")
            print("Wygrał komputer!")
        elif wybor1 == 'N' and wybor2 == 'K':
            print(f"{wybor1} - {wybor2}!")
            print("wygrał komputer")
        else:
            print(f"{wybor1} - {wybor2}!")
            print("wygrał gracz!")
            

        
A = Game()

num = 0
while num < 3:
	A.run(A.user_input(), A.computer_input())
	num = num + 1
