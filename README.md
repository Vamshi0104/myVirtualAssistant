# myVirtualAssistant
Simple Virtual Assistant using Python

INTRODUCTION:

Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and explanatory text. 
Uses include: data cleaning and transformation, numerical simulation, statistical modeling, machine learning and much more .
So I prefer this  Notebook whenever coding is with Python,since there are many functionalities like easily modules can be imported,
User-Friendly Environment is craeted for coding,(Ctrl+Enter) to run the cell(current code).

Packages that are included in order to create Simple Virtual-Assistant are:

1.	gTTS (For Text to Speech functionalities by Google)
2.	datetime (For displaying date,time)
3.	calendar (For displaying calendar )
4.	playsound (Supporting package for gTTS to play sound )
5.	numpy (Dealing with Arrays and Random functions )
6.	selenium(To enable web-browser functionality)
7.	wikipedia(Resource for the information required by User)

So in order to Install these packages Type and Run Simple code:

	import sys

	!{sys.executable} -m pip install <package_name>
	
				OR
https://anaconda.org/anaconda  [Visit site a run the package Commend in Anaconda Prompt] or Miniconda can also be installed (Less usage of RAM, fewer Packages when compared to Anaconda).

[ Note:-Make sure that all the above packages are installed before proceeding to run or code. ]

Step1:

Create a module in Main file (Virtual_Assitant.py).The coding part only goes with user input and corresponding conditional statements(if, elif, else) to get the data by calling the module in the file 

Step2:

Now it’s time to create additional, supporting which made and responsible for creating a Virtual Assistant.
The supporting python files like DateTime_VA.py actually the extension changes if your working with Jupyter Notebook wherein extensions is (.ipynb) .

Actually it is quite easy to import a another file in existing  file with one line code that is let’s consider importing DateTime_VA python file in Main File Virtual_Assitant.ipynb  
				
				%run Datetime_VA.ipynb  (Works in JupyterNotebook)
 
 While viewing the code you can find this Statement( get_ipython().run_line_magic('run', 'entry_VA.ipynb')),since it is executed in Jupyter notebook extension is (.ipynb) but the files attached to Master Branch are (.py) So,Just replace with statement(%run Datetime_VA.ipynb) if you are running in Jupyter Notebook.
				
File Handling fuctions like open, read, write  are used for Quotes, Song modules as they take content from corresponding .txt files which are already attached to the master branch in my repository 

Step3:

Before running Weather_VA.ipynb in your notebook, web driver from selenium package must be installed and executable path is mandatory.So,Download the chromedriver.exe file for Google Chrome,place .exe file in LocalDisk in any folder and Copy address,paste value as text to executable_path.

To Know about your ChromeDriver:
You will Find 3 dots to right of your chrome->Help>>About Google Chrome
Find appropriate version of your Chrome And Download file from below link: 
			https://sites.google.com/a/chromium.org/chromedriver/downloads

	For Example:
			driver=webdriver.Chrome(executable_path='C:\Python\chromedriver.exe')



Step4:

Make sure that Jupyter Notebook and Python  that you have installed are lastest release version in order to run as Currently  I am using Python 3.7
For more info in Downloading Visit:
			https://anaconda.org 


--->Finally,Run Virtual_Assistant.py file(Attached to Master Branch) to execute.

Make sure that you follow above Simple 4 Steps to Run or Add or Remove Functionalities from your Virtual-Assistant 

				   			Happy Coding....:)
