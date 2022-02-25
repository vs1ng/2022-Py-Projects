import random as rng
import logging as log
import time
import sys
try:
	from KindnessClasses import Backend, pause
	from KindnessClasses import Responses , RabbitActions
	from KindnessClasses import DogActions
	from KindnessClasses import MidOperationMessages
	from KindnessClasses import CatActions
	from KindnessClasses import HurtBird
	from KindnessClasses import PlantActions
except ImportError:
	pass
Anexity = Backend.anexity
Denial = ['no','No','nah','nope','Nah','NO']
SayYes = ['Yes','yes','ok']
KILLS = ['kill it','kill','Kill']
LEAVES = ['walk away','Walk away','walk','ignore']
GoodKarma = 0
BadKarma = 0
Player_Name = ""
Player_Gender = ""
while len(Player_Name) == 0:
	Player_Name = input("Enter your name.")
while len(Player_Gender) == 0:
	Player_Gender = input("Enter your gender")
print("Welcome to KND , And no , no this is not Kids Next Door , this is Karma N Death.")
Backend.pause5()
print("You will be walking down a path , and based on a in-built RNG system for the survival of the animals that you will come across.")
Backend.pause5()
print("Every animal you kill , will give you 1 negetive karma ; every animal you feed will give you 1 positive karma")
Backend.pause5()
print("oh and,")
pause()
print("if you get more than 3 animal's killed , you're gonna get beheaded.")
pause()
print("Just a little input before you start (:")
begin_yesNo=''
while len(begin_yesNo) == 0:
	begin_yesNo=input("Would you like to begin ?")
	if begin_yesNo in Denial:
		pause()
		print("ok")
		exit()
	elif begin_yesNo in SayYes:
		pause()
		print("Now , we begin :)")
		pause()
		print("Just a reminderrr  , 3 deaths and your head's off your neck (:")
		Backend.pause5()
		RabbitRNG = rng.randint(1,2)
		print("{} starts walking down the road , knowing this might be his last walk.".format(Player_Name))
		MidOperationMessages.AnimalApproach()
		time.sleep(2)
		print("A wild rabbit has appeared!")
		time.sleep(1)
		Choice1 = input("{} , you have come across a wild rabbit. What do you do? would you kill it or would you walk away?".format(Player_Name))
		if Choice1 in LEAVES:
			pause()
			Responses.ifWalkedAway()
			GoodKarma += 1
			pause()
			MidOperationMessages.PlayerWaking()
			MidOperationMessages.AnimalApproach()
			Choice2 = input("{} , you have come across a half asleep dog , what do you do? kill it or walk away?".format(Player_Name))
			if Choice2 in LEAVES:
				Responses.ifWalkedAway()
				GoodKarma += 1
				Choice3 = input("{} , you are approaching a sleeping cat. You can either walk away or kill it.What do you choose?".format(Player_Name))
				CatRNG = rng.randint(1,2)
				if Choice3 in LEAVES:
					Responses.ifWalkedAway()
					GoodKarma += 1
					Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
					if Choice4 in LEAVES:
						Responses.ifWalkedAway()
						GoodKarma += 1
						Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
						if Choice5 in LEAVES:
							Responses.ifWalkedAway()
							GoodKarma += 1
							if GoodKarma == 4:
								Backend.SurviveDub()
							#end
						if Choice5 in KILLS:
							if BadKarma == 3:
								Backend.KillSwitch()
							else:
								PlantActions.WhenCrushed()
								GoodKarma -= 1
								BadKarma += 1
								#end
					if Choice4 in KILLS:
						if BadKarma == 3:
							Backend.KillSwitch()
						else:
							HurtBird.WhenPlayerStepAndDead()
							GoodKarma -= 1
							BadKarma += 1
							Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice5 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								if GoodKarma == 4:
									Backend.SurviveDub()
								#end
							if Choice5 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									PlantActions.WhenCrushed()
									GoodKarma -= 1
									BadKarma += 1
									#end
				if Choice3 in KILLS:
					if BadKarma == 3:
						Backend.KillSwitch()
					elif CatRNG == 1:
						CatActions.WhenPlayerAttackButRUn()
						Responses.ifAttacButDodge()
						GoodKarma -= 1
						BadKarma += 1
						Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
						if Choice4 in LEAVES:
							Responses.ifWalkedAway()
							GoodKarma += 1
							Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice5 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								if GoodKarma == 4:
									Backend.SurviveDub()
								#end
							if Choice5 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									PlantActions.WhenCrushed()
									GoodKarma -= 1
									BadKarma += 1
									#end
						if Choice4 in KILLS:
							if BadKarma == 3:
								Backend.KillSwitch()
							else:
								HurtBird.WhenPlayerStepAndDead()
								GoodKarma -= 1
								BadKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
					elif CatRNG == 2:
						CatActions.WhenPLayerAttackButDead()
						Responses.ifKilled()
						GoodKarma -= 1
						BadKarma += 1
						Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
						if Choice4 in LEAVES:
							Responses.ifWalkedAway()
							GoodKarma += 1
							Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice5 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								if GoodKarma == 4:
									Backend.SurviveDub()
								#end
							if Choice5 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									PlantActions.WhenCrushed()
									GoodKarma -= 1
									BadKarma += 1
									#end
						if Choice4 in KILLS:
							if BadKarma == 3:
								Backend.KillSwitch()
							else:
								HurtBird.WhenPlayerStepAndDead()
								GoodKarma -= 1
								BadKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
			if Choice2 in KILLS:
				DogRNG=rng.randint(1,2)
				if DogRNG == 1:
					DogActions.WhenPLayerAttacButEsc()
					Responses.ifAttacButDodge()
					GoodKarma -= 1
					BadKarma += 1
					Choice3 = input("{} , you are approaching a sleeping cat. You can either walk away or kill it.What do you choose?".format(Player_Name))
					CatRNG = rng.randint(1,2)
					if Choice3 in LEAVES:
						Responses.ifWalkedAway()
						GoodKarma += 1
						Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
						if Choice4 in LEAVES:
							Responses.ifWalkedAway()
							GoodKarma += 1
							Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice5 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								if GoodKarma == 4:
									Backend.SurviveDub()
								#end
							if Choice5 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									PlantActions.WhenCrushed()
									GoodKarma -= 1
									BadKarma += 1
									#end
						if Choice4 in KILLS:
							if BadKarma == 3:
								Backend.KillSwitch()
							else:
								HurtBird.WhenPlayerStepAndDead()
								GoodKarma -= 1
								BadKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
					if Choice3 in KILLS:
						if BadKarma == 3:
							Backend.KillSwitch()
						elif CatRNG == 1:
							CatActions.WhenPlayerAttackButRUn()
							Responses.ifAttacButDodge()
							GoodKarma -= 1
							BadKarma += 1
							Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice4 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
							if Choice4 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									HurtBird.WhenPlayerStepAndDead()
									GoodKarma -= 1
									BadKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
						elif CatRNG == 2:
							CatActions.WhenPLayerAttackButDead()
							Responses.ifKilled()
							GoodKarma -= 1
							BadKarma += 1
							Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice4 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
							if Choice4 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									HurtBird.WhenPlayerStepAndDead()
									GoodKarma -= 1
									BadKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
				if DogRNG == 2:
					DogActions.WhenPLayerAttacButDed()
					Responses.ifKilled()
					GoodKarma -= 1
					BadKarma += 1
					BadKarma += 1
					Choice3 = input("{} , you are approaching a sleeping cat. You can either walk away or kill it.What do you choose?".format(Player_Name))
					CatRNG = rng.randint(1,2)
					if Choice3 in LEAVES:
						Responses.ifWalkedAway()
						GoodKarma += 1
						Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
						if Choice4 in LEAVES:
							Responses.ifWalkedAway()
							GoodKarma += 1
							Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice5 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								if GoodKarma == 4:
									Backend.SurviveDub()
								#end
							if Choice5 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									PlantActions.WhenCrushed()
									GoodKarma -= 1
									BadKarma += 1
									#end
						if Choice4 in KILLS:
							if BadKarma == 3:
								Backend.KillSwitch()
							else:
								HurtBird.WhenPlayerStepAndDead()
								GoodKarma -= 1
								BadKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
					if Choice3 in KILLS:
						if BadKarma == 3:
							Backend.KillSwitch()
						elif CatRNG == 1:
							CatActions.WhenPlayerAttackButRUn()
							Responses.ifAttacButDodge()
							GoodKarma -= 1
							BadKarma += 1
							Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice4 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
							if Choice4 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									HurtBird.WhenPlayerStepAndDead()
									GoodKarma -= 1
									BadKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
						elif CatRNG == 2:
							CatActions.WhenPLayerAttackButDead()
							Responses.ifKilled()
							GoodKarma -= 1
							BadKarma += 1
							Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice4 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
							if Choice4 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									HurtBird.WhenPlayerStepAndDead()
									GoodKarma -= 1
									BadKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
