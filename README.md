## configDB 

A database like , dynamic config file generator to enable more customization in
your python project . From games to ML notebooks and everything between.

## Support 

[X] Ini file type

[X] CRUD operations

[X] Zero dependency

## Install

### From main branch 

```bash
pip install git+https://github.com/shellordie/configDB.git@main
```

### From source

```bash
git clone https://github.com/shellordie/configDB
```

```
cd configDB
```

```bash
chmod +x run.sh
```

```bash
./run.sh
```

### From pypi 

```bash
pip install configDB
```

## Basic Usage

### Initialize configDB 

```python
>>> db=configDB("config") 
# configDB generate a folder "configs" with a file "config.ini"
```

### Create a section with it's elements 

```python
# create db take the section name for first agument and the data to be added for second argument 
# the data should be a dictionnary
>>> db.create("settings",{"theme":"dark","volume":34,"menu_style":"collapse"})
```

### Read from the db with "get()"

```python
>>> settings_data=get("settings") # take the section name and return a dictionnary 
>>> for key in settings_data: # print individual elements
>>>     print(key, settings_data[key])
```

### Read from the db with "iter()"

```python
>>> dbiterator=db.iter() # create an iterator
>>> settings_theme =dbiterator["settings"]["theme"] # get theme from settings
>>> print(settings_theme)
```

### Update the "theme" in  "settings" section

```python
>>> db.update("settings",{"theme":"light"}) 
```
### Delete the "settings" section

```python
>>> db.delete("settings")
```

## Other methods

```python
>>> len() # return the len of your configDB

>>> clear() # clear all sections in your configDB

>>> get_sections() # return all sections name in your configDB

>>> get_all() # return all sections data in your configDB

>>> has("section_name") # return True if the section name exist and False if not
```

## Need Help ?

If you need help or want a feature open an issue and i will look into it

Thanks you.
