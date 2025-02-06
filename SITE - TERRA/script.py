from gettext import install
from hashlib import scrypt
import xml

import IPython
import pip


pip install BeautifulSoup xml

from bs4 import BeautifulSoup

# 1️⃣ Abre o arquivo HTML original
with open("arquivo.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# 2️⃣ Remove comentários do HTML
for comment in soup.find_all(string=lambda text: isinstance(text, str) and text.startswith("<!--")):
    comment.extract()

# 3️⃣ Remove tags vazias (<div></div>, <p></p>, etc.)
for tag in soup.find_all():
    if tag.name not in ["br", "img"] and not tag.text.strip():  # Mantém tags essenciais
        tag.extract()

# 4️⃣ Remove classes, IDs e estilos inline
for tag in soup.find_all():
    tag.attrs = {key: value for key, value in tag.attrs.items() if key not in ["class", "id", "style"]}

# 5️⃣ Salva o HTML limpo
with open("arquivo_limpo.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

print("✅ HTML limpo salvo como 'arquivo_limpo.html'!")

IPython scrypt.py

