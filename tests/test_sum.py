#import unittest

from fastapi.testclient import TestClient
from app import main
#class TestSum(unittest.TestCase):
#
#    def test_sum(self):
#        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

# start hatim code

client = TestClient(main.app)

def test_root():
    # make request to root
    response = client.get("/")
    # validate status code on success
    assert response.status_code == 200
    # validate response on success
    assert response.json() == {"message": "Hello World. Welcome to the API home page!"}

def test_path():
    # make request to root
    response = client.get("/path")
    # validate status code on success
    assert response.status_code == 200
    # validate response on success
    assert response.json() == {"message": "This is /path endpoint, use post request to transform text to uppercase"}

def test_path_post():
    # msg
    msg = "hello"
    # json data
    data = {'msg': msg}
    # make request to root
    response = client.post("/path", json=data)
    # validate status code on success
    assert response.status_code == 200
    # validate response on success
    assert response.json() == {"message": msg.upper()}

def test_path_id():
    # path_id
    path_id = 21
    url = f"/path/{path_id}"
    # make request to root
    response = client.get(url)
    # validate status code on success
    assert response.status_code == 200
    # validate response on success
    assert response.json() == {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}

# end hatim code

#if __name__ == '__main__':
#    unittest.main()
