# Awake

Python script to move mouse every {x} minutes with option of pressing a key to keep you pc   
awake while you're away. 

#### Examples:
```shell
# -m   number of minutes, defaults to 3
# -k   key to press and the number of times to press it, defaults to None

# using default settings
> python src/awake.py

# setting activity check to 1 minute
> python src/awake.py -m 1

# setting activity check to 2 minutes, then press shift key 3 times 
> python src/awake.py -m 2 -k shift:3 
```

### Logging
 _Outputs a random quote and depending on color you can tell the status:_
 - _**Cyan**_ - Activity
 - _**Yellow**_ - No Activity
