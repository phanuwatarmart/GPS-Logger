# GPS Logger

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-success)
![Status](https://img.shields.io/badge/Status-Simulation%20Tested-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A modular GPS logging system developed with Python, designed for Raspberry Pi Zero 2 W.

The application records GPS coordinates along with timestamps and stores the data in CSV format. It includes a **Simulation Mode** for development and testing, allowing the system to run without physical GPS hardware.

---

## Demo

The application runs in Simulation Mode, generating simulated GPS coordinates and timestamps at a configurable interval and saving the data to a CSV file.

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
The project is organized into modular components, separating configuration, GPS data generation, timestamp handling, and CSV logging.

Main Program (main.py) — Coordinates the application workflow.

GPS Module (gps.py) — Generates simulated GPS coordinates.

RTC Module (rtc.py) — Provides timestamps for each GPS log entry.

Logger Module (logger.py) — Stores GPS data and timestamps in CSV format.

Config Module (config.py) — Stores configurable settings, including logging intervals and simulation parameters.


## Features

- Modular Python architecture
- GPS coordinate simulation
- Timestamp recording
- CSV data logging
- Configurable logging interval
- Graceful shutdown using `Ctrl+C`
- Simulation Mode for testing without GPS hardware

---

## Technologies

- **Language:** Python
- **Development Environment:** Antigravity / Visual Studio Code
- **Version Control:** Git & GitHub
- **Target Hardware:** Raspberry Pi Zero 2 W
- **Data Storage:** CSV

---

## Project Structure

```text
GPS-Logger/
├── images/
├── sample_data/
│   └── gps_log.csv
├── src/
│   ├── config.py
│   ├── gps.py
│   ├── logger.py
│   ├── main.py
│   └── rtc.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

# Module Description

| File | Responsibility |
|------|----------------|
| `main.py` | Coordinates the application workflow |
| `config.py` | Stores project configuration |
| `gps.py` | Provides GPS coordinates |
| `rtc.py` | Provides current date and time |
| `logger.py` | Saves data into CSV |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/phanuwatarmart/GPS-Logger.git
```

Navigate to the project directory:

```bash
cd GPS-Logger
```

## Usage

Run the application:

```bash
python src/main.py
```

The application will start generating simulated GPS coordinates and timestamps, displaying them in the terminal and saving them to a CSV file in the `sample_data/` directory.

Press `Ctrl+C` to stop the application.

## Output Example

### Terminal Output

```text
GPS Logger Started
Timestamp: 2026-07-08 21:34:38
Latitude: 13.755868
Longitude: 100.502077

GPS Logger Started
Timestamp: 2026-07-08 21:34:43
Latitude: 13.756647
Longitude: 100.502005
```

### CSV Output

```csv
Timestamp,Latitude,Longitude
2026-07-08 21:34:38,13.755868,100.502077
2026-07-08 21:34:43,13.756647,100.502005
2026-07-08 21:34:48,13.756108,100.502215
```

## Configuration

The application settings can be modified in `src/config.py`.

| Parameter | Description |
|---|---|
| `LOG_INTERVAL` | Time interval between each GPS log entry (seconds) |
| `SIMULATED_LATITUDE` | Base latitude used for GPS simulation |
| `SIMULATED_LONGITUDE` | Base longitude used for GPS simulation |
| `GPS_OFFSET` | Offset range used to generate simulated GPS coordinates |

## Future Improvements

- Integrate a real GPS module (NEO-6M)
- Implement hardware-based GPS data reading
- Integrate RTC module (DS3231)
- Deploy the system on Raspberry Pi Zero 2 W
- Improve error handling and logging reliability

## What I Learned

- Modular Python application design
- Working with Python modules and imports
- Generating and handling simulated GPS data
- Recording timestamps and writing CSV files
- Using Git and GitHub for version control
- Testing and debugging a Python application
- Organizing a project for future hardware integration

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.