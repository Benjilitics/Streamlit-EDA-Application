# eda-app

Benjamin Trinh
August 2022

This instruction is from *Chanin Nantasenamat* or *DataProfessor*. I added some personal notes while following his steps.

# Watch the tutorial video from Chanin

[How to build an EDA app using Pandas Profiling | Streamlit #19](https://youtu.be/p4uohebPuCg)

<a href="https://youtu.be/p4uohebPuCg"><img src="http://img.youtube.com/vi/p4uohebPuCg/0.jpg" alt="How to build an EDA app using Pandas Profiling | Streamlit #19" title="How to build an EDA app using Pandas Profiling | Streamlit #19" width="400" /></a>

# Demo

Launch the web app:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://benjilitics-streamlit-eda-application-app-3m55t6.streamlitapp.com/)

# Reproducing this web app
To recreate this web app on your own computer, do the following.

### Create conda environment
Firstly, we will create a conda environment called *eda*

In Windows, open Anaconda Prompt terminal

```
conda create -n eda python=3.9
```
Secondly, we will login to the *eda* environment
```
conda activate eda
```
### Install prerequisite libraries

Download requirements.txt file

Change to the project directory with command `cd <Project Directory>`

```
wget https://raw.githubusercontent.com/dataprofessor/eda-app/main/requirements.txt

```
If you see error, try this `conda install -c menpo wget`

Pip install libraries
```
pip install -r requirements.txt
```

###  Download and unzip contents from GitHub repo

Download and unzip contents from https://github.com/dataprofessor/eda-app/archive/main.zip

###  Launch the app

```
streamlit run app.py
```

You might encounter some errors below due to the upgrade/downgrade of dependencies. Try the solutions mentioned herewith then:

* If you see protocol buffers error. Try: `pip install --upgrade protobuf==3.20.0`
* If you see error: `AttributeError: module ‘click’ has no attribute ‘get_os_args’`. Try `pip install streamlit==1.8.1` # I already update this streamlit version in the requirements.txt 
* If you see error `ImportError: cannot import name 'escape' from 'jinja2'`. Try to downgrade jinja2 by `pip install jinja2==3.0.3`
* If you see error `ImportError: DLL load failed: The specified module could not be found`. Try to install `pip install pyqt5-tools`. Then copy 2 files `libcrypto-1_1-x64.dll` and `libssl-1_1-x64.dll` from anaconda3/library/bin into anaconda3/env/eda/DLLs
* If you see error `ModuleNotFoundError: No module named 'pyarrow.lib'` then install `pip install pyarrow`
* If you see error `ImportError: cannot import name '_imaging' from 'PIL' (C:\Users\benjamin.trinh\Anaconda3\envs\eda\lib\site-packages\PIL\__init__.py)` then try `pip uninstall PIL` and `pip uninstall Pillow` then `pip install Pillow`

HERE WE GO!