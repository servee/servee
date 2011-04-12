import re

def space_out_camel_case(stringAsCamelCase):
    """
    @@TODO white-box implementation of this function from somebody who hasn't seen the code.
    
    Adds spaces to a camel case string.  Failure to space out string returns the original string.
    >>> space_out_camel_case('DMLSServicesOtherBSTextLLC')
    'DMLS Services Other BS Text LLC'
    
    Originally by Simon Hartley 12/27/2008, tbh, I'm not sure of the licensing presumptions of
    a site like the below...which means I probably don't have the right to use this.
    http://refactormycode.com/codes/675-camelcase-to-camel-case-python-newbie#refactor_139268
    """
    
    if stringAsCamelCase is None:
        return None

    pattern = re.compile('([A-Z][A-Z][a-z])|([a-z][A-Z])')
    return pattern.sub(lambda m: m.group()[:1] + " " + m.group()[1:], stringAsCamelCase)
