# AWS IAM Groups Management Using Python & Boto3

## 📌 Project Overview

This project demonstrates how to automate AWS Identity and Access Management (IAM) Group operations using Python and the AWS SDK for Python (Boto3).

Instead of manually managing IAM groups through the AWS Management Console, this project provides a menu-driven Python application to perform common IAM Group management tasks programmatically.

**Day 02 of my AWS Boto3 Learning Journey.**

## 🎯 Problem Statement

In organizations, managing multiple IAM users and their group memberships manually can become repetitive and time-consuming.

For example:
- Creating IAM groups for different departments.
- Adding new employees to the appropriate groups.
- Removing users from groups when their roles change.
- Retrieving existing IAM groups for auditing.

Performing these repetitive operations manually can increase operational effort and the possibility of human error.

## 💡 Solution

This project uses Python and Boto3 to automate IAM Group management through AWS IAM APIs.

It provides a simple interactive menu to:
- List all IAM groups.
- Create new IAM groups.
- Add IAM users to groups.
- Remove IAM users from groups.

## 🛠️ Technologies Used

- Python
- AWS Boto3 SDK
- AWS IAM
- AWS CLI
- Amazon Web Services

## 📂 Project Structure

```text
day-02-iam-groups/
│
├── main.py
└── README.md
```

## ⚙️ Prerequisites

Before running this project, make sure you have:

1. An AWS account.
2. Python installed.
3. Boto3 installed.
4. AWS credentials configured.
5. An IAM identity with the required IAM permissions.
6. Existing IAM users for testing user-to-group operations.

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Directory

```bash
cd day-02-iam-groups
```

### Step 3: Install Boto3

```bash
pip install boto3
```

### Step 4: Configure AWS Credentials

```bash
aws configure
```

Provide your AWS Access Key, Secret Access Key, default region and output format when prompted.

Do not hardcode AWS credentials in your Python source code or commit them to GitHub.

### Step 5: Run the Application

```bash
python main.py
```

## 📚 Boto3 Operations Covered

### 1. List IAM Groups

**Method:** `list_groups()`

Retrieves IAM groups from the AWS account.

```python
response = iam.list_groups()
```

The project uses a Boto3 paginator to retrieve all groups across multiple response pages.

**Use Case:** IAM inventory and access auditing.

### 2. Create IAM Group

**Method:** `create_group()`

Creates a new IAM group.

```python
response = iam.create_group(
    GroupName="Developers"
)
```

**Use Case:** Automating group creation for departments such as Developers, Testers and Administrators.

### 3. Add User to Group

**Method:** `add_user_to_group()`

Adds an existing IAM user to an existing IAM group.

```python
iam.add_user_to_group(
    GroupName="Developers",
    UserName="devops-user"
)
```

**Use Case:** Assigning employees to appropriate groups based on their job roles.

### 4. Remove User from Group

**Method:** `remove_user_from_group()`

Removes an IAM user from a group without deleting the user account.

```python
iam.remove_user_from_group(
    GroupName="Developers",
    UserName="devops-user"
)
```

**Use Case:** Managing group memberships when an employee changes departments or responsibilities.

## 🔐 Required IAM Permissions

The AWS identity executing this Python application requires the following permissions:

| IAM Action | Purpose |
|---|---|
| `iam:ListGroups` | List IAM groups |
| `iam:CreateGroup` | Create IAM groups |
| `iam:AddUserToGroup` | Add users to groups |
| `iam:RemoveUserFromGroup` | Remove users from groups |

Follow the **Principle of Least Privilege** and grant only the permissions required by the application.

## 🖥️ Application Menu

```text
========== AWS IAM GROUP MANAGEMENT ==========

1. List IAM Groups
2. Create IAM Group
3. Add User to Group
4. Remove User from Group
5. Exit

Enter your choice (1-5):
```

## 🔍 Key Learning Outcomes

Through this project, I learned:

- How to connect to AWS IAM using Boto3.
- How to retrieve IAM groups programmatically.
- How to create IAM groups using Python.
- How to manage IAM user-group memberships.
- How to use Boto3 pagination.
- How to automate repetitive AWS IAM operations.
- Why IAM Group-based permission management is useful.
- Why the Principle of Least Privilege matters in cloud security.

## ⚠️ Important Security Notes

- Creating an IAM group does not automatically grant permissions to its members.
- Permissions can be granted by attaching IAM policies to the group.
- IAM groups cannot contain other IAM groups.
- Removing a user from a group does not delete the IAM user.
- Users may still have permissions through other groups or directly attached policies.
- Never upload AWS access keys or secret keys to GitHub.

## 📈 Future Improvements

This project can be extended with:

- IAM policy attachment and detachment.
- IAM group membership auditing.
- Automated user provisioning.
- Error handling for invalid users and groups.
- IAM access review reports.

## 👨‍💻 Learning Journey

This project is part of my hands-on **AWS Boto3 Learning Journey**, where I am learning to automate AWS services using Python.

**Day 01:** IAM Users Management  
**Day 02:** IAM Groups Management  
**Day 03:** IAM Policies Management (Upcoming)

---

⭐ If you find this project useful, feel free to explore the code and share your feedback.

#Python #AWS #Boto3 #AWSIAM #CloudComputing #DevOps #AWSAutomation
