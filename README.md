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

3) Install the project dependencies:
```bash
pip install -r requirements.txt
```

4) Run PostgreSQL server
   Also on this stage you should open config.cfg and fullfil your data:
```cfg
[PostgreSQL]
host = localhost
port = 5432
name = postgres
user = postgres
password = 12345
```

6) Run python script
```bash
python main.py
```

## Usage

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
