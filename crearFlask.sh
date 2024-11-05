#!/bin/bash

if [[ $# > 0 ]] ; then

    nombreProject=$1;

    echo “creando projecto: $nombreProject“ 

    mkdir "$nombreProject" ;
    cd "$nombreProject" 
    pwd
    echo -e "carpeta creada \n"


    echo -e "from flask import Flask\n" >> app.py
    echo -e "app = Flask(__name__) \n" >> app.py

    echo -e "@app.route('/')" >> app.py
    echo -e "def index():" >> app.py
    echo -e '    return "Hola mundo"\n' >> app.py

    echo -e 'if __name__ == "__main__":' >> app.py
    echo -e "    app.run(debug=True)\n" >> app.py

    echo -e "archivo app.py creado"

    #mkdir .venv
    virtualenv venv
    echo -e "######  ENTORNO VIRTUAL CREADO #####################3"
    # echo -e "######  Activate  #####################"
    # source venv/bin/activate
    # echo -e "######  Activate  #####################"
    # echo -e "######  instalando flask  #####################"
    # pip install Flask
    # pip install requests
    # deactivate
else
    echo "olvidaste ingresar el nombre del directorio" 

fi



#pipenv install flask



#code .
#pipenv shell

# desactivate
