from schemas import User, Task

USERS: dict[int, User] = {}
TASKS: dict[int, Task] = {}

user_id_seq = 1
task_id_seq = 1
