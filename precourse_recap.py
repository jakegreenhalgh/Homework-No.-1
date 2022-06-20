Name = "Parrots"
IsBird = True
LifeSpan = 100
SmallestHeight = 3.5
def parrot_facts():
    print("Here's some facts about "+ Name + ":")
    print(Name + " are birds? - " + str(IsBird) + "!")
    print(Name + " can live up to " + str(LifeSpan) + " years!")
    print(Name + " can be as small as " + str(SmallestHeight) + " inches!")
parrot_facts()