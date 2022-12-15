def test_request_main_page(client):
    response = client.get("/")
    assert b"<h2>Hello, Flask Web</h2>" in response.data