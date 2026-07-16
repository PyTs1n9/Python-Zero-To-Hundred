"""094 日志状态分析。"""

from pathlib import Path


def analyse_log(path):
    """读取日志，统计状态码、IP、平均耗时和最慢记录。"""
    status_counts = {}
    ip_addresses = set()
    records = []

    with open(path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            parts = line.split()
            if len(parts) != 4:
                continue
            time_text, ip, status_text, response_text = parts
            try:
                status = int(status_text)
                response_ms = float(response_text)
            except ValueError:
                continue
            if not 100 <= status <= 599 or response_ms < 0:
                continue

            status_counts[status] = status_counts.get(status, 0) + 1
            ip_addresses.add(ip)
            records.append(
                {
                    "line": line_number,
                    "time": time_text,
                    "ip": ip,
                    "status": status,
                    "response_ms": response_ms,
                }
            )

    average = 0.0
    if records:
        average = round(sum(record["response_ms"] for record in records) / len(records), 2)
    slowest = sorted(records, key=lambda record: (-record["response_ms"], record["line"]))[:3]
    return {
        "status": dict(sorted(status_counts.items())),
        "unique_ip": len(ip_addresses),
        "average_ms": average,
        "slowest": slowest,
    }


if __name__ == "__main__":
    sample = Path(__file__).with_name("access.log")
    print(analyse_log(sample))
