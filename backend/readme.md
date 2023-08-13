
To run server in dev mode
```bash
uvicorn web_api:app --reload
```

To run in production mode use
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker web_api:app
```