import requests
import re

api_baseurl =  'https://api.postcodes.io/postcodes/{}'  # PostCodes.IO API used
validator_regex = '^([A-Z][A-HJ-Y]?[0-9][A-Z0-9]? ?[0-9][A-Z]{2}|GIR ?0A{2})$'  # This is default regex used. Custom regex can be used for required functions

def get_postcode_details(postcode):
    """
    This method returns details of postcode in serializable JSON data from GET request made to API

    :param postcode: Input of postcode is required.
    :return: json: Includes details of postcode
    """
    try:
        data = requests.get(api_baseurl.format(postcode), timeout=1)
        return data.json()
    except Exception as exp:
        print(exp)

def validate_postcode_api(postcode):
    """
    This method returns validity status of postcode as boolean from GET request made to API
    Remark: This method verifies legitimacy of the postcode.

    :param postcode: Input of postcode is required.
    :return: boolean: True if valid and False if invalid
    """
    try:
        data = requests.get(api_baseurl.format(postcode) + '/validate', timeout=1)
        return True if data.status_code == 200 and data.json()['result'] else False
    except Exception as exp:
        print(exp)

def validate_postcode_regex(postcode, regex = validator_regex):
    """
    This method returns validity status of postcode as boolean from regex
    Remark: This method only validates the formatting and doesn't verify legitimacy of the postcode.

    :param postcode: Input of postcode is required.
    :param regex: Regular Expression for validation. Default value set from variable above
    :return: boolean: True if valid and False if invalid
    """
    try:
        regex = re.compile(regex)
        return False if regex.search(postcode) is None else True
    except Exception as exp:
        print(exp)


def parse_inward(postcode):
    """
    This method returns parsed string of Inward Code after validating via regex

    :param postcode: Input of postcode is required.
    :return: string: String of Inward Code
    """
    try:
        if validate_postcode_regex(postcode):
            return postcode.split(" ")[1]
    except Exception as exp:
        print(exp)

def parse_outward(postcode):
    """
    This method returns parsed string of Outward Code after validating via regex

    :param postcode: Input of postcode is required.
    :return: string: String of Outward Code
    """
    try:
        if validate_postcode_regex(postcode):
            return postcode.split(" ")[0]
    except Exception as exp:
        print(exp)
