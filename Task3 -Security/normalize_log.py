
import csv
from datetime import datetime

INPUT_FILE = "auth.log"
OUTPUT_FILE = "normalized_logs.csv"


def normalize_logs():
    normalized_data = []

    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                # Skip empty lines and comments
                if not line or line.startswith("#"):
                    continue

                fields = [field.strip() for field in line.split("|")]

                if len(fields) != 5:
                    print(f"Skipping invalid line: {line_number}")
                    continue

                timestamp, ip, account, action, result = fields

                try:
                    parsed_time = datetime.strptime(
                        timestamp, "%Y-%m-%d %H:%M:%S"
                    )
                except ValueError:
                    print(f"Invalid timestamp at line: {line_number}")
                    continue

                normalized_data.append({
                    "timestamp": parsed_time.isoformat(sep=" "),
                    "ip_address": ip,
                    "account": account,
                    "action": action.upper(),
                    "result": result.upper()
                })

        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
            fieldnames = [
                "timestamp", "ip_address",
                "account", "action", "result"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(normalized_data)

        print("Log normalization completed!")
        print(f"Total valid events: {len(normalized_data)}")
        print(f"Output saved to: {OUTPUT_FILE}")

    except FileNotFoundError:
        print("Error: auth.log file not found.")
        print("Keep auth.log in the same folder as this script.")


if __name__ == "__main__":
    normalize_logs()
