import boto3

iam = boto3.client("iam")


# 1. List IAM Groups
def list_groups():
    print("\nExisting IAM Groups:")

    paginator = iam.get_paginator("list_groups")

    group_count = 0

    for page in paginator.paginate():
        for group in page["Groups"]:
            group_count += 1

            print(f"\nGroup Name: {group['GroupName']}")
            print(f"Group ID: {group['GroupId']}")
            print(f"Group ARN: {group['Arn']}")

    if group_count == 0:
        print("No IAM groups found.")

    print(f"\nTotal Groups: {group_count}")


# 2. Create IAM Group
def create_group():
    group_name = input("Enter Group Name: ").strip()

    if not group_name:
        print("Group name cannot be empty.")
        return

    response = iam.create_group(
        GroupName=group_name
    )

    group = response["Group"]

    print("\nGroup Created Successfully!")
    print("Group Name:", group["GroupName"])
    print("Group ARN:", group["Arn"])


# 3. Add User to Group
def add_user_to_group():
    group_name = input("Enter Group Name: ").strip()
    user_name = input("Enter IAM Username: ").strip()

    if not group_name or not user_name:
        print("Group name and username are required.")
        return

    iam.add_user_to_group(
        GroupName=group_name,
        UserName=user_name
    )

    print(f"\n{user_name} added to {group_name} successfully!")


# 4. Remove User from Group
def remove_user_from_group():
    group_name = input("Enter Group Name: ").strip()
    user_name = input("Enter IAM Username: ").strip()

    if not group_name or not user_name:
        print("Group name and username are required.")
        return

    iam.remove_user_from_group(
        GroupName=group_name,
        UserName=user_name
    )

    print(f"\n{user_name} removed from {group_name} successfully!")


# Main Menu
def main():
    while True:
        print("\n========== AWS IAM GROUP MANAGEMENT ==========")
        print("1. List IAM Groups")
        print("2. Create IAM Group")
        print("3. Add User to Group")
        print("4. Remove User from Group")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            list_groups()

        elif choice == "2":
            create_group()

        elif choice == "3":
            add_user_to_group()

        elif choice == "4":
            remove_user_from_group()

        elif choice == "5":
            print("Exiting IAM Group Management.")
            break

        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()
