import boto3
from botocore.exceptions import ClientError

iam = boto3.client("iam")


def create_access_key():

    username = input("Enter IAM Username: ")

    try:
        response = iam.create_access_key(
            UserName=username
        )

        key = response["AccessKey"]

        print("\nAccess Key Created Successfully!")
        print("Access Key ID:", key["AccessKeyId"])
        print("Secret Access Key:", key["SecretAccessKey"])

        print("\nIMPORTANT: Save the Secret Access Key securely.")
        print("It cannot be retrieved again.")

    except ClientError as e:
        print("Error:", e.response["Error"]["Message"])


def list_access_keys():

    username = input("Enter IAM Username: ")

    try:
        response = iam.list_access_keys(
            UserName=username
        )

        keys = response["AccessKeyMetadata"]

        if not keys:
            print("No Access Keys found.")
            return

        for key in keys:
            print("\nAccess Key ID:", key["AccessKeyId"])
            print("Status:", key["Status"])
            print("Created:", key["CreateDate"])

    except ClientError as e:
        print("Error:", e.response["Error"]["Message"])


def update_access_key():

    username = input("Enter IAM Username: ")
    key_id = input("Enter Access Key ID: ")
    status = input("Enter Status (Active/Inactive): ").capitalize()

    if status not in ["Active", "Inactive"]:
        print("Invalid status!")
        return

    try:
        iam.update_access_key(
            UserName=username,
            AccessKeyId=key_id,
            Status=status
        )

        print("Access Key status updated successfully!")

    except ClientError as e:
        print("Error:", e.response["Error"]["Message"])


def check_last_used():

    key_id = input("Enter Access Key ID: ")

    try:
        response = iam.get_access_key_last_used(
            AccessKeyId=key_id
        )

        print("\nLast Used Details:")
        print(response["AccessKeyLastUsed"])

    except ClientError as e:
        print("Error:", e.response["Error"]["Message"])


def delete_access_key():

    username = input("Enter IAM Username: ")
    key_id = input("Enter Access Key ID: ")

    confirm = input("Are you sure? (yes/no): ")

    if confirm.lower() != "yes":
        print("Deletion cancelled.")
        return

    try:
        iam.delete_access_key(
            UserName=username,
            AccessKeyId=key_id
        )

        print("Access Key deleted successfully!")

    except ClientError as e:
        print("Error:", e.response["Error"]["Message"])


while True:

    print("\n===== IAM ACCESS KEY MANAGER =====")
    print("1. Create Access Key")
    print("2. List Access Keys")
    print("3. Activate / Deactivate Access Key")
    print("4. Check Last Used Details")
    print("5. Delete Access Key")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        create_access_key()

    elif choice == "2":
        list_access_keys()

    elif choice == "3":
        update_access_key()

    elif choice == "4":
        check_last_used()

    elif choice == "5":
        delete_access_key()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
