import boto3

iam = boto3.client("iam")

response = iam.get_user(
    UserName="devops-user"
)

user = response["User"]

print("Username:", user["UserName"])
print("User ID:", user["UserId"])
print("ARN:", user["Arn"])
print("Created:", user["CreateDate"])
