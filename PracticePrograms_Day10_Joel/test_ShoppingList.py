import pytest
from ShoppingList import app
from flask import jsonify

def test_Create_Get_200():
    tester = app.test_client()
    response = tester.get('/list')
    status = response.status_code
    assert status == 200

def test_Create_post_200():
    tester = app.test_client()
    response = tester.post('/list', json={"item_name":"test_items","item_quantity":3})
    assert response.status_code == 200

def test_Create_post_400_SameItem():
    tester = app.test_client()
    response = tester.post('/list', json={"item_name":"test_items","item_quantity":3})
    assert response.status_code == 400

def test_Create_post_400_Validations():
    tester = app.test_client()
    response = tester.post('/list', json={"item_name":"","item_quantity":0})
    assert response.status_code == 400

def test_EditList_put_200():
    tester = app.test_client()
    response = tester.put('/list/test_items', json={"item_name":"test_items","item_quantity":4})
    assert response.status_code == 200

def test_EditList_put_404():
    tester = app.test_client()
    response = tester.put('/list/test_items2', json={"item_name":"test_items","item_quantity":4})
    assert response.status_code == 404

def test_EditList_put_400():
    tester = app.test_client()
    response = tester.put('/list/test_items', json={"item_name":"","item_quantity":0})
    assert response.status_code == 400

def test_EditList_delete_200():
    tester = app.test_client()
    response = tester.delete('/list/test_items')
    assert response.status_code == 200

def test_EditList_delete_404():
    tester = app.test_client()
    response = tester.delete('/list/test_items')
    assert response.status_code == 404



