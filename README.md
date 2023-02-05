# SlugEats <img src="https://media.giphy.com/media/g5FB33d3GVUkg/giphy.gif" width="50" height="37"> 

SlugEats is a GUI application built using the Kivy framework for Python and pandas. The app provides information about open dining halls, their hours of operation, and food being served along with the nutrition facts. It also allows users to calculate their daily calorie intake based on their height and weight, and keeps track of their Slug Points balance. The goal of the project is to help the community on the university campus to live healthier lives by being mindful of their food choices and spending. The team hopes to improve the appearance of the app and incorporate matplotlib to graph daily nutrients, with a future goal of turning it into an app for iOS and Android.
# Getting Started
To get started with SlugEats, you will need to have the following software installed:
You can use pip to install the dependencies.
- Python 3
- Kivy framework for Python
- pandas library
Once you have the required software installed, follow these steps:

1. Clone the repository: To get started with the project, you will need to clone the repository from GitHub onto your local machine. <repository URL>
2. Navigate to the cloned repository directory
3. Run the following command to start the app: python SlugEats.py
4. The SlugEats GUI should now be up and running
The following files are included in the repository:

- `SlugEats.py` - This is the main script that runs the application
- `SlugEats.kv` - This is the Kivy file for the GUI design
- `journal.py` - This script manages the daily journal feature
- `slug_point_calculator.py` - This script calculates the daily slug point balance
- `nutrition_facts.csv` - This file contains the nutrition information for food served at dining halls
- `indexed_hours.csv` - This file contains the hours of operation for each dining hall
- `yellow.png and blue.png` - These files are images used in the GUI
- Please note that the application uses information in the `nutrition_facts.csv` and `indexed_hours.csv` files to provide information about dining halls and the food being served.
