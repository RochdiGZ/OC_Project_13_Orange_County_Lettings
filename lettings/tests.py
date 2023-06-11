from django.urls import reverse
import pytest

from .models import Address, Letting


@pytest.mark.django_db
def test_lettings_index(client):
    url = reverse("lettings:index")
    response = client.get(url)

    assert response.status_code == 200
    assert b"<title>Lettings</title>" in response.content


@pytest.mark.django_db
def test_lettings_detail(client):
    address = Address(
        number=15,
        street="Henry St Pearl River",
        city="New York",
        state="NY",
        zip_code=10965,
        country_iso_code="USA"
    )
    address.save()

    letting = Letting(
        title="Hilton Garden Inn",
        address=address
    )
    letting.save()
    url = reverse("lettings:letting",  args=[1])
    response = client.get(url, data={})

    assert response.status_code == 200
    assert b"<title>Hilton Garden Inn</title>" in response.content
