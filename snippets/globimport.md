saving this in the __init__.py file will allow importing all the modules from the fgolder like so
```python
from folder import *
```

```python
from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
```
