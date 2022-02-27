import os
import fastapi as _fastapi
# import uvicorn
# import asyncio
# from hypercorn.config import Config
# from hypercorn.asyncio import serve


app = _fastapi.FastAPI()


@app.get("/")
def read_root():
    return {"Cor": str(os.getenv(key='COR', default="AZUL")), "PID": str(os.getpid())}


if __name__ == "__main__":
    # uvicorn.run("main:app", host="127.0.0.1", port=5001, log_level="info", reload=True, debug=True, workers=1)
    # config = Config()
    # config.bind = ["127.0.0.1:5001"]
    # config.use_reloader = True
    # asyncio.run(serve(app, config))
    pass

# pip install --upgrade pip
# pip install fastapi[all] -U
# pip install "uvicorn[standard]" -U
# pip install "hypercorn[trio]" -U

# uvicorn main:app --reload
# hypercorn main:app --worker-class trio

# pip freeze > requirements.txt
# pip install -r requirements.txt

# docker-compose down
# docker-compose up -d --build

# kubectl config get-contexts
# kubectl config use-context docker-desktop
# kubectl config use-context minikube
# kubectl delete service wrk-jenkins-preto-01
# kubectl delete deployment wrk-jenkins-preto-01
# kubectl delete rs wrk-jenkins-preto-01-59f65b4495
# kubectl apply -f deployment.yaml

