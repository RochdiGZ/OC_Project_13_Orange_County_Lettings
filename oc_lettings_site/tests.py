import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index(client):
    url = reverse('index')
    response = client.get(url)

    assert response.status_code == 200
    assert b"<title>Holiday Homes</title>" in response.content
