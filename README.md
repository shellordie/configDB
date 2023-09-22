## configDB 

A database like , dynamic config file generator to enable more customization in
your python project . from games to ML notebooks and everything between

## Install

## From main branch 

```bash
pip install git+https://github.com/shellordie/configDB.git@main
```

## From source

```bash
git clone https://github.com/shellordie/configDB
```

```bash
chmod +x run.sh
```

```bash
./run.sh
```

## From pypi 

```bash
pip install configDB
```

## Support 

[x] Ini file type
[x] CRUD operations

## Usage

### Initialize configDB 

```python
>>> db=configDB("config") 

# configDB generate a folder "configs" with a file "config.ini"
```

### create a section with elements 

```python
# create db take the section name for first agument and the data to be added for second
argument 

# the data should be a dictionnary

>>> db.create("settings",{"theme":"dark","volume":34,"menu_style":"collapse"})
```



