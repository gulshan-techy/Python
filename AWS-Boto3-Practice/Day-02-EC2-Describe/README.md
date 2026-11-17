# Day 2 – Describe EC2 Instances Using Python Boto3

## About This Project

In this project, I used Python and AWS Boto3 to retrieve EC2 instance details programmatically.

I used the `describe_instances()` method to fetch information about EC2 instances from my AWS account.

## What I Learned

- Using the Boto3 EC2 client.
- Understanding the `describe_instances()` method.
- Working with AWS API responses.
- Understanding Reservations and Instances.
- Retrieving Instance ID and Name.
- Checking EC2 instance states.
- Retrieving Public and Private IP addresses.
- Retrieving Instance Type and Availability Zone.
- Retrieving EC2 instance Launch Time.
- Using nested for loops to process AWS responses.

## Technologies Used

- Python
- AWS Boto3
- Amazon EC2
- AWS CLI
- Visual Studio Code

## Project Structure

```text
Day-02-ec2-describe/
│
├── main.py
├── requirements.txt
└── README.md
```

## Step 1: Install Boto3

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
boto3
```

## Step 2: Configure AWS Credentials

If you have already configured AWS CLI in Day 1, you do not need to configure it again.

```bash
aws configure
```

Make sure your configured AWS Region is:

`ap-south-1`

Your AWS credentials should have permission to describe EC2 instances.

## Step 3: Run the Program

```bash
python main.py
```

## Information Retrieved

The program retrieves:

| Information | Description |
|---|---|
| Instance ID | Unique EC2 instance identifier |
| Name | EC2 instance Name tag |
| State | Current instance state |
| Public IP | Public IPv4 address, if assigned |
| Private IP | Private IPv4 address |
| Instance Type | EC2 compute configuration |
| Availability Zone | Location of the instance |
| Launch Time | Instance launch date and time |

## Important Boto3 Method

### describe_instances()

The `describe_instances()` method retrieves information about EC2 instances.

It returns a response containing Reservations and Instances.

Nested loops are used to access individual instance details.

## Learning Outcome

Successfully retrieved EC2 instance information using Python Boto3 without manually checking each instance in the AWS Management Console.

---

**Part of my AWS Boto3 Learning Journey – Day 02**
