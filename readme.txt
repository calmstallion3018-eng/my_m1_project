・ローカルターミナルでやること
git add .
git commit -m "適当なコメント"
git push origin main

・PythonAnywhereでやること
(Bash)
cd ~/my_m1_project
git pull origin main

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --noinput

(Web)
Reload Shigre0912.pythonanywhere.com