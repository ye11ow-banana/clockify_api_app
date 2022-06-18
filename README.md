# Installation

```sh
git clone https://github.com/ye11ow-banana/clockify_api_app.git
```

```sh
cd clockify_api_app
```

In the file `clockify.py` on lines 52, 53, 54, 55 replace `os.getenv(...)` with `"<your key or id>"`

Unix:
```sh
python3 -m venv venv
```
```sh
source venv/bin/activate
```
```sh
pip3 install -r requirements.txt
```
```sh
python3 clockify.py
```

Windows:
```sh
python -m venv venv
```
```sh
venv\Scripts\activate.bat
```
```sh
pip install -r requirements.txt
```
```sh
python clockify.py
```