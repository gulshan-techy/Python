import boto3

region = "ap-south-1"
# Create EC2 Client
ec2 = boto3.client("ec2", region_name=region)

# Function to Describe EC2 Instances
def describe_instances():
        # Get EC2 Instance Details
        response = ec2.describe_instances()
        # Check Reservations
        for reservation in response["Reservations"]:
            # Get Instances
            for instance in reservation["Instances"]:
                instance_id = instance["InstanceId"]
                name = "N/A"

                for tag in instance.get("Tags", []):
                    if tag["Key"] == "Name":
                        name = tag["Value"]

                state = instance["State"]["Name"]
                public_ip = instance.get("PublicIpAddress", "N/A")
                private_ip = instance.get("PrivateIpAddress", "N/A")
                instance_type = instance["InstanceType"]
                az = instance["Placement"]["AvailabilityZone"]
                launch_time = instance["LaunchTime"]

                print("-" * 60)
                print("Instance ID:", instance_id)
                print("Name:", name)
                print("State:", state)
                print("Public IP:", public_ip)
                print("Private IP:", private_ip)
                print("Instance Type:", instance_type)
                print("Availability Zone:", az)
                print("Launch Time:", launch_time)
        print("-" * 60)
# Call Function
describe_instances()
