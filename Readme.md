[![Lint Code](https://github.com/SergeiNaum/Stakewolle/actions/workflows/linter_check.yml/badge.svg)](https://github.com/SergeiNaum/Stakewolle/actions/workflows/linter_check.yml)
# Test task for the company ip_godovich
# **rating** Api for working with comic book rating system. Created with DRF


## Quick start
  
#### Or you can deploy the project locally by following these instructions:

##### clonne project from repo

```
git clone https://github.com/SergeiNaum/ip_godovich.git
```
---

##### navigate to project_folder

```
cd ip_godovich
```
---

##### Start app execute the command
```
docker-compose up
```
---
##### CONGRATULATIONS THE CONTAINER IS UP AND RUNNING AND THE API IS READY FOR TESTING_🚀

---

##### Available methods for API requestsAvailable methods for API requests

Swagger ui documentation
```
http://127.0.0.1:8000/api/schema/swagger-ui/
```
---
Or use curl or Postman


API endpoint for returning average comic book rating
```
curl http://127.0.0.1:8000/api/comics/{int:pk}/rating/
```

---


API endpoint for creating a comic book rating {"comic": comic.id, "value": 1-5}
```
curl -X POST http://127.0.0.1:8000/api/ratings/ -d '{"comic": 3, "value": 5}' -H "Content-Type: application/json"
```

---

**To stop app, execute the command**

```
docker-compose down -v
```

---

markdown


Copy code
# Task Description

The task was to implement a rating system and display the rating for each comic. The rating should be based on the average score users can give comics from 1 to 5. The rating should be updated in real-time on any modern framework.

## Implemented Endpoints

### 1. Creating a Rating

- **Method**: `POST`
- **URL**: `/api/ratings/`
- **Parameters**:
 - `comic_id` - comic identifier
 - `user_id` - user identifier
 - `value` - rating from 1 to 5
- **Description**: When creating a rating, the comic's average rating is updated, and the rating is saved. To send a request, the user must be logged in. The service implements the basic authentication method.

### 2. Getting the Average Comic Rating

- **Method**: `GET`
- **URL**: `/api/comics/<comic_id>/rating/`
- **Description**: Returns the average rating of the comic. There are no user requirements for this endpoint. Manual Redis caching has also been added as a query optimization to the database.

## User Registration

User registration is provided by Django through the admin panel (you must first create a superuser) by running the command:

```bash
docker ps # get all running containers
# copy the id or container name
docker exec -it <container_id> /bin/bash # command to run the shell inside the Django container (container name: rating)
./manage.py createsuperuser # register superuser