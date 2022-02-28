import os
import socket
import fastapi as _fastapi


app = _fastapi.FastAPI()


@app.get(path="/", response_class=_fastapi.responses.HTMLResponse, status_code=_fastapi.status.HTTP_200_OK)
def read_root():
    # return {"message": "Hello World", "Cor": str(os.getenv(key='COR', default="AZUL")), "PID": str(os.getpid()), "HostName": str(socket.gethostname())}
    cor = os.getenv(key='COR', default="#000000")
    cor_descr = os.getenv(key='COR_DESCR', default="PRETO")
    html_content = f'''
        <!DOCTYPE html> 
        <html> 
            <body bgcolor="#{str(cor)}"> 
                <div style="text-align: center"> 
                    <br/> <br/>
                    <h1 style="color: white">EU SOU A COR {str(cor_descr)}</h1> 
                    <p style="color: white">PID: {str(os.getpid())}</p> 
                    <p style="color: white">HostName: {str(socket.gethostname())}</p>
                </div> 
            </body> 
        </html> 
    '''
    return _fastapi.responses.HTMLResponse(content=html_content, status_code=_fastapi.status.HTTP_200_OK)


# python3 -m venv venv
# source venv/Scripts/activate
# cd venv\Scripts
# activate

# pip install --upgrade pip
# pip install fastapi[all] -U
# pip install "uvicorn[standard]" -U
# pip install "hypercorn[trio]" -U
# pip install pytest -U
# pip install pytest-cov -U

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
