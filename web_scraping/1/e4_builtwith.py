#!/usr/bin/env python
import builtwith

if __name__ == '__main__':
    """
    >>> import builtwith1
    >>> builtwith.parse('http://example.webscraping.com')
    {u'javascript-frameworks': [u'jQuery', u'Modernizr', u'jQuery UI'], u'web-frameworks': [u'Web2py', u'Twitter Bootstrap'], u'programming-languages': [u'Python'], u'web-servers': [u'Nginx']}
    """

    print(builtwith.parse('http://example.webscraping.com'))
