# fastapi_linux
usage in linux

# API
This is the repository for API source.

## Getting Start

How to startup this api
```bash
cd /path/fastapi_linux
uvicorn app:my_app --host 0.0.0.0 --port 8000 --workers 10
```
  
execution with log_config
```bash
uvicorn app:my_app --host 0.0.0.0 --port 8000 --workers 10 --log-config log_config.ini
```
  
## Sample Requests
1. url (GET method)
   ```bash
   curl -X GET http://vm_ip:8000/get
   ```
  
2. url (POST method)
   ```
   curl -X POST http://vm_ip:8000/url -H "Content-Type: application/json" -d '{"user":"test_user","data":"my_data"}' 
   ```