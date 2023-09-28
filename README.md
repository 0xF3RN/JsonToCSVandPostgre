# Project Documentation: JsonToCSVandPostgre
## Introduction

Welcome to the documentation for my project. This documentation will guide you through the installation and usage of the project components.

## Installation

To get started with the project, follow these installation steps:

1) Clone the repository:

```bash
git clone https://github.com/cutecei/JsonToCSVandPostgre.git
```

2) Navigate to the project directory:

```bash
cd JsonToCSVandPostgre
```

3) Make sure you have Python 3.10 installed on your system and install the project dependencies:

```bash
pip install -r requirements.txt
```

4) Run PostgreSQL

5) The script uses a configuration file (config.cfg) to specify database connection parameters.
```ini
[database]
host = localhost
port = 5432
name = db_name
user = db_user
password = db_password
```
   Replace localhost, 5432, db_name, db_user, db_password with your PostgreSQL database params.

6) Run the script
   
```bash
python main.py
```

## Usage

1) Prepare your JSON data in the desired format. Here's an example:

```json
[
  {
        "md5": "22222222222222222222222222222222",
        "sha256": "2222222222222222222222222222222222222222222222222222222222222222",
        "domain": "blog.kill.net"
    },
    {
        "md5": "33333333333333333333333333333333",
        "sha256": "3333333333333333333333333333333333333333333333333333333333333333",
        "domain": "blog.example.net"
    },
    {
        "md5": "44444444444444444444444444444444",
        "sha256": "4444444444444444444444444444444444444444444444444444444444444444",
        "domain": "example-.com"
    },
    {
        "md5": "55555555555555555555555555555555",
        "sha256": "5555555555555555555555555555555555555555555555555555555555555555"
    }
]
```

2) Run the script
```bash
python main.py
```
   The script will perform the following steps:
   - Check the JSON file for validity.
   - Add the valid JSON data to a CSV file (data.csv) and PostgreSQL DB.

3) Result (console output):
   - Adding new data
   ```cmd
   [INFO] Data has been added to CSV: [{'md5': '11111111111111111111111111111111', 'sha256': '1111111111111111111111111111111111111111111111111111111111111111', 'domain': 'blog.example.net'}]
   [INFO] Data has been added to PostgreSQL: {'md5': '11111111111111111111111111111111', 'sha256': '1111111111111111111111111111111111111111111111111111111111111111', 'domain': 'blog.example.net'}
   [INFO] Data has been added to CSV: [{'md5': '22222222222222222222222222222222', 'sha256': '2222222222222222222222222222222222222222222222222222222222222222', 'domain': 'blog.kill.net'}]        
   [INFO] Data has been added to PostgreSQL: {'md5': '22222222222222222222222222222222', 'sha256': '2222222222222222222222222222222222222222222222222222222222222222', 'domain': 'blog.kill.net'}   
   [INFO] Data has been added to CSV: [{'md5': '33333333333333333333333333333333', 'sha256': '3333333333333333333333333333333333333333333333333333333333333333', 'domain': 'blog.example.net'}]     
   [INFO] Data has been added to PostgreSQL: {'md5': '33333333333333333333333333333333', 'sha256': '3333333333333333333333333333333333333333333333333333333333333333', 'domain': 'blog.example.net'}
   [INFO] Data has been added to CSV: [{'md5': '77777777777777777777777777777777', 'sha256': '7777777777777777777777777777777777777777777777777777777777777777', 'domain': 'blog.example.net'}]
   [INFO] Data has been added to PostgreSQL: {'md5': '77777777777777777777777777777777', 'sha256': '7777777777777777777777777777777777777777777777777777777777777777', 'domain': 'blog.example.net'}
   ```
   - Adding existing data
   ```cmd
   [INFO] Already exists: ('11111111111111111111111111111111', '1111111111111111111111111111111111111111111111111111111111111111', 'blog.example.net')
   [INFO] Already exists: ('22222222222222222222222222222222', '2222222222222222222222222222222222222222222222222222222222222222', 'blog.kill.net')
   [INFO] Already exists: ('33333333333333333333333333333333', '3333333333333333333333333333333333333333333333333333333333333333', 'blog.example.net')
   [INFO] Already exists: ('77777777777777777777777777777777', '7777777777777777777777777777777777777777777777777777777777777777', 'blog.example.net')
   ```
## Function Descriptions

| Функция                | Описание|
|------------------------|-----------|
| `add_to_postgre(json_data: dict)` | Adds data to PostgreSQL. |
| `get_existing_data(csv_file="data.csv")`| Returns unique records. |
| `add_to_csv(json_data: dict, csv_file="data.csv")`| Adds data to a CSV file. |
| `json_reader_and_validator(json_file="data.json")` | Reads jsons and validates them. |
| `main()`| Main function. |


   
