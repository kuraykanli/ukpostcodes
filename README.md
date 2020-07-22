# ukpostcodes

Library that validates and formats post codes for UK. 

# Installation
###### PIP Installation
```python
$ pip install ukpostcodes
```

###### Clone the Repository
`git@github.com:kuraykanli/ukpostcodes.git`

###### Installing to environment and running tests
```python
   # Install pip dependencies for standalone run from library
   pip install -r requirements.txt

   # Run Setup file for install to global or virtual environment
   python3 setup.py install

   # Unit Tests are available at tests.py
   python3 -m unittest tests.py

```

# Usage
Import Library
```python
import ukpostcodes.ukpostcodes as ukpostcodes
```

## get_postcode_details
```python
ukpostcodes.get_postcode_details(postcode)
```

This method returns details of postcode in serializable JSON data from GET request made to API
* **:param postcode** - Input of postcode is required.
* **:return: json** - Includes details of postcode if postcode is valid


## validate_postcode_api
```python
ukpostcodes.validate_postcode_api(postcode)
```

This method returns validity status of postcode as boolean from GET request made to API

Remark: This method verifies legitimacy of the postcode.
* **:param postcode** - Input of postcode is required.
* **:return: boolean** - True if valid and False if invalid


## validate_postcode_regex
```python
ukpostcodes.validate_postcode_regex(postcode)
```

This method returns validity status of postcode as boolean from regex

Remark: This method only validates the formatting and doesn't verify legitimacy of the postcode.
* **:param postcode** - Input of postcode is required.
* **:param rexgex** - Optional: Regular Expression for validation. Default value set from variable
* **:return: boolean** - True if valid and False if invalid


## parse_inward
```python
ukpostcodes.parse_inward(postcode)
```

This method returns parsed string of Inward Code after validating via regex.
* **:param postcode** - Input of postcode is required.
* **:return: json** - String of Inward Code


## parse_outward
```python
ukpostcodes.parse_outward(postcode)
```

This method returns parsed string of Outward Code after validating via regex.
* **:param postcode** - Input of postcode is required.
* **:return: json** - String of Outward Code


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)