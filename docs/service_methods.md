1. What is the user trying to do?
2. What inputs are needed?
3. What must be true before this is allowed?
4. What existing data do I need to load?
5. What changes should happen?
6. What side effects should happen?
7. What should be returned?


POST   /tasks             needs body: what should I create?
PATCH  /tasks/{task_id}   usually needs body: what should I change?
GET    /tasks/{task_id}   no body: ID is in the path
DELETE /tasks/{task_id}   no body: ID is in the path
GET    /tasks             no body, maybe query params for filters
