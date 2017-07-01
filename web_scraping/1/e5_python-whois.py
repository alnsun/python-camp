#!/usr/bin/env python

import whois

print whois.whois('python.org')

"""
{
  "updated_date": "2017-02-25 03:10:25",
  "status": "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
  "name": "Domain Administrator",
  "dnssec": "unsigned",
  "city": "Beaverton",
  "expiration_date": "2018-03-28 05:00:00",
  "zipcode": "97008",
  "domain_name": "PYTHON.ORG",
  "country": "US",
  "whois_server": null,
  "state": "OR",
  "registrar": "Gandi SAS",
  "referral_url": null,
  "address": [
    "9450 SW Gemini Dr.",
    "ECM# 90772"
  ],
  "name_servers": [
    "NS3.P11.DYNECT.NET",
    "NS1.P11.DYNECT.NET",
    "NS2.P11.DYNECT.NET",
    "NS4.P11.DYNECT.NET"
  ],
  "org": "Python Software Foundation",
  "creation_date": "1995-03-27 05:00:00",
  "emails": [
    "e89d6901ba3e470e8cedc3eaa32a0074-1697561@contact.gandi.net",
    "7fd79ebe18980da9baceef0fa1b27680-1705778@contact.gandi.net"
  ]
}
"""
