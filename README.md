# Api
## Setup Api:
  - `pip install -r requirements.txt`
  - `python manage.py runserver`
  
## Api Register User URLs:
  - Register user
  -   Json Format:
```
{
    "username": "huzefa",
    "password": "123"
    }
```
   

    - localhost:8000/api/register/
    
  - Login  user
    - localhost:8000/api/login/
    
  - Logout user
    - localhost:8000/api/logout/
    
## Api Profile URLs:
  - GET POST Delete Profile detail
    - localhost:8000/api/profile

  - GET PUT Delete Specific Profile detail
     - localhost:8000/api/profile/1
   
    
