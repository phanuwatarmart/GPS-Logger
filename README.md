# GPS Logger

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-success)
![Status](https://img.shields.io/badge/Status-Simulation%20Tested-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A modular GPS logging system developed with Python for Raspberry Pi Zero 2 W.

The application records GPS coordinates together with timestamps and stores the data in CSV format. It includes a **Simulation Mode** for development and testing, making it possible to develop the software without requiring GPS hardware.

---

# Demo

> *(Add a screenshot after pushing to GitHub.)*

![GPS Logger](images/demo.png)

---

# System Architecture

```text
                  +----------------+
                  |   config.py    |
                  +----------------+
                           │
                           ▼
+-----------+     +----------------+      +--------------+
|  gps.py   | --->|    main.py     |----->|  logger.py   |
+-----------+     +----------------+      +--------------+
        ▲                  │                     │
        │                  ▼                     ▼
+-----------+       +-------------+      gps_log.csv
|  rtc.py   |       | Console UI  |
+-----------+       +-------------+
```

---

# Features

- Simulation Mode for development
- Hardware Mode (planned)
- GPS coordinate logging
- Timestamp recording
- CSV file storage
- Configurable settings
- Modular architecture
- Clean code following PEP 8

---

# Technologies

| Category | Technology |
|-----------|------------|
| Language | Python 3 |
| Hardware | Raspberry Pi Zero 2 W |
| GPS | NEO-6M (Planned) |
| RTC | DS3231 (Planned) |
| Storage | CSV |
| Development | VS Code |
| Version Control | Git & GitHub |

---

# Project Structure

```text
GPS-Logger/
│
├── images/
│
├── sample_data/
│   └── gps_log.csv
│
├── src/
│   ├── config.py
│   ├── gps.py
│   ├── rtc.py
│   ├── logger.py
│   └── main.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

# Module Description

| File | Responsibility |
|------|----------------|
| `main.py` | Coordinates the application workflow |
| `config.py` | Stores project configuration |
| `gps.py` | Provides GPS coordinates |
| `rtc.py` | Provides current date and time |
| `logger.py` | Saves data into CSV |

---

# Installation

Clone the repository.

```bash
git clone https://github.com/phanuwatarmart/GPS-Logger.git
```

Move into the project.

```bash
cd GPS-Logger
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Usage

```bash
cd src
python main.py
```

---

# Console Output

```text
==================================================
GPS Logger Started
==================================================

Time      : 2026-07-08 21:34:38
Latitude  : 13.755868
Longitude : 100.502077
--------------------------------------------------

Time      : 2026-07-08 21:34:43
Latitude  : 13.756647
Longitude : 100.502005
--------------------------------------------------
```

---

# CSV Output

```csv
Timestamp,Latitude,Longitude
2026-07-08 21:34:38,13.755868,100.502077
2026-07-08 21:34:43,13.756647,100.502005
```

---

# Configuration

Example configuration in `config.py`

```python
SIMULATION_MODE = True

LOG_INTERVAL = 5

SIMULATED_LATITUDE = 13.7563
SIMULATED_LONGITUDE = 100.5018

GPS_OFFSET = 0.01
```

---

# Future Improvements

- Connect to GPS NEO-6M
- Connect to RTC DS3231
- SQLite database support
- Unit testing
- Docker support
- Web dashboard
- GPX export
- REST API integration

---

# What I Learned

This project helped me practice:

- Python Modules
- Software Design
- Configuration Management
- CSV File Handling
- Clean Code
- PEP 8
- Refactoring
- Code Review
- Software Testing
- Git & GitHub Workflow

---

# License

This project is licensed under the MIT License.