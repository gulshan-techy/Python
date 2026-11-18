# Day 3 – EC2 Management Using Python Boto3

## About This Project

In this project, I created a simple EC2 Management Tool using Python and AWS Boto3.

The program allows users to manage EC2 instances through a command-line menu instead of manually performing every operation in the AWS Management Console.

## What I Learned

- Starting EC2 instances using `start_instances()`.
- Stopping EC2 instances using `stop_instances()`.
- Rebooting EC2 instances using `reboot_instances()`.
- Terminating EC2 instances using `terminate_instances()`.
- Filtering EC2 instances by their state.
- Retrieving Running and Stopped instances.
- Using Python functions and a while loop.
- Handling AWS API errors using ClientError.
- Creating a simple menu-based EC2 management tool.

## Technologies Used

- Python
- AWS Boto3
- Amazon EC2
- AWS CLI
- Visual Studio Code

## Project Structure

```
Day-03-ec2-management/
│
├── main.py
├── requirements.txt
└── README.md
```

## Step 1: Install Boto3

```bash
pip install -r requirements.txt
```

## Step 2: Configure AWS Credentials

If AWS CLI was already configured in Day 1, you do not need to configure it again.

```
aws configure
```

Make sure your default region is:

`ap-south-1`

## Step 3: Run the Program

```
python main.py
```

## Available Operations

| Option | Operation |
|---|---|
| 1 | Start EC2 Instance |
| 2 | Stop EC2 Instance |
| 3 | Reboot EC2 Instance |
| 4 | Terminate EC2 Instance |
| 5 | List Running Instances |
| 6 | List Stopped Instances |
| 7 | Exit Program |

## Important Boto3 Methods

| Method | Purpose |
|---|---|
| start_instances() | Starts EC2 instances |
| stop_instances() | Stops EC2 instances |
| reboot_instances() | Reboots EC2 instances |
| terminate_instances() | Terminates EC2 instances |
| describe_instances() | Retrieves EC2 instance information |

## EC2 Filters

The program uses EC2 filters to retrieve instances based on their state.

Example:

```
Filters=[
    {
        "Name": "instance-state-name",
        "Values": ["running"]
    }
]
```

This filter retrieves only Running instances.

## Important Safety Note

Terminating an EC2 instance is a destructive operation.

The program asks for confirmation before sending a termination request.

Always verify the Instance ID before performing lifecycle operations.

## Learning Outcome

Successfully created a simple command-line EC2 management tool using Python Boto3 to start, stop, reboot, terminate and filter EC2 instances.

---

**Part of my AWS Boto3 Learning Journey – Day 03**
