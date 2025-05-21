# 🔎 Task 07 — Deep Dive into OpenAI Agents SDK

📂 Repo: [Panaversity Learn Agentic AI](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first)  
📚 SDK Reference: [openai-agents-python Docs](https://openai.github.io/openai-agents-python/)

---

## ❓ Questions to Start Thinking (With Answers)

---

### 1️⃣ Why is the `Agent` class defined as a `dataclass`?

**✅ English Explanation:**

The `Agent` class is defined using `@dataclass` to:

- Simplify code with auto-generated `__init__`, `__repr__`, etc.
- Organize agent's properties (like name, model, instructions) cleanly
- Allow immutability and defaults easily

**🗣️ Roman Urdu:**

Dataclass use karne se Agent ka structure clean aur readable hota hai. Constructor (`__init__`) aapko manually likhna nahi padta.

**🧑‍💻 Code Example:**

```python
from dataclasses import dataclass

@dataclass
class Agent:
    name: str
    instructions: str
    model: str
```

📘 **Source:**  
[Agent Class – OpenAI Docs](https://openai.github.io/openai-agents-python/ref/agent/)

---

### 2️⃣ Why is `instructions` (system prompt) part of the `Agent` class?  
### 2a. Why can `instructions` also be a callable?

**✅ English Explanation:**

- **Static Prompt:** When instructions are just a string (e.g. "You are a fitness coach"), it defines the agent’s consistent behavior.
- **Callable Prompt:** If instructions is a function, it can dynamically generate prompts depending on time, context, or user data.

**🗣️ Roman Urdu:**

Instructions static bhi ho sakti hain aur function bhi. Agar function ho to har dafa naye instructions generate ho sakte hain — jaise "Suggest dinner based on current weather."

**🧑‍💻 Code Example:**

```python
# Static instructions
@dataclass
class Agent:
    instructions: str

# Dynamic instructions
def get_dynamic_instructions():
    return "You are a chef. Suggest a recipe based on the season."

@dataclass
class Agent:
    instructions: str | Callable = get_dynamic_instructions
```

📘 **Why useful?**  
Dynamic prompts = More personalized agents.

---

### 2b. Why is the user prompt passed to `Runner.run()` as a parameter?  
And why is `run()` a `@classmethod`?

**✅ English Explanation:**

- The **user prompt** changes every time, so it should not be fixed in the agent.
- It is passed at runtime to `Runner.run(agent, prompt)`.
- Using `@classmethod` means you don't need to create a `Runner` instance — it's a utility function that runs the agent directly.

**🗣️ Roman Urdu:**

Har baar user ka input (prompt) alag hota hai — is liye usay `run()` function mein pass kiya jata hai. `@classmethod` banana isliye asaan hai taake direct call kiya ja sake.

**🧑‍💻 Code Example:**

```python
from openai_agents import Runner

user_prompt = "Suggest a healthy breakfast."
result = Runner.run(agent=health_agent, prompt=user_prompt)
print(result)
```

📘 Source: [Runner.run() – OpenAI Docs](https://openai.github.io/openai-agents-python/ref/run/)

---

### 3️⃣ What is the purpose of the `Runner` class?

**✅ English Explanation:**

The `Runner` class is the execution engine. It:

- Takes an `Agent` and a user prompt
- Sends everything to the OpenAI model
- Returns the agent's response

You can think of it as the **orchestrator or conductor** of the agent execution.

**🗣️ Roman Urdu:**

Runner class agent ko chalata hai. User input leta hai, agent ki instructions ke sath combine karta hai, aur result nikaalta hai.

**🧑‍💻 Code Flow:**

```python
result = Runner.run(agent=agent_object, prompt="Give me a workout plan.")
```

📌 **Purpose:** Simplifies complex agent execution into one method call.

---

### 4️⃣ What are Generics in Python? Why use them for `TContext`?

**✅ English Explanation:**

Generics allow classes and functions to accept multiple data types safely.  
`TContext` is a **generic type variable** used to pass context (like user preferences or history) into an Agent in a type-safe way.

**🗣️ Roman Urdu:**

Generics ek flexible box jese hain. Aap context mein string, dict, ya kisi bhi type ka data de sakte ho, aur Python aapko error se bachata hai.

**🧑‍💻 Code Example:**

```python
from typing import TypeVar, Generic
from dataclasses import dataclass

TContext = TypeVar("TContext")

@dataclass
class Agent(Generic[TContext]):
    name: str
    instructions: str
    model: str
    context: TContext
```

📘 **Why useful?**

- Flexible: Supports different kinds of data
- Safe: Catches type mismatches
- Reusable: Same class works across different projects

---

## ✅ Summary

| Question | Summary |
|---------|---------|
| Why `dataclass`? | Clean, auto-generated methods for Agent setup |
| Why system prompt in Agent? | Defines personality, supports static/dynamic behavior |
| Why user prompt in `run()`? | It changes per request; `classmethod` simplifies execution |
| Purpose of Runner? | Handles execution, simplifies agent invocation |
| Why Generics (`TContext`)? | Flexibility + type safety for context-specific agents |

---

## 📚 References

- [🔗 Agent Class Reference](https://openai.github.io/openai-agents-python/ref/agent/)
- [🔗 Runner Class Reference](https://openai.github.io/openai-agents-python/ref/run/)
- [📁 GitHub Repo](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first)

---

Let’s keep building smarter, flexible agents using OpenAI’s powerful Agent SDK 🚀
