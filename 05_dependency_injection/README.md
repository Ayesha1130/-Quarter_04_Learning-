# FastAPI Dependency Injection Demo 🚀

This project is a hands-on demonstration of **Dependency Injection (DI)** in FastAPI.  
It covers multiple ways of injecting reusable logic into API endpoints using `Depends()`.

---

## 📌 Features

- ✅ Simple function-based dependencies  
- ✅ Dependency with query parameters  
- ✅ Secure login with basic auth simulation  
- ✅ Multiple dependencies in one endpoint  
- ✅ Class-based dependencies with error handling (404)  
- ✅ Organized and testable code structure  

---

## 📂 Endpoints Overview

| Method | Endpoint                               | Description                            |
|--------|----------------------------------------|----------------------------------------|
| GET    | `/get_simple_goal`                     | Returns a static goal message          |
| GET    | `/get-goal?userName=Ali`               | Returns goal + username                |
| GET    | `/signin?username=Admin&password=Admin`| Simulates login check                  |
| GET    | `/main/{num}`                          | Shows sum using multiple dependencies  |
| GET    | `/blog/{id}`                           | Fetches blog title using class DI      |
| GET    | `/user/{id}`                           | Fetches user name using class DI       |

---

## 🛠️ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/fastapi-di-demo.git
cd fastapi-di-demo
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI 🚀

---

## 📚 Concepts Covered

- FastAPI's `Depends()` utility  
- Function-based & class-based DI  
- Sub-dependencies and query param injection  
- Error handling with `HTTPException`  
- Clean and modular API design  

---

## 🙏 Credits

Special thanks to my teacher for guiding me through the concepts!  
This project was built as part of my backend development learning journey.

---

## 📬 Contact

- Connect with me on [LinkedIn](https://www.linkedin.com/in/ayesha-iqbal-2613402b4/)  


---

## 🏷️ Tags

`#FastAPI` `#Python` `#Backend` `#DependencyInjection` `#Learning` `#API`
