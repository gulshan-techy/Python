# 🐍 Day 17: System & Process Monitoring with psutil (Part 1)

## 📌 Overview
So far, we have learned how to handle files and store data. But what if we want our Python scripts to look under the hood of our computer? How do we check how much RAM is being used, or what the current CPU load is?

Today, I started exploring **`psutil` (Process and System Utilities)**. It is a fantastic third-party Python library used for retrieving information on system hardware utilization and running processes.

---

## 🛠️ Concepts Learned

### 1. Installing `psutil`
Because `psutil` is a third-party library (not built into Python by default), we first need to install it via the terminal using `pip`:
```
pip install psutil
```

### 2. Checking CPU Usage
The CPU is the brain of the computer. We can easily check how many cores our system has and what percentage of the CPU is currently being utilized.
```
import psutil

# Get total physical and logical CPU cores
cpu_count = psutil.cpu_count(logical=True)
print("Total CPU Cores:", cpu_count)

# Get current CPU usage percentage (measured over 1 second)
cpu_usage = psutil.cpu_percent(interval=1)
print(f"Current CPU Usage: {cpu_usage}%")
```
3. Checking Memory (RAM) Usage
RAM is your computer's short-term memory. We can fetch total, available, and used memory metrics and convert bytes into Gigabytes (GB) for readability.
```
import psutil

# Get virtual memory statistics
memory = psutil.virtual_memory()

# Convert bytes to Gigabytes (1 GB = 1024^3 bytes)
total_gb = memory.total / (1024 ** 3)
available_gb = memory.available / (1024 ** 3)
used_percent = memory.percent

print(f"Total RAM: {total_gb:.2f} GB")
print(f"Available RAM: {available_gb:.2f} GB")
print(f"RAM Usage: {used_percent}%")
```

4. Checking Disk Storage Usage
We can also check how much storage space is left on our hard drive or SSD.

```
import psutil

# Get disk usage statistics (use '/' for Linux/Mac or 'C:\\' for Windows)
disk = psutil.disk_usage('/')

total_disk = disk.total / (1024 ** 3)
free_disk = disk.free / (1024 ** 3)
disk_percent = disk.percent

print(f"Total Disk Space: {total_disk:.2f} GB")
print(f"Free Disk Space: {free_disk:.2f} GB")
print(f"Disk Usage: {disk_percent}%")
```

💡 Summary
With psutil, Python gives us direct visibility into our machine's hardware health. In Part 1, we learned how to monitor the core pillars of any system: CPU, RAM, and Disk Storage.


