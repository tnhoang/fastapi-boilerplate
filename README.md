TODO:
- create boilerplate with endpoints, models, crud, pydantic

NOTE:
- Must run backend at /src folder, it's convinient for import package
- Pip package python-jose, not jose.
- Export PYTHONPATH=$PWD to solve problems with import in projects
- Absolute and relative import: when you define PYTHONPATH, if you want to import module in a child
directory, you have 2 options: absolute and relative. If the child's too far away from parent, it's easier to import by
using relative import(.child3 instead dir(PYTHONPATH).child1.child2.child3)
- Problem with pylance, if raise missing import, check in settings JSON:
  - python.languageServer: Pylance
  - python.pythonPath: point to poetry environment
- Alembic Migration:
  - Assign Base model to alembic/env file
  - Change model
  - Run cmd: alembic revision --autogenerate -m "message"
  - alembic upgrade +1 / head
- Problem with sh file
  - Must declare PYTHONPATH
- Problem with pg database:
  - select * from public.user;
- Pydantic gonna validate input data from endpoint api

POETRY:
- poetry install
- list packages: poetry show
- poetry env list --full-path

Question:
- What is pip install python-multipart
-
