from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Meditation(BaseModel):
    description: str
    duration: str
    instructions: str

class MeditationData(BaseModel):
    name: str
    meditation: Meditation

# Load your CSV data into a dictionary
meditation_data = {}
with open("meditation_techniques.csv") as file:
    # Assuming the first row has headers (Name, Description, Duration, Instructions)
    headers = next(file).strip().split(",")
    for line in file:
        data = dict(zip(headers, line.strip().split(",")))
        meditation_data[data["Name"]] = Meditation(
            description=data["Description"],
            duration=data["Duration"],
            instructions=data["Instructions"],
        )

@app.get("/names")
async def get_all_names():
    return list(meditation_data.keys())

@app.get("/meditation/{name}")
async def get_meditation_details(name: str):
    meditation = meditation_data.get(name)
    if meditation is None:
        return {"error": f"Meditation with name '{name}' not found"}
    return meditation


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
