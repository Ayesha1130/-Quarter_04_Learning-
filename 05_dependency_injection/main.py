from fastapi import FastAPI,Depends,HTTPException,Query,status
from typing import Annotated


app = FastAPI()

# 1. Simple Dependency
def get_simple_goal():
    return {"Goal": "We are building AI agent workforce"}

@app.get("/get_simple_goal")
def simple_goal(response: Annotated[dict, Depends(get_simple_goal)]):
    return response

# 2.  Dependency with parameter
def get_goal(userName: str):
    return {"Goal": "We are building AI agent workforce", "userName": userName}


# 3. Login with Query Parameters
def dep_login(username: str = Query(None), password: str = Query(None)):
    if username == "Admin" and password == "Admin":
        return {"Message" : "Login Successfully "}
    else:
        return {"Message" : "Login Failed"}
    
@app.get("/signin")
def login_api(user : Annotated[dict, Depends(dep_login)]):
    return user

# 4. Multiple Dependencies
def depfunc1(num: int):
    return num + 1

def depfunc2(num: int):
    return num + 2

@app.get("/main/{num}")
def get_main(
    num: int,
    num1: Annotated[int, Depends(depfunc1)],
    num2: Annotated[int, Depends(depfunc2)]
):
    total = num + num1 + num2
    return {"result": f"Pakistan {total}"}

# 5. Class-based Dependency
blog = {
    "1": "Generative AI blog",
    "2": "Machine Learning blog",
    "3": "Deep Learning blog"
}

user = {
    "8": "Ayesha",
    "9": "Iqbal"
}

class GetObjectOr404():
    def __init__(self,model):
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        
blog_dependency = GetObjectOr404(blog)
user_dependency = GetObjectOr404(user)

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return {"blog" : blog_name}

@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    return {"user" : user_name}
        

