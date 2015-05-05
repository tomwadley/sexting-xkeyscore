from email import Email
from sms import SMS
from fbmsg import FBMsg
from voip import Voip
from bankwire import BankWire
from paypal import Paypal

def all_transformers():
    return [
        Email(),
        SMS(),
        FBMsg(),
        Voip(),
        BankWire(),
        Paypal(),
    ]
