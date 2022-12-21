echo "BUILD START"
python3.10 -m pip install --upgrade pip
python3.10 -m pip install virtualenv
python3.10 -m virtualenv env
source env/bin/activate

python3.10 -m pip install -r requirements.txt
python3.10 manage.py collectstatic --noinput --clear
echo "BUILD END"