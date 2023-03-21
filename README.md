# KED

## Setup

Open the folder with all the repo files

Optional: install virtual environment and run it
+ Create a virtual environment and access it

		python3 -m venv venv
	
+ on linux:

		source venv/bin/activate
	
+ on windows

		.\venv\Scripts\activate
		
Install the needed packages: 
	
	pip install -r requirements.txt

Run main.py

	python main.py

## Workflow for this repo:
### Gitflow Workflow

+ __main__ conteains the releases files.

+ __Development__ it's the most advanced working copy (it contains all the completed Features merged toghether)

+ __Features__ are all improvements and modifications. All work in progress has to have a Feature branch open (may be unstable)

![image](https://user-images.githubusercontent.com/63608106/219937289-373d2e42-f940-4bab-8431-489e1639b80d.png)

More details about this workflow on [Atlassian Git Tutorials Page](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)

# Kivy Encryption Decryption Application

The main purpose of KEDA project is to offer a simple interface for safe and local text encryption. 

The inputs of the app can be either the plaintext or the cyphertext given by the user alongside a password. 
The output of the application is the cyphertext in case of encryption and the plaintext in case of decryption if all data is correctly added. 

This application uses Python 3.8 with packages from Kivy, pycryptodome and hashlib. 
Kivy is used for the GUI, pycryptodome and hashlib are used for the encryption algorithm.

For encryption this project uses the AES256 algorithm. 

