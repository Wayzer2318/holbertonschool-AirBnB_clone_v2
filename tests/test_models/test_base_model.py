#!/usr/bin/python3

from models.base_model import BaseModel


def test_id_is_str():
    model = BaseModel()
    assert str(type(model.id)) == "<class 'str'>"


def test_created_is_dtobj():
    model = BaseModel()
    assert str(type(model.created_at)) == "<class 'datetime.datetime'>"

def test_updated_is_dtobj():
    model = BaseModel()
    assert str(type(model.updated_at)) == "<class 'datetime.datetime'>"
