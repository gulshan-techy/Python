import boto3

# AWS Region
region = "ap-south-1"

# Create EC2 Client
ec2 = boto3.client(
    "ec2",
    region_name=region)

# Function to Launch EC2 Instance
def launch_instance():

        # Launch EC2 Instance
        response = ec2.run_instances(

            ImageId="ami-04b0b8ee9ce90920a", # It's Amazon Linux 2023 AMI ID 
            InstanceType="t3.micro",
            KeyName="mum-key",
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [
                        {
                            "Key": "Name",
                            "Value": "Boto3-EC2"
                        }
                    ]
                }
            ]
        )
        # Get Instance ID
        instance_id = response["Instances"][0]["InstanceId"]
        print("EC2 Instance Launched Successfully!")
        print("Instance ID:", instance_id)

# Call Function
launch_instance()
