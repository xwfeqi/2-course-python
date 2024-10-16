import uuid
from .exceptions import InvalidParcelException, ParcelNotFoundException

class Parcel:
    def __init__(self, sender, recipient, weight):
        if not sender or not recipient:
            raise InvalidParcelException("Інформація про відправника або отримувача відсутня.")
        if weight > 30:
            raise InvalidParcelException("Перевищено максимальну вагу посилки: 30 кг.")

        self.tracking_number = str(uuid.uuid4())
        self.sender = sender
        self.recipient = recipient
        self.weight = weight
        self.status = "прийнято"

class PostalOffice:
    instances = []

    def __init__(self):
        self.parcels = {}
        PostalOffice.instances.append(self)

    def accept_parcel(self, parcel):
        self.parcels[parcel.tracking_number] = parcel
        parcel.status = "прийнято"

    def dispatch_parcel(self, parcel):
        if parcel.tracking_number not in self.parcels:
            raise ParcelNotFoundException("Посилку не знайдено.")
        parcel.status = "в дорозі"

    def receive_parcel(self, parcel):
        if parcel.tracking_number not in self.parcels:
            raise ParcelNotFoundException("Посилку не знайдено.")
        parcel.status = "отримано"

    def deliver_parcel(self, parcel):
        if parcel.tracking_number not in self.parcels:
            raise ParcelNotFoundException("Посилку не знайдено.")
        parcel.status = "доставлено"

def track_parcel(tracking_number):
    for office in PostalOffice.instances:
        if tracking_number in office.parcels:
            parcel = office.parcels[tracking_number]
            return parcel.status
    raise ParcelNotFoundException("Посилку не знайдено.")
