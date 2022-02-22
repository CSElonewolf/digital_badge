
# Digital Badge 

A badge is a digital piece of evidence with which a student demonstrates that they have mastered certain skills or knowledge. Badges are a great instrument to make acquired knowledge and skills visible and 'portable'.


## Technology Used

1. Python 3.7 & Django for backend & SQLite for database 
2. Django REST Framework for REST API
3. Bootstrap 4 for Frontend 
4. Vanilla Js for scripts 



## Run Locally

Clone the project

```bash
  git clone https://github.com/CSElonewolf/digital_badge.git
```

Go to the project directory

```bash
  cd digital_badge
```

Create a Virtual Env

```bash
  python -m venv <env name>
```

Install the package inside the virtual env 

```bash
  pip install -r requirements.txt
```
Make Migrations 

```bash
  python manage.py makemigrations 
```

Migrate the changes  

```bash
  python manage.py migrate 
```

Create a Superuser  

```bash
  python manage.py createsuperuser
```

Run the project on localhost port 8000(default)

```bash
  python manage.py runserver 
```
## Where to find .png badge images 

```bash
  assests/
```

## Screenshots

![App Screenshot](https://github.com/CSElonewolf/digital_badge/blob/main/assests/readme_images/1.2.png)

![App Screenshot](https://github.com/CSElonewolf/digital_badge/blob/main/assests/readme_images/1.png)

![App Screenshot](https://github.com/CSElonewolf/digital_badge/blob/main/assests/readme_images/2.png)

![App Screenshot](https://github.com/CSElonewolf/digital_badge/blob/main/assests/readme_images/4.png)

![App Screenshot](https://github.com/CSElonewolf/digital_badge/blob/main/assests/readme_images/6.png)

![App Screenshot](https://github.com/CSElonewolf/digital_badge/blob/main/assests/readme_images/7.png)

![App Screenshot](https://github.com/CSElonewolf/digital_badge/blob/main/assests/readme_images/8.png)

## API Reference

#### Verify Badge 

```http
  GET /badge/verify
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**.  |
| `email` | `string` | **Required**. |

#### Example 
```http
  GET http:127.0.0.1/badge/verify?name=<badge_name>&email=<email_id>
```

<!-- ## Demo

Insert gif or link to demo -->

