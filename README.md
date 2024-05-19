# data-hackfest

This application is hosted in render.com.

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