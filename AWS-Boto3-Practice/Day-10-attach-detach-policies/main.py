import boto3

iam = boto3.client("iam")

def attach_user_policy():
    user_name = input("Enter IAM username: ")
    policy_arn = input("Enter Policy ARN: ")

    iam.attach_user_policy(
        UserName=user_name,
        PolicyArn=policy_arn
    )

    print("Policy attached to user successfully!")

def detach_user_policy():
    user_name = input("Enter IAM username: ")
    policy_arn = input("Enter Policy ARN: ")

    iam.detach_user_policy(
        UserName=user_name,
        PolicyArn=policy_arn)

    print("Policy detached from user successfully!")

def attach_group_policy():
    group_name = input("Enter IAM group name: ")
    policy_arn = input("Enter Policy ARN: ")

    iam.attach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )

    print("Policy attached to group successfully!")

def detach_group_policy():
    group_name = input("Enter IAM group name: ")
    policy_arn = input("Enter Policy ARN: ")

    iam.detach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn)

    print("Policy detached from group successfully!")

def list_user_policies():
    user_name = input("Enter IAM username: ")

    response = iam.list_attached_user_policies(
        UserName=user_name)

    for policy in response["AttachedPolicies"]:
        print(policy["PolicyName"], policy["PolicyArn"])

def list_group_policies():
    group_name = input("Enter IAM group name: ")

    response = iam.list_attached_group_policies(
        GroupName=group_name)

    for policy in response["AttachedPolicies"]:
        print(policy["PolicyName"], policy["PolicyArn"])

while True:

    print("\n===== IAM POLICY MANAGEMENT =====")
    print("1. Attach policy to user")
    print("2. Detach policy from user")
    print("3. Attach policy to group")
    print("4. Detach policy from group")
    print("5. List user policies")
    print("6. List group policies")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        attach_user_policy()

    elif choice == "2":
        detach_user_policy()

    elif choice == "3":
        attach_group_policy()

    elif choice == "4":
        detach_group_policy()

    elif choice == "5":
        list_user_policies()

    elif choice == "6":
        list_group_policies()

    elif choice == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
