from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    
    assert response.status_code == 200
    # Ahora verificamos que aparezca tu nombre y la matrícula en el HTML
    assert b"George" in response.data
    assert b"20240001" in response.data