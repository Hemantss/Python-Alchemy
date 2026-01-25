import argparse
from data_manager import save_record, load_records
from logger import log_info

def main():
    parser = argparse.ArgumentParser(
        description="Data Utility App — manage and log JSON-based data records."
    )

    parser.add_argument("--add", nargs="+", help="Add a new record as key=value pairs")
    parser.add_argument("--show", action="store_true", help="Show all stored records")

    args = parser.parse_args()

    if args.add:
        data = {}
        for pair in args.add:
            if "=" in pair:
                key, value = pair.split("=", 1)
                data[key] = value
        save_record(data)
        log_info(f"Added new record: {data}")

    elif args.show:
        records = load_records()
        for rec in records:
            print(rec)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
