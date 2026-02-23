import platform
import socket
import shutil
from datetime import datetime

def system_info():
    return {
        "os": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }

def network_info():
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except Exception:
        ip_address = "Unavailable"
    return {"hostname": hostname, "ip_address": ip_address}

def disk_info():
    total, used, free = shutil.disk_usage("/")
    gb = 1024 ** 3
    return {
        "total_gb": round(total / gb, 2),
        "used_gb": round(used / gb, 2),
        "free_gb": round(free / gb, 2),
    }

def format_report():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sys = system_info()
    net = network_info()
    disk = disk_info()

    lines = []
    lines.append("=" * 55)
    lines.append("SYSTEM DIAGNOSTIC REPORT")
    lines.append(f"Generated: {now}")
    lines.append("=" * 55)

    lines.append("\n[System]")
    lines.append(f"OS: {sys['os']} {sys['release']}")
    lines.append(f"Version: {sys['version']}")
    lines.append(f"Machine: {sys['machine']}")
    lines.append(f"Processor: {sys['processor']}")

    lines.append("\n[Network]")
    lines.append(f"Hostname: {net['hostname']}")
    lines.append(f"IP Address: {net['ip_address']}")

    lines.append("\n[Disk]")
    lines.append(f"Total: {disk['total_gb']} GB")
    lines.append(f"Used:  {disk['used_gb']} GB")
    lines.append(f"Free:  {disk['free_gb']} GB")

    lines.append("\nNotes:")
    lines.append("- Disk path uses '/' (works on Windows too in Python, but may map differently).")
    lines.append("- IP resolution depends on local network/DNS configuration.")

    return "\n".join(lines)

if __name__ == "__main__":
    print(format_report())
