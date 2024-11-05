mkdir $1 

cd $1

touch app.py

mkdir .venv

mkdir static

mkdir templates

cd static

mkdir css

mkdir images

pipenv install flask

pipenv shell
# 
#(activar nuevamente)  source venv/bin/activate
