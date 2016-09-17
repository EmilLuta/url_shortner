# url_shortner

A basic application that will provide a simple way to shorten urls on request

### Getting your hands dirty ###

* cd to a comfy location
* git clone git@github.com:EmilLuta/url_shortner.git
* cd url_shortner/
* virtualenv -p $(which python3) venv
* source venv/bin/activate
* pip install -r requirements.txt
* cp config_example.py config.py
* update the config.py file to suit your needs
* ./manage.py create_database
* ./manage.py runserver
* point your browser to [http://localhost:5000/](http://localhost:5000/)
