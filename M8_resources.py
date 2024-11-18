class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname
    def get_year(self):
        return self.weapons
    def get_color(self):
        return self. weaknesses
    def profile(self):
        return self.nickname, self.weapons, self. weaknesses
    
player1 = character('','','')

player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

#end of class, beginning of test code

Martin = character('Martin', ['rope','pen','coat','first aid kit', 'paper','idea'],['weak1','weak2'])
print(f"My weapons are {Martin.weapons}")
print("coat" in Martin.weapons)
