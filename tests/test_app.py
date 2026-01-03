from myapp.app import app

def test_about_page():
    # Use Flask's test client
    client = app.test_client()
    resp = client.get("/about")
    assert resp.status_code == 200
    assert b"About This App" in resp.data
