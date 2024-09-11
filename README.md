## Resume Parser 
First make a virtual env  
```
virtualenv env
```
Activate this env 
```
source env/bin/activate
```
Download required packages 
```
pip install -r requirements.txt
```
Now migrate  
```
python manage.py makemigrations
python manage.py migrate
```
Run server
```
python manage.py runserver
```
## Upload resume 
url -> http://localhost:8000/api/extract_resume  
In postman go to form_data and upload file with resume as key.
