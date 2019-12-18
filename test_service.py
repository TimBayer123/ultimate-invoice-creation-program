from vat_validation import *

install_requirements()
validation_result = check_vat("DE262567315")
print(type(validation_result))

print("PARTY HARD")