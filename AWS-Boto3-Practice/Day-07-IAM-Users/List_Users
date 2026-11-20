import boto3

iam = boto3.client("iam")

response = iam.list_users()

print("\n=======All Iam Users List=======\n")

for user in response["Users"]:
    print("Username:", user["UserName"])
    print("User ID:", user["UserId"])
    print("Created:", user["CreateDate"])
    print("---------------------------------")
