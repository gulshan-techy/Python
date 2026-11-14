# Launch EC2 Instance Using Python Boto3

## About This Project

In this project, I learned how to launch an Amazon EC2 instance using Python and the Boto3 library.

Instead of manually launching an EC2 instance through the AWS Management Console, I used Python code to automate the process.

## What I Learned

- What is Amazon EC2?
- What is Boto3?
- What is an AMI?
- What is an EC2 Instance Type?
- What is a Key Pair?
- How to connect Python with AWS.
- How to launch an EC2 instance using Boto3.

## Services and Tools Used

- Amazon EC2
- AWS IAM
- Python
- Boto3
- AWS CLI
- VS Code

## Project Structure

```
Day-01-EC2-Launch/
│
├── main.py
├── README.md
└── requirements.txt
```

## Step 1: Install Boto3

```
pip install boto3
```

## Step 2: Configure AWS Credentials

```
aws configure
```

Enter your AWS Access Key, Secret Key and Region.

## Step 3: Update EC2 Details

Before running the Python program, update:

- AMI ID
- Instance Type
- Key Pair Name
- AWS Region

Use an AMI ID available in your selected AWS region.

## Step 4: Run the Program

```
python main.py
```

## Expected Output

```
EC2 Instance Launched Successfully!

Instance ID: i-xxxxxxxxxxxxxxxxx
```

## Important Boto3 Function

**run_instances()**

This function launches one or more EC2 instances using the provided configuration.

## Key Learnings

I learned how to automate EC2 instance creation using Python instead of manually creating instances through the AWS Console.

## Cleanup

After completing the practice, terminate the EC2 instance from the AWS Management Console to avoid unnecessary charges.
