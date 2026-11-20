import boto3

iam = boto3.client("iam")

response = iam.delete_user(
    UserName="devops-user"
)

print("IAM User Deleted Successfully!")
