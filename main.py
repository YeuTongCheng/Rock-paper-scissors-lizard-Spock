def rpsls(player_choice):
    print (" ")
    print ("Player chooses "+ player_choice)
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(4)
    comp_choice=number_to_name(comp_number)
    print ("Computer chooses "+ comp_choice)
    difference=player_number-comp_number
    if difference==0:
        return ("Player and computer tie!")
    elif difference==1 or difference==2 or difference==-3 or difference==-4:
        return "Player wins!"
    else:
        return "Computer wins!"
  
  
