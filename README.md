# data-hackfest

This application is hosted in render.com. But if due to render.com's free tier you do not see the data in the frontend follow the below steps  to run the backend server before running the frontend.

### Steps to run the app on local

cd to DATA-HACKFEST folder.

Create a virtual environment:
python -m venv < venv- name >

Run the virtual environment:
./< venv- name >/Scripts/activate

Install the requirements:
pip install -r requirements.txt

Run the app:
uvicorn main:app --reload
