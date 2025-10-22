## The following repository helps you to understand how to integrate pytest and flake8 linting with github actions


Steps to clone the repository

```bash
git clone https://github.com/uchiha-vivek/Pytest-CICD.git
```

```bash
cd Pytest-CICD
```

```bash
python -m venv venv
pip install -r requirements.txt
venv\Scripts\activate
```


Running all the test cases from the root folder

```bash
pytest -v   
```

Running the flake command

```bash
flake8 . 
```