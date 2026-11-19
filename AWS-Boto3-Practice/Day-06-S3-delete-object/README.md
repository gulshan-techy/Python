# Day 06 – AWS S3 Advanced Operations Using Python & Boto3

## Overview

This project demonstrates basic advanced operations and security concepts in Amazon S3.

Using Python and Boto3, I practiced deleting S3 objects and explored important S3 features such as Versioning, Bucket Policies, Block Public Access, and Static Website Hosting.

## What I Learned

- Delete S3 objects using Boto3.
- Understand Amazon S3 Versioning.
- Understand S3 Bucket Policies.
- Learn how Block Public Access protects S3 resources.
- Understand S3 Static Website Hosting.
- Perform S3 bucket cleanup.

## Technologies Used

- Python
- AWS S3
- AWS Boto3 SDK
- AWS Management Console
- VS Code

## Project Structure

```text
day-03-s3-advanced-operations/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

Install Boto3:

```bash
pip install -r requirements.txt
```

## AWS Configuration

Configure AWS credentials:

```bash
aws configure
```

Make sure your IAM identity has the required S3 permissions.

## Run the Project

```bash
python main.py
```

## Boto3 Method Practiced

| Method | Purpose |
|---|---|
| `delete_object()` | Deletes an S3 object or creates a delete marker when versioning is enabled |

## AWS S3 Concepts Covered

### 1. Versioning
Maintains multiple versions of an object and helps recover previous versions.

### 2. Bucket Policy
A JSON-based resource policy that controls access to an S3 bucket and its objects.

### 3. Block Public Access
Helps prevent accidental public exposure of S3 resources.

### 4. Static Website Hosting
Allows hosting static HTML, CSS, and JavaScript websites using Amazon S3.

## Security Note

Keep S3 buckets private by default. Public access should only be configured when it is genuinely required.

## Learning Outcome

After completing this project, I understand basic S3 object deletion, versioning, bucket access policies, public access controls, and static website hosting.
