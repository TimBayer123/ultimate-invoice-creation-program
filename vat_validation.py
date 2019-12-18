import subprocess
import sys
import re

from zeep import Client

"""
 example:

    validation_result = check_vat("DE262567315")
    print(type(validation_result)) 

"""



client = Client("http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl")

# installs requirements
def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "zeep"])

# returns bo
def check_vat(vat_ID):
    vat_id_split = re.split('(\d+)',vat_ID)
    validation_result = client.service.checkVat(countryCode=vat_id_split[0], vatNumber=vat_id_split[1])
    return validation_result['valid']

