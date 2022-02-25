#classes for Kindness.py
import time
import logging
import sys

from KindnessATL.Kindness import Anexity
def pause():
	time.sleep(2)
class MidOperationMessages():
	def AnimalApproach():
		time.sleep(1)
		logging.warning("Player , You are approaching an animal , !!Make the right choice!!")
		time.sleep(1)
	def PlayerWaking():
		print("Player walks down the road , expecting another animal.")
		pause()
		MidOperationMessages.AnimalApproach
		pause()
class Backend:
	def pause5():
		time.sleep(3)
	def anexity():
		pause()
		print('.')
		pause()
		print('..')
		pause()
		print('...')
		pause()
		print('....')
		pause()
		print('.....')
		pause()
	def KillSwitch():
		print("""
			  .
			  ..
			  ...
			  ....
			  .....
			  ......
			  you had to do it didnt you...
				""")
		time.sleep(2)
		print("""
				Just the way you saw , god keeps adding your bad karma in his list of bad karma for you whenever you do something wrong.
				which is why , it is always good to be kind and show kindness to others so that our container of badkarma doesnt go over the limit or else god will have to...well use the Killswitch :] 
				so always show kindness and be kind to anyone and everyone you meet.""")
		sys.exit("Player has killed 3 animals = death")
	def SurviveDub():
		print("""
				AND PLAYER HAS WON!!!
				as you saw , you saved the lives of 4 living things and got to live !
				This is how you should be , In real life!
				always show kindness to everyone and everythin you meet :]""")
		time.sleep(1)
		sys.exit("player has won - game over")
class Responses:
	def ifWalkedAway():
		print("Player has chosen to walk away!")
		Backend.anexity()
		print("Player has reicived 1 point of good karma!")
		pass
	def ifKilled():
		Backend.anexity()
		print("...you monster.")
		pause()
		print("You...you killed it..")
		pass
	def ifAttacButDodge():
		pause()
		print("Player tried attacking the animal!")
		pause()
		print("the animal escaped!")
		pause()
		print("Player has got 1 more bad karma for attempting to kill the animal!")
class RabbitActions:
	def WhenPLayerAttacButEsc():
		time.sleep(1)
		rabbitescanc='and the rabbit escaped!'
		print(rabbitescanc.capitalise())
	def WhenPLayerAttacButDed():
		Backend.anexity()
		print("..you monster..")
		time.sleep(1)
		print("you killed it...")
		time.sleep(1)
		logging.warning("Player has got 1 bad karma.")
class DogActions:
	def WhenPLayerAttacButEsc():
		time.sleep(1)
		dogescanc = 'the dog heard you running towards it and ran away in time!'
		print(dogescanc.capitalise())
		logging.warning("Player has got another bad karma point.")
	def WhenPLayerAttacButDed():
		Backend.anexity()
		print("..you monster.")
		time.sleep(1)
		print("You killed it..")
		time.sleep(2)
		logging.warning("Player has got another point for bad karma.")
class CatActions:
	def WhenPlayerAttackButRUn():
		time.sleep(1)
		catescanc = 'the cat heard you running towards it and escaped!'
		print(catescanc.capitalize())
		logging.warning("Playrr has got another bad karma point.")
	def WhenPLayerAttackButDead():
		time.sleep(1)
		Backend.anexity()
		print("..you monster.")
		time.sleep(1)
		print("you killed it...")
		time.sleep(1)
		logging.warning("PLayer has got another point for bad karma.")
class HurtBird:
	def WhenPlayerStepAndDead():
		Backend.anexity()
		print("..you monster.")
		time.sleep(1)
		print("you killed it...")
		time.sleep(1)
		logging.warning("PLayer has got another point for bad karma.")
class PlantActions:
	def WhenCrushed():
		Backend.anexity()
		print("..you monster.")
		time.sleep(1)
		print("you killed it...")
		time.sleep(1)
		logging.warning("PLayer has got another point for bad karma.")
		