#!/usr/bin/env python

import rospy
from lamp_state_service.srv import *
from std_msgs.msg import String
import json

def handle_request(request):
	global json_dict
	lamp_id=request.lamp_id.data
	state=request.state.data
	
	#smart lamp
	if((lamp_id > 0 and lamp_id < 5) and (state == 0 or state == 1 or state == 2 )):
		json_dict["lamp_%d"%(lamp_id)]=state
		response=change_stateResponse()
		response.res.data=True
	#non-smart lamp
	elif((lamp_id > 4 and lamp_id < 9) and (state == 1 or state == 0)):
		json_dict["lamp_%d"%(lamp_id)]=state
		response=change_stateResponse()
		response.res.data=True
	else:
		response=change_stateResponse()
		response.res.data=False
	return response

	
def simple_server():
	global json_dict
	rospy.init_node("lamp_state_service")
	rospy.Service("lamp_state_service_server" , change_state, handle_request)
	pub=rospy.Publisher("lamp_state", String,queue_size=10)
	rate=rospy.Rate(15)

	#smart lamp id = 1 - 4
	#non_smart lamp id = 5 - 8
	json_dict={
	"lamp_1":0,
	"lamp_2":0,
	"lamp_3":0,
	"lamp_4":0,
	"lamp_5":0,
	"lamp_6":0,
	"lamp_7":0,
	"lamp_8":0
	}

	while not rospy.is_shutdown():
		json_msg=json.dumps(json_dict)
		pub.publish(json_msg)
		rate.sleep()

if __name__ == '__main__':
	global json_dict
	simple_server()
