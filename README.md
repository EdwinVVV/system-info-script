# System Info Script (Python)

A lightweight IT support utility that gathers basic system diagnostics in a single run.

## Problem

Help desk technicians often need to quickly gather system details during troubleshooting.
Manually checking OS version, hostname, disk space, and network configuration takes time and can lead to inconsistent reporting.

## Solution

This Python script automates the collection of:

- Operating system details
- Machine architecture and processor
- Hostname and IP address
- Disk usage statistics (total, used, free)
- Timestamped formatted report output

## How It Works

The script uses:

- `platform` for OS and hardware info
- `socket` for hostname and IP resolution
- `shutil` for disk usage
- `datetime` for report timestamps

## How to Run

```bash
python system_info.py
