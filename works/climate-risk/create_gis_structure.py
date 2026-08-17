import os
from pathlib import Path

# Get the desktop path for the current user
desktop = Path.home() / "Desktop"
working_directory = desktop / "GIS"

# Base folders
input_data = working_directory / "Input Data"
results_folders = [
    "Laboratory_Results_RCP45",
    "Laboratory_Results_RCP85",
    "Project_Results_RCP45",
    "Project_Results_RCP85"
]
categories = ["Climate", "Precipitation", "Temperature", "Trends"]

# Substructure for Precipitation
precipitation_structure = {
    "Annual": ["Dyness", "MIN", "SUM"],
    "Monthly": [],
    "Seasonal": {
        "Summer": ["MAX", "MIN", "SUM"],
        "Winter": ["MAX", "MIN", "SUM"]
    }
}

# Substructure for Temperature
temperature_structure = {
    "Annual": ["MAX", "MEAN", "MIN"],
    "Monthly": []
}

# Create working directory and Input Data folder
os.makedirs(input_data, exist_ok=True)

# Create results folders and nested structure
for result_folder in results_folders:
    base_path = working_directory / result_folder
    for category in categories:
        category_path = base_path / category
        os.makedirs(category_path, exist_ok=True)

        if category == "Precipitation":
            for subfolder, contents in precipitation_structure.items():
                subfolder_path = category_path / subfolder
                os.makedirs(subfolder_path, exist_ok=True)
                if isinstance(contents, list):
                    for item in contents:
                        os.makedirs(subfolder_path / item, exist_ok=True)
                elif isinstance(contents, dict):
                    for season, metrics in contents.items():
                        season_path = subfolder_path / season
                        for metric in metrics:
                            os.makedirs(season_path / metric, exist_ok=True)

        elif category == "Temperature":
            for subfolder, contents in temperature_structure.items():
                subfolder_path = category_path / subfolder
                os.makedirs(subfolder_path, exist_ok=True)
                for item in contents:
                    os.makedirs(subfolder_path / item, exist_ok=True)

print("GIS folder structure created on Desktop!")