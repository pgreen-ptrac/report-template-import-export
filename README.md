# report-template-import-export
Currently Plextrac doesn't have the ability to import or export Report Templates. This script adds that functionality by saving the payload of a GET request to a json file. This json file can be passed around and send as the payload of a CREATE request to import the Report Template back into the platform or into another instance of Plextrac.

The main using of importing Report Templates is during new customer onboarding when the Professional Services team has been tasked with creating a Jinja Export Template. This Jinja template will pull info from specific fields in a Plextrac report and the Report Template helps automatically setup those fields instead of manual creation for each new report. Without the import/export functionality a new customer will have to create the Report Template in their instance. With the functionality, they can save time by importing a Report Template provided by the Professional Services team.

# Requirements
- [Python 3+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [pipenv](https://pipenv.pypa.io/en/latest/install/)

# Installing
After installing Python, pip, and pipenv, run the following commands to setup the Python virtual environment.
```bash
git clone this_repo
cd path/to/cloned/repo
pipenv install
```

# Setup
After setting up the Python environment, you will need to setup a few things before you can run the script.

## Credentials
In the `config.yaml` file you should add the full URL to your instance of Plextrac.

The config also can store your username and password. Plextrac authentication lasts for 15 mins before requiring you to re-authenticate. The script is set up to do this automatically. If these 3 values are set in the config, and MFA is not enable for the user, the script will take those values and authenticate automatically, both initially and every 15 mins. If any value is not saved in the config, you will be prompted when the script is run and during re-authentication.

Script estimated run time: ~<1 minute

# Usage
After setting everything up you can run the script with the following command. You should be in the folder where you cloned the repo when running the following.
```bash
pipenv run python main.py
```
You can also add values to the `config.yaml` file to simplify providing the script with the data needed to run. Values not in the config will be prompted for when the script is run.

## Required Information
The following values can either be added to the `config.yaml` file or entered when prompted for when the script is run.
- PlexTrac Top Level Domain e.g. https://yourapp.plextrac.com
- Username
- Password
- MFA Token (if enabled)

## Script Execution Flow
- Prompts user for Plextrac instance URL
  - Validate URL points to a running instance of Plextrac
- Prompts user for username, password, and mfa (if applicable)
- Calls authenticate endpoints and stores Authorization headers for future use
- Prompts user to choose to import or export a report template
- Guides user to select a report template to export, or a json file to import
