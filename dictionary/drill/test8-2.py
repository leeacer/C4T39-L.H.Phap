kamen = {
    "name" : "kamen rider build",
    "release" : "03/09/2017",
    "bottles" : ["RabbitTank", "GorillaMond", "HawkGatling", "NinninComic", "RocketPanda", "FireHedgehog", "LionCleaner", "KeyDragon", "KaizokuRessya", "OctopusLight", "PhoenixRobo", "SmaphoWolf", "RoseCopter", "ToraUFO", "KujiraJet", "KirinCyclone"],
    "publisher" : "bandai",
    "country" : "japan" 
}

quiz = {
    "1" : "kamen rider build",
    "2" : "kamen rider zi-o",
    "3" : "kamen rider ghost",
    "4" : "kamen rider ex-aid"
}

while True:
    print("Which kamen rider uses infused bottles?")
    for k,v in quiz.items():
        print(k + ".", v)
    answer = input("Your answer:")
    if answer == list(quiz.keys())[0]:
        print("yay")
        break
    else:
        print("nay")