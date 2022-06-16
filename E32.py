from bs4 import BeautifulSoup

soup = BeautifulSoup("<html> <p>ekta <strong> Patel <a> Hello</html>", "html.parser")
print(soup.prettify())