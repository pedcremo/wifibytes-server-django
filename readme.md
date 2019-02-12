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
    mkdir .virtualenvs 
    NEW python3 -m venv .virtualenvs/wifibytes

2.- Activate virtualenv
    NEW source .virtualenvs/wifibytes/bin/activate
    

3.- Clone the repo in home
    git clone https://github.com/pedcremo/wifibytes-server-django.git
   
4.- Enter to Django project directory
    cd wifibytes-server-django

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
    python manage.py migrate --settings=wifibytes.settings.local

7.- Create super user
    python manage.py createsuperuser --settings=wifibytes.settings.local

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

## nginx conf file and notes for production deployment ##
Be sure this nginx directive is setted
proxy_set_header X-Real-IP $remote_addr;


Add this file to /etc/nginx/sites-available:

upstream wifibytes_django {
    server unix:///home/wifibyres/wifibytes.sock; 
}
server {
    listen 80;
    server_name DOMINIO_DEL_PROYECTO.com ; client_max_body_size 0;
    charset utf-8;

    location /media {
        alias /home/wifibytes/wifibytes-project/wifibytes/media; 
    }
    location /static {
        alias /home/wifibytes/wifibytes-project/wifibytes/assets;   
    }
    location / {
        uwsgi_pass wifibytes_django;
        uwsgi_param QUERY_STRING $query_string; uwsgi_param REQUEST_METHOD $request_method; uwsgi_param CONTENT_TYPE $content_type; uwsgi_param CONTENT_LENGTH $content_length; uwsgi_param REQUEST_URI $request_uri; uwsgi_param PATH_INFO $document_uri; uwsgi_param DOCUMENT_ROOT $document_root; uwsgi_param SERVER_PROTOCOL $server_protocol; uwsgi_param REMOTE_ADDR $remote_addr; uwsgi_param REMOTE_PORT $remote_port; uwsgi_param SERVER_ADDR $server_addr; uwsgi_param SERVER_PORT $server_port; uwsgi_param SERVER_NAME $server_name; uwsgi_param UWSGI_SCHEME http;
    }   
}

 `cd/etc/nginx/sites-available`
 `touch wifibytes && nano -c wifibytes`

 Create symbolic link 
 `ln -s /etc/nginx/sites-available/wifibytes /etc/nginx/sites-enabled/wifibytes`
 Reset nginxx
`/etc/init.d/nginx restart`
