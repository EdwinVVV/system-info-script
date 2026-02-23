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
    # Note: "/" works on Linux/macOS. On Windows this maps to current drive for many setups.
    total, used, free = shutil.disk_usage("/")
    gb = 1024 ** 3
    return {
        "total_gb": round(total / gb, 2),
        "used_gb": round(used / gb, 2),
        "free_gb": round(free / gb, 2),
    }

def cpu_memory_info():
    """
    Uses psutil when available for accurate CPU/RAM stats on Windows/Linux.
    Falls back gracefully if psutil isn't installed.
    """
    try:
        import psutil  # pip install psutil
        cpu_percent = psutil.cpu_percent(interval=1)
        vm = psutil.virtual_memory()
        gb = 1024 ** 3
        return {
            "cpu_percent": cpu_percent,
            "ram_total_gb": round(vm.total / gb, 2),
            "ram_used_gb": round(vm.used / gb, 2),
            "ram_available_gb": round(vm.available / gb, 2),
            "ram_percent": vm.percent,
        }
    except Exception:
        return {
            "cpu_percent": "Unavailable (install psutil)",
            "ram_total_gb": "Unavailable (install psutil)",
            "ram_used_gb": "Unavailable (install psutil)",
            "ram_available_gb": "Unavailable (install psutil)",
            "ram_percent": "Unavailable (install psutil)",
        }

def format_report():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sys = system_info()
    net = network_info()
    disk = disk_info()
    cm = cpu_memory_info()

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

    lines.append("\n[CPU / Memory]")
    lines.append(f"CPU Usage: {cm['cpu_percent']}%")
    lines.append(f"RAM Total: {cm['ram_total_gb']} GB")
    lines.append(f"RAM Used: {cm['ram_used_gb']} GB")
    lines.append(f"RAM Available: {cm['ram_available_gb']} GB")
    lines.append(f"RAM Usage: {cm['ram_percent']}%")

    lines.append("\n[Network]")
    lines.append(f"Hostname: {net['hostname']}")
    lines.append(f"IP Address: {net['ip_address']}")

    lines.append("\n[Disk]")
    lines.append(f"Total: {disk['total_gb']} GB")
    lines.append(f"Used: {disk['used_gb']} GB")
    lines.append(f"Free: {disk['free_gb']} GB")

    lines.append("\n[Notes]")
    lines.append("- Install psutil for accurate CPU/RAM metrics: pip install psutil")
    lines.append("- Disk path uses '/' (works on Linux/macOS; Windows may map differently).")

    return "\n".join(lines)

if __name__ == "__main__":
    report = format_report()
    print(report)

    filename = "system_report.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\nReport saved to {filename}")
