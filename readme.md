# TRON CLI - Python

My attempt to make a command line interface helper inspired by the movie Tron.
In the movie Flynn as a command line AI called Tron. I thought it would be cool to name my utility the same. Although not an ai... yet, it has the potential to be the starting point of all my automation of boring stuff.

So far it doesn't do much aside from copying files in two different ways.

Going forward I would like to add job search helpers and task helpers to update excel files and documents that I use daily.


# USAGE
### Duplicate File
```
tron file -d 'myFolder/myFile.txt'
```
creates ```myfile_000.txt```

### Backup File
```
tron file -d 'myFolder/myFile.txt'
```
creates ```myFile_backup.txt```

# Installation
```
git clone http://github.com/patomation/indeed-scraper ~/.tron
```

```
echo 'alias indeed="python ~/.tron/"' >> ~/.bashrc
```

## Getting Started
Install all the dependencies in requirements.txt
```
pip install -r requirements.txt
```

## Development
Install virtual environment
```
$ python3 -m pip install --user virtualenv
```
Create New Environment:
```
$ python3 -m venv env
python 2:
$ python -m virtualenv env
```
Activate environment
```
source env/bin/activate
```
Deactivate Environment
```
deactivate
```
Install dependencies:
```
pip install -r requirements.txt
```
Save dependencies:
```
pip freeze > requirements.txt
```

[More About this](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

## Going Forward
