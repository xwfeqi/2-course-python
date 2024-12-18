import pytest
from postal_service.parcel import Parcel, PostalOffice, track_parcel
from postal_service.exceptions import InvalidParcelException, ParcelNotFoundException


def test_create_parcel():
    parcel = Parcel(sender="John Doe", recipient="Jane Doe", weight=10)
    assert parcel.tracking_number is not None
    assert parcel.sender == "John Doe"
    assert parcel.recipient == "Jane Doe"
    assert parcel.weight == 10
    assert parcel.status == "прийнято"

def test_parcel_weight_limit():
    with pytest.raises(InvalidParcelException):
        Parcel(sender="John Doe", recipient="Jane Doe", weight = 35)

def test_accept_parcel():
    parcel = Parcel(sender="John Doe", recipient="Jane Doe", weight=5)
    office = PostalOffice()
    office.accept_parcel(parcel)
    assert parcel.status == "прийнято"

def test_dispatch_parcel():
    parcel = Parcel(sender="John Doe", recipient="Jane Doe", weight=5)
    office = PostalOffice()
    office.accept_parcel(parcel)
    office.dispatch_parcel(parcel)
    assert parcel.status == "в дорозі"

def test_receive_parcel():
    parcel = Parcel(sender="John Doe", recipient="Jane Doe", weight=5)
    office = PostalOffice()
    office.accept_parcel(parcel)
    office.dispatch_parcel(parcel)
    office.receive_parcel(parcel)
    assert parcel.status == "отримано"

def test_deliver_parcel():
    parcel = Parcel(sender="John Doe", recipient="Jane Doe", weight=5)
    office = PostalOffice()
    office.accept_parcel(parcel)
    office.dispatch_parcel(parcel)
    office.receive_parcel(parcel)
    office.deliver_parcel(parcel)
    assert parcel.status == "доставлено"

def test_track_parcel():
    parcel = Parcel(sender="John Doe", recipient="Jane Doe", weight=5)
    office = PostalOffice()
    office.accept_parcel(parcel)
    tracking_number = parcel.tracking_number
    assert track_parcel(tracking_number) == "прийнято"

def test_track_invalid_parcel():
    office = PostalOffice()
    with pytest.raises(ParcelNotFoundException):
        track_parcel("INVALID_TRACKING_NUMBER")
