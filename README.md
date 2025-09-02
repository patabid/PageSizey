# PageSizey
## Sizing your paper

PageSizey is a simple module written to facilitate getting the most likely paper page size from a set of input dimensions.

Its primary use case is to identify the most likely page size code (ex. A4) from the `CropBox` feature in a pdf. 

## Installation
```
pip install PageSizey
```
## Example:
```
from pagesizey import page_size

size = page_size(8.5, 11) # inch page size in this case, mm values can also be used

print(size)
```

## Returns
```
{
    'standard': 'ansi',
    'size': 'a',
    'common_name': 'letter', # This only appears if there is a common name
}
```

# License
Simple, MIT, no warranty implied or given.

Copywrite 2025 [PataBid Inc.](https://patabid.com)
