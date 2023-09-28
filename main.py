import json
import re
import csv
import psycopg2
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")
db_params = config["PostgreSQL"]
connection = psycopg2.connect(host=db_params["host"], dbname=db_params["name"],
                              user=db_params["user"], password=db_params["password"],
                              port=db_params["port"])

md5_pattern = r'\b[0-9a-fA-F]{32}\b'
sha256_pattern = r'\b[0-9a-fA-F]{64}\b'
domain_pattern = r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$"


def add_to_postgre(json_data: dict):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS data(
                    id SERIAL PRIMARY KEY,
                    md5_value VARCHAR(32),
                    sha256_value VARCHAR(64),
                    domain VARCHAR
                );
            """)
        cur.execute(f"""INSERT INTO data (md5_value, sha256_value, domain) VALUES
            ('{json_data["md5"]}', '{json_data["sha256"]}', '{json_data["domain"]}');
        """)
        cur.close()
        print(f"[INFO] Data has been added to PostgreSQL: {json_data}")
    except Exception as _e:
        print(_e)


def get_existing_data(csv_file="data.csv"):
    try:
        existing_data = set()
        with open(csv_file, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                record_tuple = (row["md5"], row["sha256"], row["domain"])
                existing_data.add(record_tuple)
        return existing_data
    except Exception:
        return ()


def add_to_csv(json_data: dict, csv_file="data.csv"):
    data = [json_data]
    with open(csv_file, "a", newline="") as file:
        fieldnames = ["md5", "sha256", "domain"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        for row in data:
            writer.writerow(row)
        print(f"[INFO] Data has been added to CSV: {data}")


def json_reader_and_validator(json_file="data.json"):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
            for data_key in data:
                if "md5" and "sha256" and "domain" in data_key:
                    condition = re.match(md5_pattern, data_key["md5"]) and re.match(sha256_pattern, data_key["sha256"]) and re.match(domain_pattern, data_key["domain"])
                    if condition:
                        data_to_check = (data_key["md5"], data_key["sha256"], data_key["domain"])
                        existing_data = get_existing_data()
                        if data_to_check in existing_data:
                            print(f"[INFO] Already exists: {data_to_check}")
                        else:
                            add_to_csv(data_key)
                            add_to_postgre(data_key)
    except Exception as e:
        print(e)


def main():
    json_reader_and_validator()


if __name__ == "__main__":
    main()
    connection.commit()
    connection.close()
