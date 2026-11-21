import boto3
import json

iam = boto3.client("iam")

# 1. List Customer Managed Policies
def list_policies():
    print("\n========== IAM POLICIES ==========")

    paginator = iam.get_paginator("list_policies")

    policy_count = 0

    for page in paginator.paginate(Scope="Local"):
        for policy in page["Policies"]:
            policy_count += 1

            print(f"\nPolicy Name: {policy['PolicyName']}")
            print(f"Policy ARN: {policy['Arn']}")
            print(f"Policy ID: {policy['PolicyId']}")
            print(f"Default Version: {policy['DefaultVersionId']}")
            print("--------------------------------")

    if policy_count == 0:
        print("No customer-managed policies found.")

    print(f"\nTotal Policies: {policy_count}")

# 2. Create Custom IAM Policy
def create_policy():
    policy_name = input("Enter Policy Name: ").strip()
    bucket_name = input("Enter S3 Bucket Name: ").strip()

    if not policy_name or not bucket_name:
        print("Policy name and bucket name are required.")
        return

    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject"
                ],
                "Resource": f"arn:aws:s3:::{bucket_name}/*"
            }
        ]
    }

    response = iam.create_policy(
        PolicyName=policy_name,
        PolicyDocument=json.dumps(policy_document),
        Description="Allows reading objects from a specific S3 bucket"
    )

    policy = response["Policy"]

    print("\nPolicy Created Successfully!")
    print("Policy Name:", policy["PolicyName"])
    print("Policy ARN:", policy["Arn"])


# 3. Get IAM Policy Details
def get_policy():
    policy_arn = input("Enter Policy ARN: ").strip()

    if not policy_arn:
        print("Policy ARN is required.")
        return

    response = iam.get_policy(
        PolicyArn=policy_arn
    )

    policy = response["Policy"]

    print("\n========== POLICY DETAILS ==========")
    print("Policy Name:", policy["PolicyName"])
    print("Policy ARN:", policy["Arn"])
    print("Policy ID:", policy["PolicyId"])
    print("Default Version:", policy["DefaultVersionId"])
    print("Attachment Count:", policy["AttachmentCount"])

    # Fetch the actual policy document
    version_response = iam.get_policy_version(
        PolicyArn=policy_arn,
        VersionId=policy["DefaultVersionId"]
    )

    print("\nPolicy Document:")
    print(json.dumps(
        version_response["PolicyVersion"]["Document"],
        indent=4
    ))

# 4. Delete IAM Policy
def delete_policy():
    policy_arn = input("Enter Policy ARN to delete: ").strip()

    if not policy_arn:
        print("Policy ARN is required.")
        return

    confirm = input(
        "Are you sure you want to delete this policy? (yes/no): "
    ).strip().lower()

    if confirm != "yes":
        print("Deletion cancelled.")
        return

    iam.delete_policy(
        PolicyArn=policy_arn
    )

    print("Policy Deleted Successfully!")


# Main Menu
def main():
    while True:
        print("\n========== AWS IAM POLICY MANAGEMENT ==========")
        print("1. List Customer Managed Policies")
        print("2. Create Custom IAM Policy")
        print("3. Get IAM Policy Details")
        print("4. Delete IAM Policy")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            list_policies()

        elif choice == "2":
            create_policy()

        elif choice == "3":
            get_policy()

        elif choice == "4":
            delete_policy()

        elif choice == "5":
            print("Exiting IAM Policy Management.")
            break

        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()
