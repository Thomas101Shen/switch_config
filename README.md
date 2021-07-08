**Requirements for this program to work:**
Cisco switch has ssh enabled for at least one user

# Step 1: Download Dependencies
In the root directory run the following line:
	`pip install -r setup.py`

# Step 2: Checking Syntax of Excel Sheet
	**Everything other than the name Column should either be numbers or all lowercase
	For specifying allowed trunking seperate each Vlan no. with a ', '
> Notes: everything must be in lowercase except for interface name

# Step 3: Move Excel Sheet Into config_files
Move excel sheet to the config_files in the root directory that main.py is running in
	ex:
		go into PowerShell and run the command:
			`mv ${file path which can be found in the finder bar/right clicking on the file} ./config_files`
			(assuming you are in the same dir as main.py)
>**ProTip:** if there are spaces anywhere put \` before them

>**ProTip:** go into the interface python files and edit the dictionary possible_values to exclude anything you don't want

# Step 4: Configure device
open device.py and enter the information into the dictionary accordingly

# Step 5: Run the Program
In your CLI run the command: python main.py