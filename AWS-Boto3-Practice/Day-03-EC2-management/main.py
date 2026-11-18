import boto3
from botocore.exceptions import ClientError

# AWS Region
region = "ap-south-1"

# Create EC2 Client
ec2 = boto3.client("ec2", region_name=region)


# Function to Start EC2 Instance
def start_instance():

    instance_id = input("Enter Instance ID to Start: ")

    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print("Start request sent successfully!")

    except ClientError as e:
        print("Error:", e)


# Function to Stop EC2 Instance
def stop_instance():

    instance_id = input("Enter Instance ID to Stop: ")

    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print("Stop request sent successfully!")

    except ClientError as e:
        print("Error:", e)


# Function to Reboot EC2 Instance
def reboot_instance():

    instance_id = input("Enter Instance ID to Reboot: ")

    try:
        ec2.reboot_instances(InstanceIds=[instance_id])
        print("Reboot request sent successfully!")

    except ClientError as e:
        print("Error:", e)


# Function to Terminate EC2 Instance
def terminate_instance():

    instance_id = input("Enter Instance ID to Terminate: ")

    confirm = input("Are you sure? Type YES to confirm: ")

    if confirm == "YES":

        try:
            ec2.terminate_instances(InstanceIds=[instance_id])
            print("Termination request sent successfully!")

        except ClientError as e:
            print("Error:", e)

    else:
        print("Termination cancelled.")


# Function to List Running or Stopped Instances
def list_instances(state):

    try:

        response = ec2.describe_instances(
            Filters=[
                {
                    "Name": "instance-state-name",
                    "Values": [state]
                }
            ]
        )

        print(f"\n{state.upper()} EC2 INSTANCES")

        for reservation in response["Reservations"]:

            for instance in reservation["Instances"]:

                instance_id = instance["InstanceId"]
                instance_type = instance["InstanceType"]

                print("Instance ID:", instance_id)
                print("Instance Type:", instance_type)
                print("-" * 40)

    except ClientError as e:
        print("Error:", e)


# Main Menu
while True:

    print("\n===== EC2 MANAGEMENT TOOL =====")

    print("1. Start Instance")
    print("2. Stop Instance")
    print("3. Reboot Instance")
    print("4. Terminate Instance")
    print("5. List Running Instances")
    print("6. List Stopped Instances")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        start_instance()

    elif choice == "2":
        stop_instance()

    elif choice == "3":
        reboot_instance()

    elif choice == "4":
        terminate_instance()

    elif choice == "5":
        list_instances("running")

    elif choice == "6":
        list_instances("stopped")

    elif choice == "7":
        print("Exiting EC2 Management Tool.")
        break

    else:
        print("Invalid choice! Please select 1 to 7.")
