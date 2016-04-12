import time
import math
import sys
import rock_scissors_paper as RSP

# Calculate distance between two points
def POINT_DISTANCE(Pa, Pb):
	point_distance = 0
	for i in range(3):
		point_distance = point_distance + ((Pa[i] - Pb[i])**2)
	return math.sqrt(point_distance)
# initiallize leap motion
PERMIT = 1
sampletime = 0.01
currenttime = time.time()
lasttime = time.time()
listener = RSP.RSPListener()
controller = RSP.Leap.Controller()
# Have the sample listener receive events from the controller
controller.add_listener(listener)
frame = controller.frame()
print(len(frame.hands))
time.sleep(1)
# play
while PERMIT != 0:
	# initialize game with only one hand
	frame = controller.frame()
	HandsNum = len(frame.hands)
	while HandsNum != 1:
		print("Please place one and only one hand within the play area!")
		frame = controller.frame()
		HandsNum = len(frame.hands)
	controller.remove_listener(listener)
	print("RSP game ready?")
	print("3")
	time.sleep(1)
	print("2")
	time.sleep(1)
	print("1")
	start = time.time()
	# print("GO")
	time.sleep(0.2)
	# keep sampling until the gesture is stable
	STABILITY = 2000 
	lastIndexL = 0.0
	lastMiddleL = 0.0
	lastRingL = 0.0
	IndexL = 0.0
	MiddleL = 0.0
	RingL = 0.0
	while STABILITY != 0:
		controller.add_listener(listener)
		frame = controller.frame()
		for hand in frame.hands:
			centerPos = [0,0,0]
			for k in range(3):
				centerPos[k] = hand.palm_position[k]
			# print("Palm Center:", centerPos)
			for finger in hand.fingers:
				if listener.finger_names[finger.type] == 'Index':
					IndexPos = finger.joint_position(3)
					# print(IndexPos)
				if listener.finger_names[finger.type] == 'Middle':
					MiddlePos = finger.joint_position(3)
					# print(MiddlePos)
				if listener.finger_names[finger.type] == 'Ring':
					RingPos = finger.joint_position(3)
					# print(RingPos)
			IndexL = POINT_DISTANCE(centerPos,IndexPos)
			MiddleL = POINT_DISTANCE(centerPos,MiddlePos)
			RingL = POINT_DISTANCE(centerPos,RingPos)
			# print("Middle 3 Finger's Position:",IndexL,MiddleL,RingL)
		controller.remove_listener(listener)
		if abs((lastIndexL + lastMiddleL + lastRingL) - (IndexL + MiddleL + RingL)) <= 5:
			STABILITY = STABILITY - 1
		else: 
			STABILITY = 2000
		lastIndexL = IndexL
		lastMiddleL = MiddleL
		lastRingL = RingL
	if (IndexL + MiddleL) >= (RingL * 3.5):
		print("ROCK")
	elif (IndexL + MiddleL + RingL) >= 250:
		print("SCISSORS")
	elif (IndexL + MiddleL + RingL) < 250:
		print("PAPER")
	else:
		print("Please propose standard gestrues")
	end = time.time()
	print("Reaction Time: ", end-start)
	PERMIT = input("play RSP with me? -- 0 for no, 1 for yes")
	if PERMIT not in [0,1]:
		PERMIT = input("plat RSP with me? -- 0 for no, 1 for yes")

# Keep this process running until Enter is pressed
print "Press Enter to quit..."
try:
	sys.stdin.readline()
except KeyboardInterrupt:
	pass
finally:
	# Remove the sample listener when done
	controller.remove_listener(listener)