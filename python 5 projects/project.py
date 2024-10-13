name=input("Hey what's your name: ")
print("Hello",name,"Welcome to medicoPlus+")

question=int(input("select one of these: 1.Symptoms 2.Consultation 3.others "))
while True:
 if question == 1:
    print("What symptoms are you looking for!")
    response=int(input("Select one: 1.Headached 2.StomachPain 3.BackPain 4.exit "))
    if response == 1:
      print("Headache symptoms are:\n ->Tension Headache\n ->Migraine\n ->Cluster Headache\n ->Sinus Headache\n Consult a doctor if severe or persistent!")
    elif response == 2:
      print("StomachPain Symptoms are:\n ->Pain\n ->Pressure\n ->Sensitivity\n ->Nausea\n ->Discomfort")
    elif response ==3:
      print("BackPain symptoms are:\n ->Aching\n ->Stiffness\n ->Sharp pain\n ->Muscle spasms\n ->Limited mobility")
    elif response == 4:
      exit()
 elif question == 2:
    print("Do you want to consult(gyno,cardio...) ")
    response2=input("Yes or No ")
    if response2 == "yes":
      print("Sorry currently we don't have the doctors nearyou!")
    else:
      print("Ok good:)")
      exit()
 elif question ==3:
    print("Do you have any other things in mind!")
    response3=input("Yes or No ")
    if response3 == "yes":
      print("This feature is coming soon.......please wait......Thankyou:)")
      exit()
    else:
      print("It's great talking with you!")
      exit()
 else:
    print("Sorry i don't understand it :(")


