# Api
## Setup Api:
  - `pip install -r requirements.txt`
  - `python manage.py runserver`
  
## Api Register User URLs:
  - Register user
```
{
    "username": "",
    "email": "",
    "password": ""
    }
```
    localhost:8000/api/register/
    
  - Login  user
```
{
    "username": "",
    "password": ""
    }
```
    localhost:8000/api/login/
    
  - Logout user
    - localhost:8000/api/logout/
    
## Api Profile URLs:
 - GET POST Delete Profile detail
  - Post Profile
  ```
  { "user": "", "email": "", "location": "", "state": "", "gender": ""}
  ```
    - localhost:8000/api/profile
  use postman to post data
  Download Link: https://www.postman.com/downloads/
  
  -GET Profile 
  ```
  - localhost:8000/api/profile
   ```
    
  -Delete Profile:
  ```
  -localhost:8000/api/profile
   ```
   use postman to delete data

  - GET PUT Delete Specific Profile detail
     - localhost:8000/api/profile/1
   
    
