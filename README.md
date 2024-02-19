# aptfilesearch

aptfilesearch provides a web interface for searching through debian/ubuntu files in all packages

<img width="49%" src="https://i.imgur.com/pqgTuj4.png">
<img width="49%" src="https://i.imgur.com/TRgvOZO.png">

## Prerequesites

```
apt install python3-venv apt-file
sudo apt-file upate
```

## Installation

```
git clone https://github.com/dvolk/aptfilesearch
cd aptfilesearch
python3 -m venv env
./env/bin/pip install fastapi uvicorn jinja2
```

## Running

```
./env/bin/uvicorn main:app --reload
```