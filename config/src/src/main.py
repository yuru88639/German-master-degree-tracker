import pandas as pd

from src.scraper import fetch_page
from src.parser import parse_program

# Load program list
programs = pd.read_csv("config/programs.csv")

records = []

# Loop through each program
for _, row in programs.iterrows():

    url = row["url"]

    html = fetch_page(url)

    if html:

        info = parse_program(html)

        records.append({
            "University": row["university"],
            "Program": row["program"],
            "Region": row["region"],
            "Deadline": info["deadline"],
            "Tuition": info["tuition"],
            "GPA": info["gpa"],
            "Language": info["language"],
            "Exchange": info["exchange"],
            "URL": url
        })

# Convert to table
df = pd.DataFrame(records)

# Save Excel
df.to_excel("programs.xlsx", index=False)

print("Data collection complete")
