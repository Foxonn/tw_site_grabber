from app.parser.lib_parser import run
import json
import re
import time


def parse_site(site_url):
    if not re.match(r"http(s|)", site_url):
        return {
            "error": "The site URL must contain the HTTP or HTTPS Protocol!"}

    if not re.match(r"http(s|):\/\/.*\..*(/|)", site_url):
        return {"error": "The site URL is not correct!"}

    result = run(site_url)

    return result


def test_hello_world():
    time.sleep(20)
    return {"notify": "test_hello_world"}
