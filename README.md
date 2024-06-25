# AIO2024 - Project Module 1: Streamlit

Use [Streamlit](https://streamlit.io/) library to develop some basic applications:
- Word Correction
- Object Detection
- Chatbot

## Installation
### 1. Clone the repository
```commandline
git clone https://github.com/lebaotuann/AIO2024-Streamlit-Project.git aio2024_streamlit_project
cd aio2024_streamlit_project
```

### 2. (Optional) Create and activate a python virtual environment
- For Ubuntu:
```commandline
sudo apt-get install python3.9-venv
python3 -m venv myvenv
source myvenv/bin/activate
```
- For Windows:
```commandline
py -m venv myvenv
myvenv\Scripts\activate
```
or
```commandline
python -m venv myvenv
myvenv\Scripts\activate
```

### 3. Install the required dependencies

```commandline
pip install -r requirements.txt
```

## Run the Application
You can start the application by the following command :
```shell
streamlit run <program_file_by_py>
```

- Word Correction
```commandline
streamlit run levelshtein_distance.py
```
- Object Detection
```commandline
streamlit run object_detection.py
```
- Chatbot
```commandline
streamlit run chatbot.py
```

## References
You can refer to how to a python virtual environment.
- [Windows](https://medium.com/@rodolfo.antonio.sep/setting-up-a-python-virtual-environment-on-windows-september-2023-aa9a25f856f9)
- [Ubuntu](https://medium.com/@rodolfo.antonio.sep/setting-up-a-python-virtual-environment-on-windows-september-2023-aa9a25f856f9)
