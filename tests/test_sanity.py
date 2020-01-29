"""
Sanity test cases
"""


def test_index(client):
    """
    Checks that the 'Hello Car Api' message is shown on index
    """
    index_page = client.get("/")
    html = index_page.data.decode()

    assert index_page.status_code == 200
    assert "Hello Car API!" in html
