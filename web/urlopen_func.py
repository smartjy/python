from urllib.request import urlopen

# GET Method
data = 'langeage=python&framework=django'
f = urlopen("http://www.example.com")
print(f.read().decode('utf-8'))

# POST Method
data = 'langeage=python&framework=django'
f = urlopen("http://127.0.0.1:8000", bytes(data, encoding='utf-8'))
print(f.read(500).decode('utf-8'))
