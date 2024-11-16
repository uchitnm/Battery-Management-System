
# Battery Analysis and Management System

## Overview
The **Battery Analysis and Management System** is a software application designed to help household users manage various types of batteries, monitor their performance, and ensure responsible disposal. The system provides data-driven recommendations for battery purchases, tracks usage patterns, and generates performance reports to optimize battery usage and promote sustainability.

---

## Features
- **Battery Inventory Management**: Add, edit, and delete battery records with details like type, manufacturer, purchase date, price, and use case.
- **Usage Tracking**: Monitor battery lifespan and usage events to calculate remaining life expectancy.
- **Performance Analytics**: Generate graphical and tabular reports to compare battery performance across manufacturers.
- **Recommendation System**: Suggest suitable and economical batteries based on user requirements.
- **Responsible Disposal Guidance**: Offer best practices for environmentally safe disposal of used batteries.
- **Data Export**: Export reports in CSV format for easy sharing and offline analysis.

---

## Technologies Used
- **Database**: MySQL
- **Programming Language**: Python
- **GUI Framework**: Tkinter
- **Connector**: `mysql-connector` for database access

---

## System Requirements
- **Hardware**: 
  - Minimum 8GB RAM and 64GB storage
  - x86 or ARM processor
- **Software**:
  - Python 3.x
  - MySQL v7.0 or higher
  - Supported operating systems: Windows, macOS

---

## How to Run
1. Clone the Repository - ```bash git clone <repository-url>```
2. Run batmng.sql file to create Database.
3. Run populate.sql to populate the Database.
4. data_management.py is a python user defined module for datamanagement.
5. Run the UI_main.py - ``` python3 UI_main.py ``` - On macOS
                      - ``` python UI_main.py ``` - Windows
