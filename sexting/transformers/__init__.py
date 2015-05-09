from email import Email
from sms import SMS
from fbmsg import FBMsg
from phone import Phone
from bankwire import BankWire
from paypal import Paypal
from debitcard import DebitCard
from contactlesscard import ContactlessCard
from tube import Tube
from fbstatus import FBStatus
from tweet import Tweet

def all_transformers():
    return [
        Email(),
        SMS(),
        FBMsg(),
        Phone(),
        BankWire(),
        Paypal(),
        DebitCard(),
        ContactlessCard(),
        Tube(),
        FBStatus(),
        Tweet(),
    ]
