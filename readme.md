============================         

                                                                                                             
 Wifibytes Project


============================

How to run the project:

1.- Create virtualenv
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

6.- Migrate BBDD
    python manage.py migrate --settings=Wifibytes.settings.local

7.- Create super user
    python manage.py createsuperuser --settings=Wifibytes.settings.local

8.- Run server
    python manage.py runserver --settings=Wifibytes.settings.local


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

