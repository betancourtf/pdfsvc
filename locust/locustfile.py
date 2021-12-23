import random
from locust import HttpUser, task, between

test_urls = [
    "http://google.com",
    "http://duckduckgo.com",
    "http://medium.com",
    "http://slashdot.org",
    "http://engadget.com",
    "https://sparksuite.github.io/simple-html-invoice-template/",
    "https://nirajrajgor.github.io/html-invoice-templates/invoice1/invoice1.html",
    "https://nirajrajgor.github.io/html-invoice-templates/invoice2/invoice2.html",
    "https://nirajrajgor.github.io/html-invoice-templates/invoice3/invoice3.html",
    "http://cdn.invoicebus.com/templates/Vip%20(tertia)/template.html",
    "wrong-url-doesnt-exists-asdf.com",
]


class PDFUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def add_page_request(self):
        self.client.post(
            "/api/page-request/",
            json=dict(url=random.choice(test_urls)),
            headers=dict(Authorization=f"Token {self.token}"),
        )

    def on_start(self):
        response = self.client.post(
            "/auth/", json=dict(username="tester", password="pdfsvc123")
        )
        if not response.status_code == 200:
            raise ValueError
        data = response.json()
        self.token = data.get("token")
