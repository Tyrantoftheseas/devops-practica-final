from app import app

def test_hello():
    # Crea un cliente de prueba
    client = app.test_client()
    # Realiza una petición GET a la raíz '/'
    response = client.get('/')

    # Verifica que el status code sea 200 (OK)
    assert response.status_code == 200
    # Verifica que el mensaje sea el esperado
    assert b"Hola Mundo desde DevOps!" in response.data