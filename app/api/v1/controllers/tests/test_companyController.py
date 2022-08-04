from app.test_main import client

def test_getCompanies():
    response = client.get("/api/v1/company")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_createCompany_InvalidName():
    response = client.post("/api/v1/company/", json={"name": "si", "cnpj": 29371937219379})
    assert response.json()['detail'][0]['msg'] == "Name must be at least 3 characters"
    assert response.status_code == 422

def test_createCompany_withoutName():
    response = client.post("/api/v1/company/", json={"cnpj": 2937193721937})
    assert response.json()['detail'][0]['msg'] == "field required"
    assert response.status_code == 422

def test_createCompany_withoutCNPJ():
    response = client.post("/api/v1/company/", json={"name": "Test Company"})
    assert response.json()['detail'][0]['msg'] == "field required"
    assert response.status_code == 422

def test_createCompany_CNPJ_less14():
    response = client.post("/api/v1/company/", json={"name": "Test Company", "cnpj": 2937193721937})
    assert response.json()['detail'][0]['msg'] == "CNPJ must be 14 digits"
    assert response.status_code == 422

def test_createCompany_CNPJ_more14():
    response = client.post("/api/v1/company/", json={"name": "Test Company", "cnpj": 293719372193712})
    assert response.json()['detail'][0]['msg'] == "CNPJ must be 14 digits"
    assert response.status_code == 422


def test_createCompany_InvalidPath():
    response = client.post("/api/v1/company")
    assert response.status_code == 307
