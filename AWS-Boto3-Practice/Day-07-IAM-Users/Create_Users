import boto3

iam = boto3.client("iam")

response = iam.create_user(
    UserName="devops-user"
)

print("IAM User Created Successfully!")
print("Username:", response["User"]["UserName"])
print("User ID:", response["User"]["UserId"])
