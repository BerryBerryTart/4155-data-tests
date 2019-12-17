# Data Tests And Analysis Tools

## Steps Used To Process The Data
1. The raw file is processed with `./intervals/clean-data.py`
    * This creates a minified version of the data which can be parsed
    faster and easier. Data structure is described below.
    * DATE | TIME | CODE | MAC | AP
2. The minified data can then be processed with `./intervals/shard-by-hour.py`
which creates chunks of data by hour.
3. Since the data is now catagorised by hour, it can then be processed to find
activity by the hour in `./intervals/activity.py`
    * this creates ready to go JSON files to be imported
4. We can then average our data with the created JSON files using
`./intervals/render_averages.py`. This will also create ready to go JSON
files to be imported.

## Useful Things
- `./intervals/shard.py` can be used to break up large files into
managable 250k line chunks
- `./intervals/masterArray` contains all the access points by name
    * In binary pickle format
- `./intervals/blacklist.py` contains a list of the buildings to ignore
- `./intervals/building-map.py` directly maps the building codes to the actual
building names
- `./intervals/AccessPoint.py` is the data abstraction used to process activity
by set timeframe.
