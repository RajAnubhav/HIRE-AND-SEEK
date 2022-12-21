echo "BUILD START"
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
python3 -m virtualenv env
source env/bin/activate

python3 -m pip install mysql-client

python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "BUILD END"