import boto3
import json

iam = boto3.client("iam")

ROLE_NAME = "EC2-S3-ReadOnly-Role"

POLICY_ARN = (
    "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
)

trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

def create_role():
    response = iam.create_role(
        RoleName=ROLE_NAME,
        AssumeRolePolicyDocument=json.dumps(trust_policy),
        Description="EC2 role for S3 read-only access"
    )

    print("Role created successfully!")
    print("Role ARN:", response["Role"]["Arn"])

def get_role():
    response = iam.get_role(
        RoleName=ROLE_NAME
    )

    role = response["Role"]

    print("Role Name:", role["RoleName"])
    print("Role ARN:", role["Arn"])
    print("Trust Policy:", role["AssumeRolePolicyDocument"])

def list_roles():
    paginator = iam.get_paginator("list_roles")

    for page in paginator.paginate():
        for role in page["Roles"]:
            print(role["RoleName"], role["Arn"])

def attach_policy():
    iam.attach_role_policy(
        RoleName=ROLE_NAME,
        PolicyArn=POLICY_ARN
    )

    print("Policy attached successfully!")

def detach_policy():
    iam.detach_role_policy(
        RoleName=ROLE_NAME,
        PolicyArn=POLICY_ARN
    )

    print("Policy detached successfully!")

def list_attached_policies():
    response = iam.list_attached_role_policies(
        RoleName=ROLE_NAME
    )

    for policy in response["AttachedPolicies"]:
        print(policy["PolicyName"], policy["PolicyArn"])

def delete_role():
    iam.delete_role(
        RoleName=ROLE_NAME
    )

    print("Role deleted successfully!")

while True:

    print("\n===== IAM ROLE MANAGEMENT =====")
    print("1. Create IAM Role")
    print("2. Get Role Details")
    print("3. List IAM Roles")
    print("4. Attach Policy")
    print("5. Detach Policy")
    print("6. List Attached Policies")
    print("7. Delete IAM Role")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_role()

    elif choice == "2":
        get_role()

    elif choice == "3":
        list_roles()

    elif choice == "4":
        attach_policy()

    elif choice == "5":
        detach_policy()

    elif choice == "6":
        list_attached_policies()

    elif choice == "7":
        confirm = input("Are you sure? (yes/no): ")

        if confirm.lower() == "yes":
            delete_role()

    elif choice == "8":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
