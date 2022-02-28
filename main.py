import os
import socket
from datetime import timedelta
import fastapi as _fastapi
from fastapi_login import LoginManager
# from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException


app = _fastapi.FastAPI()
manager = LoginManager(secret='b#=x&h)cms#lsr*4+jghmlsrpe^p3nyoamu$860gip$4h+00w', token_url='/login', use_cookie=True)


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


@app.get(path="/test", status_code=_fastapi.status.HTTP_200_OK)
def read_test():
    return {"message": "Hello World", "Cor": str(os.getenv(key='COR', default="AZUL")), "PID": str(os.getpid()), "HostName": str(socket.gethostname())}


fake_db = {'chris@.mail': {'password': '123'}}


@manager.user_loader()
def load_user(email: str):
    user = fake_db.get(email)
    return user


@app.get(path='/login', status_code=_fastapi.status.HTTP_200_OK)
def login(response: _fastapi.Response):  # data: OAuth2PasswordRequestForm = _fastapi.Depends() , user = Depends(manager)
    email = "chris@.mail"  # data.username
    password = "123"  # data.password
    user = load_user(email)
    if not user:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif password != user['password']:
        raise InvalidCredentialsException
    access_token = manager.create_access_token(data=dict(sub=email), expires=timedelta(hours=12))
    manager.set_cookie(response=response, token=access_token)
    return {'access_token': access_token, 'token_type': 'bearer'}


@app.get(path='/logado', status_code=_fastapi.status.HTTP_200_OK)
def protected_route(user=_fastapi.Depends(manager)):
    return {
        'cor': str(os.getenv(key='COR', default="#000000")),
        'cor_descr': str(os.getenv(key='COR_DESCR', default="PRETO")),
        'pid': str(os.getpid()),
        'hostname': str(socket.gethostname()),
        'username': user,
    }




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
# pip install fastapi-login

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

# git tag
# git tag v1.0.0
# git push --tags
# git push origin --tags

# git tag -a v1.0.10 -m "New release"
# git push origin v1.0.10