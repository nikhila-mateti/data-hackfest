from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

allowed_origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,  # Optional, allows cookies for authenticated requests
    allow_methods=["*"],  # Optional, allows all HTTP methods
    allow_headers=["*"],  # Optional, allows all headers
)

class Meditation(BaseModel):
    description: str
    duration: str
    instructions: str

class MeditationData(BaseModel):
    name: str
    meditation: Meditation

# Load your CSV data into a dictionary
meditation_data = {}

with open("meditation_techniques.csv", newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        meditation_data[row["Name"]] = {
            "description": row["Description"],
            "duration": row["Duration"],
            "instructions": row["Instructions"]
        }

@app.get("/names")
async def get_all_names():
    return list(meditation_data.keys())

@app.get("/meditation/{name}")
async def get_meditation_details(name: str):
    meditation = meditation_data.get(name)
    if meditation is None:
        return {"error": f"Meditation with name '{name}' not found"}

    print(meditation)
    return meditation
