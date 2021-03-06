{# 
#This is a jinja2 template of a ROS2 Node
#
# Written in 13/4/2020
# Written by Rafael Brouzos
#}

from rclpy.qos import QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy, QoSLivelinessPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSPresetProfiles
from rcl_interfaces.msg import ParameterDescriptor

{% if action_servers is defined and action_servers|length %}
# Imports for Action Servers
from rclpy.action import ActionServer, CancelResponse, GoalResponse
{% endif %}
{% if action_clients is defined and action_clients|length %}
# Imports for Action Clients
from rclpy.action import ActionClient
from action_msgs.msg import GoalStatus
{% endif %}
import rclpy
from rclpy.node import Node
import sys
# Imports for msg interfaces
{%for p in publishers %}
{%if p.unique == 1 %}
from {{p.package}}.msg import {{p.type}}
{%endif%}
{%endfor%}
{%for s in subscribers %}
{%if s.unique == 1 %}
from {{s.package}}.msg import {{s.type}}
{%endif%}
{%endfor%}
# Imports for srv interfaces
{%for s in servers %}
{%if s.unique == 1 %}
from {{s.package}}.srv import {{s.type}}
{%endif%}
{%endfor%}
{%for c in clients %}
{%if c.unique == 1 %}
from {{c.package}}.srv import {{c.type}}
{%endif%}
{%endfor%}
# Imports for action interfaces
{%for s in action_servers %}
{%if s.unique == 1 %}
from {{s.package}}.action import {{s.type}}
{%endif%}
{%endfor%}
{%for c in action_clients %}
{%if c.unique == 1 %}
from {{c.package}}.action import {{c.type}}
{%endif%}
{%endfor%}
# Imports for msg inside custom interfaces
{%for e in extra_imports %}
from {{e.package}}.msg import {{e.type}}
{%endfor%}


# Class for the node {{node.name}} 
class {{node.name}}_class(Node):
	
	# Constructor function of the node
	def __init__(self):
				
		super().__init__('{{node.name}}'{%if not node.namespace == None%}, namespace = '{{node.namespace}}'{%endif%})		
		# Params
		#____________________________________________
		{%for p in params %}
		# {{p.name}}  -  {{p.type}}
		# Description: {{p.description}}
		self.param_{{p.name}} = self.declare_parameter('{{p.name}}', {{p.value}}, descriptor=ParameterDescriptor(name='p1', type={{p.type2}}, description='', additional_constraints='', read_only=False, floating_point_range=[], integer_range=[]))
		# You can use your parameter {{p.name}} with type {{p.type}}
		# with 		self.get_parameter('{{p.name}}')._value
		# You can also use your parameter from terminal or yaml file. 
		#_____
		{%endfor%}
		
		
		# Publishers
		#____________________________________________
		{%for p in publishers %}
		# {{p.name}}
		# Qos profile
		{% if p.profile.history == "standart" %}
		qos_profile_{{p.name}} = QoSPresetProfiles.{{p.profile.name}}.value
		{%elif p.profile.history == "default" %}
		qos_profile_{{p.name}} = QoSPresetProfiles.SYSTEM_DEFAULT.value
		{%else%}
		qos_profile_{{p.name}} = QoSProfile(history=QoSHistoryPolicy.{{p.profile.history}}, durability = QoSDurabilityPolicy.{{p.profile.durability}},reliability = QoSReliabilityPolicy.{{p.profile.reliability}},depth ={{p.profile.depth}})
		# Additional qos settings
		qos_profile_{{p.name}}.liveliness = QoSLivelinessPolicy.{{p.profile.liveliness}}
		qos_profile_{{p.name}}.deadline.sec = {{p.profile.deadlineSec}}
		qos_profile_{{p.name}}.deadline.nsec = {{p.profile.deadlineNSec}}
		qos_profile_{{p.name}}.lifespan.sec = {{p.profile.lifespanSec}}
		qos_profile_{{p.name}}.lifespan.nsec = {{p.profile.lifespanNSec}}
		qos_profile_{{p.name}}.liveliness_lease_duration.sec = {{p.profile.liveliness_lease_durationSec}}
		qos_profile_{{p.name}}.liveliness_lease_duration.nsec = {{p.profile.liveliness_lease_durationNSec}}
		qos_profile_{{p.name}}.avoid_ros_namespace_conventions = {{p.profile.avoid_ros_namespace_conventions}}
		{%endif%}
				
		self.publisher_{{p.name}} = self.create_publisher({{p.type}}, '{{p.topicPath}}', qos_profile = qos_profile_{{p.name}})
		self.timer_{{p.name}} = self.create_timer({{p.publishRate}}, self.publisher_call_{{p.name}})
		self.i = 0
		#_____
		{%endfor%}
		
		# Subscribers
		#____________________________________________
		{%for s in subscribers %}
		# {{s.name}}
		# Qos profile
		{% if s.profile.history == "standart" %}
		qos_profile_{{s.name}} = QoSPresetProfiles.{{s.profile.name}}.value
		{%elif s.profile.history == "default" %}
		qos_profile_{{s.name}} = QoSPresetProfiles.SYSTEM_DEFAULT.value
		{%else%}
		qos_profile_{{s.name}} = QoSProfile(history = QoSHistoryPolicy.{{s.profile.history}}, durability = QoSDurabilityPolicy.{{s.profile.durability}}, reliability = QoSReliabilityPolicy.{{s.profile.reliability}}, depth ={{s.profile.depth}})
		# Additional qos settings
		qos_profile_{{s.name}}.liveliness = QoSLivelinessPolicy.{{s.profile.liveliness}}
		qos_profile_{{s.name}}.deadline.sec = {{s.profile.deadlineSec}}
		qos_profile_{{s.name}}.deadline.nsec = {{s.profile.deadlineNSec}}
		qos_profile_{{s.name}}.lifespan.sec = {{s.profile.lifespanSec}}
		qos_profile_{{s.name}}.lifespan.nsec = {{s.profile.lifespanNSec}}
		qos_profile_{{s.name}}.liveliness_lease_duration.sec = {{s.profile.liveliness_lease_durationSec}}
		qos_profile_{{s.name}}.liveliness_lease_duration.nsec = {{s.profile.liveliness_lease_durationNSec}}
		qos_profile_{{s.name}}.avoid_ros_namespace_conventions = {{s.profile.avoid_ros_namespace_conventions}}
		{%endif%}
				
		self.subscriber_{{s.name}} = self.create_subscription({{s.type}}, '{{s.topicPath}}', self.subscriber_call_{{s.name}}, qos_profile = qos_profile_{{s.name}})
		self.subscriber_{{s.name}}
		#_____
		{%endfor%}
		
		# Servers
		#____________________________________________
		{%for s in servers %}
		# {{s.name}}
		# Qos profile
		{% if s.profile.history == "standart" %}
		qos_profile_{{s.name}} = QoSPresetProfiles.{{s.profile.name}}.value
		{%elif s.profile.history == "default" %}
		qos_profile_{{s.name}} = QoSPresetProfiles.SERVICES_DEFAULT.value
		{%else%}
		qos_profile_{{s.name}} = QoSProfile(history = QoSHistoryPolicy.{{s.profile.history}}, durability = QoSDurabilityPolicy.{{s.profile.durability}}, reliability = QoSReliabilityPolicy.{{s.profile.reliability}}, depth ={{s.profile.depth}})
		# Additional qos settings
		qos_profile_{{s.name}}.liveliness = QoSLivelinessPolicy.{{s.profile.liveliness}}
		qos_profile_{{s.name}}.deadline.sec = {{s.profile.deadlineSec}}
		qos_profile_{{s.name}}.deadline.nsec = {{s.profile.deadlineNSec}}
		qos_profile_{{s.name}}.lifespan.sec = {{s.profile.lifespanSec}}
		qos_profile_{{s.name}}.lifespan.nsec = {{s.profile.lifespanNSec}}
		qos_profile_{{s.name}}.liveliness_lease_duration.sec = {{s.profile.liveliness_lease_durationSec}}
		qos_profile_{{s.name}}.liveliness_lease_duration.nsec = {{s.profile.liveliness_lease_durationNSec}}
		qos_profile_{{s.name}}.avoid_ros_namespace_conventions = {{s.profile.avoid_ros_namespace_conventions}}
		{%endif%}
				
		self.server_{{s.name}} = self.create_service({{s.type}}, '{{s.serviceName}}', self.server_call_{{s.name}}, qos_profile = qos_profile_{{s.name}})
		#_____
		{%endfor%}
		
		# Clients
		#____________________________________________
		{%for c in clients %}
		# {{c.name}}
		# Qos profile
		{% if c.profile.history == "standart" %}
		qos_profile_{{c.name}} = QoSPresetProfiles.{{c.profile.name}}.value
		{%elif c.profile.history == "default" %}
		qos_profile_{{c.name}} = QoSPresetProfiles.SERVICES_DEFAULT.value
		{%else%}
		qos_profile_{{c.name}} = QoSProfile(history = QoSHistoryPolicy.{{c.profile.history}}, durability = QoSDurabilityPolicy.{{c.profile.durability}}, reliability = QoSReliabilityPolicy.{{c.profile.reliability}}, depth ={{c.profile.depth}})
		# Additional qos settings
		qos_profile_{{c.name}}.liveliness = QoSLivelinessPolicy.{{c.profile.liveliness}}
		qos_profile_{{c.name}}.deadline.sec = {{c.profile.deadlineSec}}
		qos_profile_{{c.name}}.deadline.nsec = {{c.profile.deadlineNSec}}
		qos_profile_{{c.name}}.lifespan.sec = {{c.profile.lifespanSec}}
		qos_profile_{{c.name}}.lifespan.nsec = {{c.profile.lifespanNSec}}
		qos_profile_{{c.name}}.liveliness_lease_duration.sec = {{c.profile.liveliness_lease_durationSec}}
		qos_profile_{{c.name}}.liveliness_lease_duration.nsec = {{c.profile.liveliness_lease_durationNSec}}
		qos_profile_{{c.name}}.avoid_ros_namespace_conventions = {{c.profile.avoid_ros_namespace_conventions}}
		{%endif%}
				
		self.client_{{c.name}} = self.create_client({{c.type}}, '{{c.serviceName}}', qos_profile = qos_profile_{{c.name}})
		#_____
		{%endfor%}
		
		# Action Servers
		#____________________________________________
		{%for s in action_servers %}
		# {{s.name}}
		self.action_server_{{s.name}} = ActionServer(self, {{s.type}}, '{{s.name}}', execute_callback=self.action_execute_call_{{s.name}}, goal_callback=self.action_goal_call_{{s.name}}, cancel_callback=self.action_cancel_call_{{s.name}})
		#_____
		{%endfor%}
		
		# Action Clients
		#____________________________________________
		{%for s in action_clients %}
		# {{s.name}}
		self.action_client_{{s.name}} = ActionClient(self, {{s.type}}, '{{s.name}}')
		#_____
		{%endfor%}
		
		
		
	# ************Callbacks************
	# Publishers
	#____________________________________________
	{%for p in publishers %}
	# This is the callback of the publisher {{p.name}}. 
	# You can store the message in the msg object attributes, according 
	# to the instructions in the comments below. This function will be 
	# called automatically with the chosen publish rate, to publish your 
	# messages. This function is the template of the publisher callback 
	# and you should put your own functionality.
	def publisher_call_{{p.name}}(self):
		msg = {{p.type}}()
		# Please create the message of the publisher in this callback
		# The message definition could be found in the package: {{p.package}}
		
		{% if p.package == 'interfaces' %}
		# Some attributes of the message may be submessages and have special attributes
		# Message after calculactions should be stored in the attibutes:
		{%for r in p.msg %}
		# msg.{{r}} 
		{%endfor%}
		{% else %}
		# The message is type {{p.package}}/{{p.msg[0]}}
		# Remember to store data in its attributes before publishing
		{% endif %}
		
		
		# TODO: Add functionality here
		
		
		# Then publish the msg with the following code
		self.publisher_{{p.name}}.publish(msg)
		
	#_____
	{%endfor%}
	
	# Subscribers
	#____________________________________________
	{%for s in subscribers %}
	# This is the callback of the subscriber {{s.name}}. 
	# You can obtain the message from the variables set in this 
	# function, according to the instructions in the comments below. 
	# This function will be called automatically every time a message is
	# received. This function is the template of the subscriber callback 
	# and you should put your own functionality.
	def subscriber_call_{{s.name}}(self, msg):
		# Please obtain the message from the subscriber in this callback
		# The message definition could be found in the package: {{s.package}}
		
		{% if s.package == 'interfaces' %}
		# Store the variables of the msg
		{%for r in s.msg %}
		{{r}} = msg.{{r}}
		{%endfor%}
		# Now you can use the received variables
		{% else %}
		# The message is type {{s.package}}/{{s.msg[0]}}
		# Remember to obtain data from its attributes
		{% endif %}
		
		
		# TODO: Add functionality here
		
		# You can see incoming info uncommenting the following line and filling the attributes "msg" object
		# ~ self.get_logger().info('I heard: '+str(msg.<put your attributres>))
	#_____
	{%endfor%}
	
	# Servers
	#____________________________________________
	{%for s in servers %}
	# This is the callback of the server {{s.name}}. 
	# You can obtain the request to the server from the variables set in 
	# this function, according to the instructions in the comments 
	# below. This function will be called automatically every time a 
	# request is received. This function is the template of the server 
	# callback and you should put your own functionality.
	def server_call_{{s.name}}(self, request, response):
		# Please add the server's functionality in this callback
		{% if s.package == 'interfaces' %}
		# Store the variables of the request
		{%for r in s.requests %}
		{{r}} = request.{{r}}
		{%endfor%}
		# Service result after calculactions should be stored in:
		{%for r in s.responses %}
		# response.{{r}} 
		{%endfor%}
		{% else %}
		# The service is type {{s.package}}/{{s.requests[0]}}
		# Remember to store data in its attributes
		{% endif %}
		
		
		# TODO: Add functionality here
		
		# You can store the result uncommenting the following line and filling the attributes of the "response" object 
		# ~ response.<put your attributres> = <put your values> 
		
		# You can see incoming info uncommenting the following line and filling the attributes "request" object
		# ~ self.get_logger().info('Incoming request\nvalue 1: '+ str(request.<put your attributres>)+' value 2: '+str(request.<put your attributres>))
		
		# Finally forward the response
		return response
	#_____
	{%endfor%}
		
	# Clients
	#____________________________________________
	{%for c in clients %}
	# This is the call function of the client {{c.name}}. 
	# You can call this function, passing all the arguments of the 
	# service request declaration (if the service is a Custom Service). 
	# This function will not be called automatically as you should call 
	# it to make a request. The function waits for the service to be 
	# available before going on and the server's response is stored in 
	# a future object once the server returns the response. This 
	# function is the template of the client call and you should call 
	# it for applying requests. Remember to change the arguments of the 
	# function based on the service you use.
	def client_call_{{c.name}}(self{% if c.package == 'interfaces' %}{%for r in c.requests %}, {{r }} {%endfor%}{% endif %}):
		# Wait for service
		while not self.client_{{c.name}}.wait_for_service(timeout_sec=1.0):
			self.get_logger().info('service not available, waiting again...')
		# Create request and fill it with data
		self.request_{{c.name}} = {{c.type}}.Request()
		{% if c.package == 'interfaces' %}
		{%for r in c.requests %}
		self.request_{{c.name}}.{{r}} = {{r}}
		{%endfor%}
		{% else %}
		# The service is type {{c.package}}/{{c.requests[0]}}
		# Remember to store data in the attributes of self.request_{{c.name}}
		{% endif %}
		self.future_{{c.name}} = self.client_{{c.name}}.call_async(self.request_{{c.name}})
		# Result after server's response is stored in 
		{%for r in c.responses %}
		# self.future_{{c.name}}.result().{{r}} 
		{%endfor%}
		
		
		# TODO: Add functionality here
		
		
	#_____
	{%endfor%}
			
	# Action Servers
	#____________________________________________
	{%for s in action_servers %}
	# This is the execute callback of the action server {{s.name}}. 
	# You can execute the goal request to the action server from the 
	# variables set in this function, according to the instructions in 
	# the comments below. This function will be called automatically 
	# every time an action goal request is received and needs to be 
	# executed. This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_execute_call_{{s.name}}(self, goal_handle):
		# Please add the server's functionality in this callback
		self.get_logger().info('Executing goal...')
		# If your action interface contain submessages remember to fill their attributes
		# Store the variables of the goal request
		{%for r in s.goal %}
		{{r}} = goal_handle.request.{{r}}
		{%endfor%}
		# Create a feedback object
		feedback_msg = {{s.type}}.Feedback()
		# Every time you want to pass feedback update feedback attributes
		{%for r in s.feedback %}
		# feedback_msg.{{r}} = ...
		{%endfor%}
		# And call 
		# goal_handle.publish_feedback(feedback_msg)
		
		# Set the Result
		goal_handle.succeed()
		result = {{s.type}}.Result()
		# Fill the result with data
		{%for r in s.result %}
		# result.{{r}} = ...
		{%endfor%}
		
		
		# TODO: Add functionality here
		
		# Finally forward the response
		return result
	
	# This is the goal callback of the action server {{s.name}}.
	# This function receives a client goal requests to handle actions.
	# This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_goal_call_{{s.name}}(self,goal_request):
		# Please add the server's functionality in this callback
		self.get_logger().info('Received goal request')
		# Uncomment one of the following to reject or to accept an action request
		#return GoalResponse.REJECT
		return GoalResponse.ACCEPT
	
	# This is the cancel callback of the action server {{s.name}}.
	# This function receives client cancel requests to handle actions.
	# This function is the template of the action server 
	# callback and you should put your own functionality.
	def action_cancel_call_{{s.name}}(self, goal_handle):
		# Please add the server's functionality in this callback
		self.get_logger().info('Received cancel request')
		# Uncomment one of the following to reject or to accept an action request
		#return CancelResponse.REJECT
		return CancelResponse.ACCEPT
	#_____
	{%endfor%}
	
	# Action Clients
	#____________________________________________
	{%for c in action_clients %}
	# This is the call function of the action client {{c.name}}. 
	# You can call this function, passing all the arguments of the 
	# action goal request declaration. This function will not be called 
	# automatically as you should call it to make a request. The 
	# function waits for the action to be available before going on and
	# the action server's response is stored in a future object once 
	# the action server return the response. This function is the 
	# template of the action client call and you should call it for 
	# applying requests.
	def send_goal_call_{{c.name}}(self{%for r in c.goal %}, {{r }} {%endfor%}):
		# Wait for action service
		self.get_logger().info('Waiting for action server...')
		self.action_client_{{c.name}}.wait_for_server()
		# If your action interface contain submessages remember to fill their attributes 
		# Create goal and fill it with data
		goal_msg = {{c.type}}.Goal()
		{%for r in c.goal %}
		goal_msg.{{r}} = {{r}}
		{%endfor%}
		# Send the goal request
		self.get_logger().info('Sending goal request...')
		self.future_{{c.name}} = self.action_client_{{c.name}}.send_goal_async(goal_msg, feedback_callback=self.feedback_client_call_{{c.name}})
		self.future_{{c.name}}.add_done_callback(self.goal_response_client_call_{{c.name}})
		
	# This is the feedback callback of the action client {{c.name}}.
	# This function receives and handles the feedback that the 
	# action server publishes. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def feedback_client_call_{{c.name}}(self, feedback):
		self.get_logger().info('received feedback')
		# If your action interface contain submessages remember to obtain their attributes 
		# Do something with the variables in feedback
		{%for r in c.feedback %}
		# feedback.feedback.{{r}}
		{%endfor%}
		
		
		# TODO: Add functionality here
		
		
		
	# This is the response callback of the action client {{c.name}}.
	# This function receives and handles the response that the 
	# action server gives. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def goal_response_client_call_{{c.name}}(self, future):
		# Set the goal result
		goal_handle = future.result()
		# Check if the goal was accepted
		if not goal_handle.accepted:
			self.get_logger().info('Goal rejected :(')
			return
		# Goal Accepted
		self.get_logger().info('Goal accepted :)')
		# Create a callback for receiving the result async
		self.client_future_{{c.name}} = goal_handle.get_result_async()
		self.client_future_{{c.name}}.add_done_callback(self.get_result_call_{{c.name}})
		
	# This is the result callback of the action client {{c.name}}.
	# This function receives and final result that the 
	# action server returns. This function is the template of the 
	# action client callback and you should put your own 
	# functionality.
	def get_result_call_{{c.name}}(self, future):
		result = future.result().result
		status = future.result().status
		if status == GoalStatus.STATUS_SUCCEEDED:
			# If your action interface contain submessages remember to obtain their attributes 
			# Do something with the variables in result
			{%for r in c.result %}
			# result.{{r}}
			self.get_logger().info('Result obtained') 
			{%endfor%}
		else:
			self.get_logger().info('Goal failed with status: {0}'.format(status))
		
		
		# TODO: Add functionality here
		
		
	#_____
	{%endfor%}
		
		
# Main executable
#____________________________________________
# This is the main executable for the node {{node.name}}.
# Run this executable from the root of the workspace using the command:
# $ ros2 run {{pack.name}} {{node.name}}_exec
#
# This executable creates a node with all its features and spins it to
# wait for its callbacks.
def main(args=None):
	rclpy.init(args=args)
	
	{{node.name}} = {{node.name}}_class()
		
	rclpy.spin({{node.name}})
	# Destroy the node explicitly
	# (optional - otherwise it will be done automatically
	# when the garbage collector destroys the node object)
	{%for s in action_servers %}
	# Destroy action server {{s.name}}
	{{node.name}}.action_server_{{s.name}}.destroy()
	{%endfor%}
	{%for c in action_clients %}
	# Destroy action server {{c.name}}
	{{node.name}}.action_client_{{c.name}}.destroy()
	{%endfor%}
	{{node.name}}.destroy_node()
	rclpy.shutdown()

# Clients executables
#____________________________________________
{%for c in clients %}
# This is the executable for the client {{c.name}}.
# Run this executable from the root of the workspace using the command:
# $ ros2 run {{pack.name}} {{node.name}}_{{c.name}} arg1 arg2 ...
#
# This executable creates a node and call its client's call. It spins 
# the node until the response from the server is received.
def run_{{c.name}}(args=None):
	rclpy.init(args=args)
	
	{{node.name}} = {{node.name}}_class()
	#TODO create typecast from command line to client call type (change int to custom type)
	{{node.name}}.client_call_{{c.name}}({%for r in c.requests %}int(sys.argv[{{loop.index}}]){% if not loop.last %}, {%endif%} {%endfor%})
	while rclpy.ok():
		rclpy.spin_once({{node.name}})
		if {{node.name}}.future_{{c.name}}.done():
			try:
				response = {{node.name}}.future_{{c.name}}.result()
			except Exception as e:
				{{node.name}}.get_logger().info('Service call failed %r' % (e,))
			else:
				{{node.name}}.get_logger().info(
				'Result of add_three_ints: for %d + %d = %d' %
				({{node.name}}.request_{{c.name}}.a, {{node.name}}.request_{{c.name}}.b, response.c))
			break
#_____
{%endfor%}
	
if __name__ == '__main__':
	main()
