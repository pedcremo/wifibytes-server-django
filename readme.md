============================         
                                                                                                      
 Wifibytes Project

============================

PREREQUISITES

sudo apt-get install libncurses5-dev
sudo apt-get install libevent-dev python-all-dev (In order to avoid reportLab problems)

We are gone to use python3  and django 2.1.5
With tool 2to3 I've ported entire wifibytes django folder from python2 to python3 `2to3 -w -n .`

How to run the project:

1.- Create virtualenv (In your home) (Don't change folder name afterwards or the virtualenv will fail )
    OLD virtualenv Wifibytes
    NEW python3 -m venv env

2.- Activate virtualenv
    NEW source env/bin/activate
    

3.- Clone the repo into virtualenv
    
    git clone https://USUARIO@bitbucket.org/cactusagency/wifibytes-project.git

4.- Enter to Django project directory
    cd Wifibytes-project

5.- Install all requirements (upgrade pip if needed `pip install --upgrade pip`)
    pip install -r requirements.txt

5.5.- Install postgres BD
    
    (ubuntu 16.04)
    sudo apt-get install -y postgresql-9.5 postgresql-contrib-9.5 
    sudo apt-get install -y postgresql-doc-9.5 postgresql-server-dev-9.5
    
    (ubuntu 14.04)
    sudo apt-get install -y postgresql-9.3 postgresql-contrib-9.3
    sudo apt-get install -y postgresql-doc-9.3 postgresql-server-dev-9.3

6.- Migrate BBDD (Not until postgres installed. Get into folder wifibytes where manage.py is installed) READ PROBLEM with reportLab
    python3 manage.py migrate --settings=wifibytes.settings.local

7.- Create super user
    python3 manage.py createsuperuser --settings=wifibytes.settings.local

8.- Run server
    python manage.py runserver --settings=wifibytes.settings.local

NOTE: Important to run in production environments:
`python manage.py collectstatic  --settings=wifibytes.settings.production`
to generate assets folder with all css, js libraries and other stuff necessary to serve statically

Check http://localhost:8000


Do a copy/backup from database (inside virtualenv)

 python manage.py dumpdata --exclude auth.permission --exclude contenttypes --settings=wifibytes.settings.[WHATEVER] > [NAME].json


Restore backup 

 python manage.py loaddata --settings=wifibytes.settings.[WHATEVER]  [NAME].json

We should copy media/ folder too from wifibytes in order to keep uploaded images and documents


For deployment install uwsgi on python3 venv 
Dependencies python3-dev package
Maybe we should uncomment on requirements.txt uwsgi installation

##### System Dependences
sudo apt-get install libncurses5-dev

### Compression dependencies

On Ubuntu 16.10
For pipeline, we need to isntall "yuglify".
sudo apt-get install npm
sudo npm -g install yuglify
ln -s /usr/bin/nodejs /usr/bin/node 

## Visual studio code integration ##

Install python extension and configure python.pythonPath":"~/env/bin/python3"
File -> Preferences -> Settings