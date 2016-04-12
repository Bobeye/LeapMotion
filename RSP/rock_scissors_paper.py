import sys
sys.path.insert(0, "/home/poopeye/LeapMotionRobo/LeapSDK/lib")
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class RSPListener(Leap.Listener):
	finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
	bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
	state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

	def on_init(self, controller):
		a=1
		# print "Leap Motion Initialized..."

	def on_connect(self, controller):
		a=1

		# print "Leap Motion Connected"

		# Enable gestures
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

	def on_disconnect(self, controller):
		a=1

		# Note: not dispatched when running in a debugger.
		# print "Disconnected"

	def on_exit(self, controller):
		a=1
		
		# print "Exited"

	def on_frame(self, controller):
		# Get the most recent frame and report some basic information
		frame = controller.frame()

	def state_string(self, state):
		if state == Leap.Gesture.STATE_START:
			return "STATE_START"

		if state == Leap.Gesture.STATE_UPDATE:
			return "STATE_UPDATE"

		if state == Leap.Gesture.STATE_STOP:
			return "STATE_STOP"

		if state == Leap.Gesture.STATE_INVALID:
			return "STATE_INVALID"
# Create a sample listener and controller
# RSP_listener = RSPListener()
# RSP_controller = Leap.Controller()


def main():
	# Create a sample listener and controller
	listener = RSPListener()
	controller = Leap.Controller()

	# Have the sample listener receive events from the controller
	controller.add_listener(listener)

	frame = controller.frame()

	

	print(len(frame.hands))

	# Get hands
	for hand in frame.hands:

		handType = "Left hand" if hand.is_left else "Right hand"

		print "  %s, id %d, position: %s" % (
			handType, hand.id, hand.palm_position)

	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		# Remove the sample listener when done
		controller.remove_listener(listener)


if __name__ == "__main__":
	main()
