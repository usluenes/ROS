# ROS
ROS Packages

## simplepublisher

This package contains:
publisher.py     : Simple Publisher /publishedTopic (string message)
subscriber.py    : Simple Subscriber /publishedTopic (string message) 
stdpublisher.py  : /numTopic Publisher Node: Custom message (/msg/Num) 
stdsubscriber.py : /numTopic Subscriber Node:Custom message (/msg/Num) 
2publisher.py    : 2 topic publisher node
std2subscriber.py: 2 topic subscriber node

## senspublisher
This package contains: 

sensorInfoPublisher.py   : SensorInformation.msg publisher

sensorInfoSubscriber.py  : SensorInformation.msg subscriber

meters_to_feet_server.py : Meter to feet converter service server

meters_to_feet_client.py : Meter to feet converter service client

counter_with_delay_as.py : Counter with 1sec delay action server

counter_with_delay_ac.py : Counter with 1sec delay action client

## week1_assignment1.py : See [ROS_mooc_week_1_assignment_1.pdf] (https://github.com/usluenes/ROS/blob/master/senspublisher/ROS_mooc_week_1_assignment_1.pdf)
The main task of this assignment is to publish a new topic that contains the height of the detected boxes based on the setup

### Part 1
Problem Defition: 

When there is no box, the sensor publishes the maximum range value which is the distance to the
conveyor belt and it reports the distance to the top surface of the box when it does detect one.
However, there is also an indication in the data sheet that, although the advertised maximum range is
2.0m, the usable range is only 1.9m and any value above that is sensor noise, which means, there can
be false positives in the sensor data.

Solution: 
1. Subscribe to the /sensor_info topic.
2. Compute the height of the box from the sensor reading.
3. Filter out the false positives from the sensor due to sensor noise.

### Part 2
Problem Definition: 

you will create a new message type called
BoxHeightInformation.msg, which contains a place holder called “box_height” which is a floating
point number. This way you can share detected box height information with other ROS nodes in your
application.

Solution:
1. Create a new message type BoxHeightInformation.msg in the same folder where
SensorInformation.msg file is located.
2. Add a place holder box_height of floating point number type in this message file.
3. Generate the new message type

### Part 3
Problem Definition: 

Now, you are ready to publish a new ROS topic “/box_height_info” ONLY when a valid box is
detected. You are not supposed to publish anything when the detected box height was invalidated due
to sensor noise.

Solution:
1. Create an object of the new BoxHeightInformation message type ONLY when you need it, that
is only when the detected box height is valid.
2. Create a publisher for the new message type in the main python module.
3. Publish the box height information on the /box_height_info topic ONLY when the detected
box has a valid height.

## week1_assignment2.py : See ROS_mooc_week_1_assignment_2.pdf
The main task of this assignment is  call a ROS service via a service client. See that the same service can also be called via the command line, provided that the service server is running. This assignment consists of two parts.

### Part 1
Problem Defition: 

In Assignment1, you created a publisher for a new topic to publish box height information.

Solution:
1.  Create a subscriber to this new topic, i.e, ”/box_height_info”

### Part 2
Problem Defition: 
Now, the box height information in ”/box_height_info” topic is in ”m” (metres). And this information has to be converted to feet.  So, in the subscriber callback for this topic, you will call the ROS serviceto convert the distance information from this topic from metres to feet, using the ”metres_to_feet” ROS service.

Solution: 
1.  Add a call to the ”metres_to_feet” service in the subscriber callback.
2.  Use arospy.loginfolog message to display the converted information in feet with a meaningfullog message







