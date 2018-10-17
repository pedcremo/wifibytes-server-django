============================         

                                                                                                             
 Wifibytes Project


============================

PREREQUISITES

sudo apt-get install libncurses5-dev
sudo apt-get install libevent-dev python-all-dev (In order to avoid reportLab problems)

How to run the project:

1.- Create virtualenv (In your home)
    virtualenv Wifibytes

2.- Activate virtualenv
    source Wifibytes/bin/activate

3.- Clone the repo into virtualenv
    cd Wifibytes
    git clone https://USUARIO@bitbucket.org/cactusagency/wifibytes-project.git

4.- Enter to Django project directory
    cd Wifibytes-project

5.- Install all requirements
    pip install -r requirements.txt

5.5.- Install postgres BD
(ubuntu 16.04)
sudo apt-get install -y postgresql-9.5 postgresql-contrib-9.5 
sudo apt-get install -y postgresql-doc-9.5 postgresql-server-dev-9.5
(ubuntu 14.04)
sudo apt-get install -y postgresql-9.3 postgresql-contrib-9.3
sudo apt-get install -y postgresql-doc-9.3 postgresql-server-dev-9.3

6.- Migrate BBDD (Not until postgres installed. Get into folder wifibytes where manage.py is installed) READ PROBLEM with reportLab
    python manage.py migrate --settings=wifibytes.settings.local

7.- Create super user
    python manage.py createsuperuser --settings=wifibytes.settings.local

8.- Run server
    python manage.py runserver --settings=wifibytes.settings.local


Check http://localhost:8000


###### PDF
"Reportlab Version 2.1+ is needed!" --import error for resolve this problem, go to your_virtualenv/local/lib/python2.7/site-packages/sx/pisa3/ edit pisa_util.py Just replace this code segment : if not (reportlab.Version[0] == "2" and reportlab.Version[2] >= "1"): raise ImportError("Reportlab Version 2.1+ is needed!") REPORTLAB22 = (reportlab.Version[0] == "2" and reportlab.Version[2] >= "2") with the following: if not (reportlab.Version[:3]>="2.1"): raise ImportError("Reportlab Version 2.1+ is needed!") REPORTLAB22 = (reportlab.Version[:3]>="2.1")

##### To Fix this error in Reporlab:
locate util.py in your virtualenv site-packages
replace this:


```
#!python

if not (reportlab.Version[0] == "2" and reportlab.Version[2] >= "1"):
    raise ImportError("Reportlab Version 2.1+ is needed!")

REPORTLAB22 = (reportlab.Version[0] == "2" and reportlab.Version[2] >= "2")

```

to:

```
#!python

if not (reportlab.Version[:3] >="2.1"):
    raise ImportError("Reportlab Version 2.1+ is needed!")

REPORTLAB22 = (reportlab.Version[:3] >="2.1")
```


https://stackoverflow.com/questions/22075485/xhtml2pdf-importerror-django/38674059#38674059


##### System Dependences
sudo apt-get install libncurses5-dev

### Compression dependencies

On Ubuntu 16.10
For pipeline, we need to isntall "yuglify".
sudo apt-get install npm
sudo npm -g install yuglify
ln -s /usr/bin/nodejs /usr/bin/node 

