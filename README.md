# My storage
A simple solution to storage data in your python project using json tables and collections.

# Initialize module
### Import the module you would like to use or all
### Example
``` python
import Tables from mystorage
```
### or
``` python
import Tables,Collection,JsonObjects from mystorage
```

# My storage come with 3 solutions for storaging data 

### Json objects
Just like a json file write,read,update and drop json files.
``` python
from mystorage import JsonObjects

json_object = JsonObjects('fileName')

# read (open json object)
json_object.read()

# update json object
# make sure you use the .read() function before updating the object
json_object.update()
```

### Tables
Use sql type of data base, most follow every table structure.
``` python
from mystorage import Tables

table = Tables()
```

### Collections
Just like mongodb, Collections let you use the nosql type of database using index objects.
``` python
from mystorage import Collections

table = Collections()
```