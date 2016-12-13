"""
####################################################
EC2 STARTUP SCRIPT
####################################################

iPython script for starting an AWS ec2 instance

"""
import json

# function to create instance with awscli
def create_instance(instance_type):

	response = !aws ec2 run-instances --image-id ami-a9d276c9 \
		--count 1 \
		--instance-type {instance_type} \
		--key-name ec2_rob \
		--security-groups ssh_only \
		--block-device-mappings "[{\"DeviceName\":\"/dev/sdf\",\"Ebs\":{\"VolumeSize\":10,\"DeleteOnTermination\":false}}]" \
		--user-data file:///Users/robertdalton/Documents/learning/online-courses/galvanize/student_lectures/aws/examples/boostrap-ec2.sh
	
	return response


# function to get instance id
def extract_id(response):
	response = json.loads(raw_response)
	id = response["Instances"][0]["InstanceID"]

	return id


# function to create name tag
def add_name_tag(id, name):
	!aws ec2 create-tags --resources id \
		--tags Key=Name,Value=awsTestInstance


if __name__=="__main__":
	response = create_instance("t2.micro")

	print response
