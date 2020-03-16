
node: Nodes_name

publisher name publy1
publisher path topic/path


# TODO messages

import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Nodes_name(Node):

    def __init__(self):
        super().__init__(Nodes_name)
        # Publishers
        #____________________________________________
        self.publy1= self.create_publisher(String, topic/path, 10)
		
        timer_period = 0.5  # seconds
        
        self.timer1 = self.create_timer(timer_period, self.timer_callback1)
        self.i = 0
		
		
    def timer_callback1(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publy1.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

		
		# Subscribers
        #____________________________________________
		

def main(args=None):
    rclpy.init(args=args)

    newnode = Nodes_name()

    rclpy.spin(newnode)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    newnode.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()