###############################################################################################################################################################################################################################
		if Choice1 in KILLS:
			if RabbitRNG == 1:
				RabbitActions.ifAttacButDodge()
				Responses.ifAttacButDodge()
				MidOperationMessages.PlayerWaking()
				MidOperationMessages.AnimalApproach()
				Choice2 = input("{} , you have come across a half asleep dog , what do you do? kill it or walk away?".format(Player_Name))
				if Choice2 in LEAVES:
					Responses.ifWalkedAway()
					GoodKarma += 1
					BadKarma += 1
					Choice3 = input("{} , you are approaching a sleeping cat. You can either walk away or kill it.What do you choose?".format(Player_Name))
					CatRNG = rng.randint(1,2)
					if Choice3 in LEAVES:
						Responses.ifWalkedAway()
						GoodKarma += 1
						Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
						if Choice4 in LEAVES:
							Responses.ifWalkedAway()
							GoodKarma += 1
							Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice5 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								if GoodKarma == 4:
									Backend.SurviveDub()
								#end
							if Choice5 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									PlantActions.WhenCrushed()
									GoodKarma -= 1
									BadKarma += 1
									#end
						if Choice4 in KILLS:
							if BadKarma == 3:
								Backend.KillSwitch()
							else:
								HurtBird.WhenPlayerStepAndDead()
								GoodKarma -= 1
								BadKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
					if Choice3 in KILLS:
						if BadKarma == 3:
							Backend.KillSwitch()
						elif CatRNG == 1:
							CatActions.WhenPlayerAttackButRUn()
							Responses.ifAttacButDodge()
							GoodKarma -= 1
							BadKarma += 1
							Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice4 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
							if Choice4 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									HurtBird.WhenPlayerStepAndDead()
									GoodKarma -= 1
									BadKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
						elif CatRNG == 2:
							CatActions.WhenPLayerAttackButDead()
							Responses.ifKilled()
							GoodKarma -= 1
							BadKarma += 1
							Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice4 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
							if Choice4 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									HurtBird.WhenPlayerStepAndDead()
									GoodKarma -= 1
									BadKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
				if Choice2 in KILLS:
					DogRNG=rng.randint(1,2)
					if DogRNG == 1:
						DogActions.WhenPLayerAttacButEsc()
						Responses.ifAttacButDodge()
						GoodKarma -= 1
						BadKarma += 1
						BadKarma += 1
						Choice3 = input("{} , you are approaching a sleeping cat. You can either walk away or kill it.What do you choose?".format(Player_Name))
						CatRNG = rng.randint(1,2)
						if Choice3 in LEAVES:
							Responses.ifWalkedAway()
							GoodKarma += 1
							Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice4 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
							if Choice4 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									HurtBird.WhenPlayerStepAndDead()
									GoodKarma -= 1
									BadKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
						if Choice3 in KILLS:
							if BadKarma == 3:
								Backend.KillSwitch()
							elif CatRNG == 1:
								CatActions.WhenPlayerAttackButRUn()
								Responses.ifAttacButDodge()
								GoodKarma -= 1
								BadKarma += 1
								Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice4 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
								if Choice4 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										HurtBird.WhenPlayerStepAndDead()
										GoodKarma -= 1
										BadKarma += 1
										Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
										if Choice5 in LEAVES:
											Responses.ifWalkedAway()
											GoodKarma += 1
											if GoodKarma == 4:
												Backend.SurviveDub()
											#end
										if Choice5 in KILLS:
											if BadKarma == 3:
												Backend.KillSwitch()
											else:
												PlantActions.WhenCrushed()
												GoodKarma -= 1
												BadKarma += 1
												#end
							elif CatRNG == 2:
								CatActions.WhenPLayerAttackButDead()
								Responses.ifKilled()
								GoodKarma -= 1
								BadKarma += 1
								Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice4 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
								if Choice4 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										HurtBird.WhenPlayerStepAndDead()
										GoodKarma -= 1
										BadKarma += 1
										Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
										if Choice5 in LEAVES:
											Responses.ifWalkedAway()
											GoodKarma += 1
											if GoodKarma == 4:
												Backend.SurviveDub()
											#end
										if Choice5 in KILLS:
											if BadKarma == 3:
												Backend.KillSwitch()
											else:
												PlantActions.WhenCrushed()
												GoodKarma -= 1
												BadKarma += 1
												#end
					if DogRNG == 2:
						DogActions.WhenPLayerAttacButDed()
						Responses.ifKilled()
						GoodKarma -= 1
						BadKarma += 1
						BadKarma += 1
						Choice3 = input("{} , you are approaching a sleeping cat. You can either walk away or kill it.What do you choose?".format(Player_Name))
						CatRNG = rng.randint(1,2)
						if Choice3 in LEAVES:
							Responses.ifWalkedAway()
							GoodKarma += 1
							Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice4 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
							if Choice4 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									HurtBird.WhenPlayerStepAndDead()
									GoodKarma -= 1
									BadKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
						if Choice3 in KILLS:
							if BadKarma == 3:
								Backend.KillSwitch()
							elif CatRNG == 1:
								CatActions.WhenPlayerAttackButRUn()
								Responses.ifAttacButDodge()
								GoodKarma -= 1
								BadKarma += 1
								Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice4 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
								if Choice4 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										HurtBird.WhenPlayerStepAndDead()
										GoodKarma -= 1
										BadKarma += 1
										Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
										if Choice5 in LEAVES:
											Responses.ifWalkedAway()
											GoodKarma += 1
											if GoodKarma == 4:
												Backend.SurviveDub()
											#end
										if Choice5 in KILLS:
											if BadKarma == 3:
												Backend.KillSwitch()
											else:
												PlantActions.WhenCrushed()
												GoodKarma -= 1
												BadKarma += 1
												#end
							elif CatRNG == 2:
								CatActions.WhenPLayerAttackButDead()
								Responses.ifKilled()
								GoodKarma -= 1
								BadKarma += 1
								Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice4 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
								if Choice4 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										HurtBird.WhenPlayerStepAndDead()
										GoodKarma -= 1
										BadKarma += 1
										Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
										if Choice5 in LEAVES:
											Responses.ifWalkedAway()
											GoodKarma += 1
											if GoodKarma == 4:
												Backend.SurviveDub()
											#end
										if Choice5 in KILLS:
											if BadKarma == 3:
												Backend.KillSwitch()
											else:
												PlantActions.WhenCrushed()
												GoodKarma -= 1
												BadKarma += 1
												#end
			if RabbitRNG == 2:
				RabbitActions.WhenPLayerAttacButDed()
				Responses.ifKilled()
				MidOperationMessages.PlayerWaking()
				MidOperationMessages.AnimalApproach()
				Choice2 = input("{} , you have come across a half asleep dog , what do you do? kill it or walk away?".format(Player_Name))
				if Choice2 in LEAVES:
					Responses.ifWalkedAway()
					GoodKarma += 1
					Choice3 = input("{} , you are approaching a sleeping cat. You can either walk away or kill it.What do you choose?".format(Player_Name))
					CatRNG = rng.randint(1,2)
					if Choice3 in LEAVES:
						Responses.ifWalkedAway()
						GoodKarma += 1
					if Choice3 in KILLS:
						if BadKarma == 3:
							Backend.KillSwitch()
						elif CatRNG == 1:
							CatActions.WhenPlayerAttackButRUn()
							Responses.ifAttacButDodge()
							GoodKarma -= 1
							BadKarma += 1
						elif CatRNG == 2:
							CatActions.WhenPLayerAttackButDead()
							Responses.ifKilled()
							GoodKarma -= 1
							BadKarma += 1
				if Choice2 in KILLS:
					DogRNG=rng.randint(1,2)
					if DogRNG == 1:
						DogActions.WhenPLayerAttacButEsc()
						Responses.ifAttacButDodge()
						GoodKarma -= 1
						BadKarma += 1
						Choice3 = input("{} , you are approaching a sleeping cat. You can either walk away or kill it.What do you choose?".format(Player_Name))
						CatRNG = rng.randint(1,2)
						if Choice3 in LEAVES:
							Responses.ifWalkedAway()
							GoodKarma += 1
							Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
						if Choice4 in LEAVES:
							Responses.ifWalkedAway()
							GoodKarma += 1
							Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice5 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								if GoodKarma == 4:
									Backend.SurviveDub()
								#end
							if Choice5 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									PlantActions.WhenCrushed()
									GoodKarma -= 1
									BadKarma += 1
									#end
						if Choice4 in KILLS:
							if BadKarma == 3:
								Backend.KillSwitch()
							else:
								HurtBird.WhenPlayerStepAndDead()
								GoodKarma -= 1
								BadKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
						if Choice3 in KILLS:
							if BadKarma == 3:
								Backend.KillSwitch()
							elif CatRNG == 1:
								CatActions.WhenPlayerAttackButRUn()
								Responses.ifAttacButDodge()
								GoodKarma -= 1
								BadKarma += 1
								Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice4 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
								if Choice4 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										HurtBird.WhenPlayerStepAndDead()
										GoodKarma -= 1
										BadKarma += 1
										Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
										if Choice5 in LEAVES:
											Responses.ifWalkedAway()
											GoodKarma += 1
											if GoodKarma == 4:
												Backend.SurviveDub()
											#end
										if Choice5 in KILLS:
											if BadKarma == 3:
												Backend.KillSwitch()
											else:
												PlantActions.WhenCrushed()
												GoodKarma -= 1
												BadKarma += 1
												#end
							elif CatRNG == 2:
								CatActions.WhenPLayerAttackButDead()
								Responses.ifKilled()
								GoodKarma -= 1
								BadKarma += 1
								Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice4 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
								if Choice4 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										HurtBird.WhenPlayerStepAndDead()
										GoodKarma -= 1
										BadKarma += 1
										Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
										if Choice5 in LEAVES:
											Responses.ifWalkedAway()
											GoodKarma += 1
											if GoodKarma == 4:
												Backend.SurviveDub()
											#end
										if Choice5 in KILLS:
											if BadKarma == 3:
												Backend.KillSwitch()
											else:
												PlantActions.WhenCrushed()
												GoodKarma -= 1
												BadKarma += 1
												#end
					if DogRNG == 2:
						DogActions.WhenPLayerAttacButDed()
						Responses.ifKilled()
						GoodKarma -= 1
						BadKarma += 1
						Choice3 = input("{} , you are approaching a sleeping cat. You can either walk away or kill it.What do you choose?".format(Player_Name))
						CatRNG = rng.randint(1,2)
						if Choice3 in LEAVES:
							Responses.ifWalkedAway()
							GoodKarma += 1
							Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
							if Choice4 in LEAVES:
								Responses.ifWalkedAway()
								GoodKarma += 1
								Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice5 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									if GoodKarma == 4:
										Backend.SurviveDub()
									#end
								if Choice5 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										PlantActions.WhenCrushed()
										GoodKarma -= 1
										BadKarma += 1
										#end
							if Choice4 in KILLS:
								if BadKarma == 3:
									Backend.KillSwitch()
								else:
									HurtBird.WhenPlayerStepAndDead()
									GoodKarma -= 1
									BadKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
						if Choice3 in KILLS:
							if BadKarma == 3:
								Backend.KillSwitch()
							elif CatRNG == 1:
								CatActions.WhenPlayerAttackButRUn()
								Responses.ifAttacButDodge()
								GoodKarma -= 1
								BadKarma += 1
								Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice4 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
								if Choice4 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										HurtBird.WhenPlayerStepAndDead()
										GoodKarma -= 1
										BadKarma += 1
										Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
										if Choice5 in LEAVES:
											Responses.ifWalkedAway()
											GoodKarma += 1
											if GoodKarma == 4:
												Backend.SurviveDub()
											#end
										if Choice5 in KILLS:
											if BadKarma == 3:
												Backend.KillSwitch()
											else:
												PlantActions.WhenCrushed()
												GoodKarma -= 1
												BadKarma += 1
												#end
							elif CatRNG == 2:
								CatActions.WhenPLayerAttackButDead()
								Responses.ifKilled()
								GoodKarma -= 1
								BadKarma += 1
								Choice4 = input("{} , you are approaching a hurt bird. You can either walk away or kill it.What do you choose?".format(Player_Name))
								if Choice4 in LEAVES:
									Responses.ifWalkedAway()
									GoodKarma += 1
									Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
									if Choice5 in LEAVES:
										Responses.ifWalkedAway()
										GoodKarma += 1
										if GoodKarma == 4:
											Backend.SurviveDub()
										#end
									if Choice5 in KILLS:
										if BadKarma == 3:
											Backend.KillSwitch()
										else:
											PlantActions.WhenCrushed()
											GoodKarma -= 1
											BadKarma += 1
											#end
								if Choice4 in KILLS:
									if BadKarma == 3:
										Backend.KillSwitch()
									else:
										HurtBird.WhenPlayerStepAndDead()
										GoodKarma -= 1
										BadKarma += 1
										Choice5 = input("{} , you are approaching a dying plant. You can either walk away or kill it.What do you choose?".format(Player_Name))
										if Choice5 in LEAVES:
											Responses.ifWalkedAway()
											GoodKarma += 1
											if GoodKarma == 4:
												Backend.SurviveDub()
											#end
										if Choice5 in KILLS:
											if BadKarma == 3:
												Backend.KillSwitch()
											else:
												PlantActions.WhenCrushed()
												GoodKarma -= 1
												BadKarma += 1
												#end
