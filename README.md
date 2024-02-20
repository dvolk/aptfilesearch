# aptfilesearch

aptfilesearch provides a web interface for searching through debian/ubuntu files in all packages

<table>
  <tr>
    <td>
<img src="https://i.imgur.com/pqgTuj4.png">      
    </td>
    <td>
<img src="https://i.imgur.com/TRgvOZO.png">
    </td>
  </tr>
  </table>

## Prerequesites

```
apt install python3-venv apt-file
sudo apt-file update
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
