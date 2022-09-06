def leverup():
    print("| / \n|/ \n| ")
    
def levermiddle():
    print("|  \n|-- \n| ")








print("Welcoke to the useless lever. To use the lever, simply type pull")
while True:
    leverup()
    user = input()
    if user == "pull":
        levermiddle()
        print("The lever magically went back up")
    else:
        print("Silly goose, you didn't pull the lever. HOW DARE YOU NOT PULL THE LEVER!!!")
        
    
    
    



