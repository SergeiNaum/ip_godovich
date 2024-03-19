[![Lint Code](https://github.com/SergeiNaum/Stakewolle/actions/workflows/linter_check.yml/badge.svg)](https://github.com/SergeiNaum/Stakewolle/actions/workflows/linter_check.yml)
# Test task for the company ip_godovich
# **Api_Refs[rating](rating)** Api for working rating system. Created with DRF, redis


## Quick start

### For your convenience, the application is deployed on my private server at:
#### --> [CLICK FOR TEST HERE](http://77.222.53.154:8000/api/schema/swagger-ui/) <--
  
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

