![Coverage Status](https://coveralls.io/repos/estebistec/drf-compound-fields/badge.png?branch=master)
![PyPI version](https://d25lcipzij17d.cloudfront.net/badge.png?id=py&r=r&ts=1683906897&type=3e&v=2.0.0&x2=0)

# DRF Compound Fields

* [Full Documentation](https://drf-compound-fields.readthedocs.io/)
* [Source Code](https://github.com/estebistec/drf-compound-fields)
* [PyPI](https://pypi.org/project/drf-compound-fields/)

# Installation

Install the package from pip:

```
pip install drf-compound-fields
```

# Basic Usage

```python
# Models
class User(AbstractUser):
    phone_numbers = models.JSONField(default=list)
    skills = models.JSONField(default=list)
    bookmarks = models.JSONField(default=dict)
    measurements = models.JSONField(default=dict) # Stores height and weight as measurements

# Serializers
from drf_compound_fields.fields import ListField, ListOrItemField, DictField, PartialDictField

class UserSerializer(serializers.ModelSerializer):
    # This is the new stuff:
    phone_numbers = ListField(child=serializers.CharField(), allow_empty=True)
    skills = ListField(child=serializers.CharField(), allow_empty=True)  # E.g., ["javascript", "python", "ruby"]
    username = ListOrItemField(serializers.CharField())  # E.g., "Prince" or ["John", "Smith"]
    bookmarks = DictField(child=serializers.URLField(), allow_empty=True)  # E.g., {"./": "http://slashdot.org"}
    measurements = PartialDictField(child=serializers.IntegerField(), included_keys=['height', 'weight'])
```