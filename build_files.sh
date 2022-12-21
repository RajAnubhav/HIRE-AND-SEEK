echo "BUILD START"
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
python3 -m virtualenv env
source env/bin/activate

python3 -m pip install https://dev.mysql.com/doc/refman/8.0/en/macos-installation-pkg.html

python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
echo "BUILD END"