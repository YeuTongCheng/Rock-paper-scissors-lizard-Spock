def name_to_number(name):
    if name=="rock":
        return 0
    elif name=="spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    elif name=="scissors":
        return 4
    else:
        return "error message"
def number_to_name(number):
    if number==0:
        return "rock"
    elif number==1:
        return "spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number==4:
        return "scissors"
    else:
      return "wrong range"
