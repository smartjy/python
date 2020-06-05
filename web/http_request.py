import requests
from bs4 import BeautifulSoup

URL = 'http://www.daum.net'
# URL = 'http://example.com'
response = requests.get(URL)
response.status_code
response.text

# print('\n##### Response status code #####\n', response.status_code, '\n##### Response status code #####\n')
# print('\n##### Response Start #####\n', response.text, '\n##### Response End #####\n')

# html parse
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# <a class="link_info" data-tiara-action-name="푸터_고객센터" data-tiara-layer="cs" href="https://cs.daum.net/">고객센터</a>
link_list = []

links = soup.find_all('a')
# print(links)
for link in links:
    # print(link.attrs['href'])
    link_list.append(link.attrs['href'])

req_list = []
for req in link_list:
    if req.startswith('https') or req.startswith('http') or req.startswith('url'):
        req_list.append(req)

len_sorted_list = sorted(set(req_list), key=len, reverse=True)

res_time_list = []

for i in len_sorted_list[:10]:

    res_time = requests.get(i).elapsed.total_seconds()
    res_time_list.append((res_time, i))
    print(len(i), i)
    # print(res_time)

res_sorted_list = sorted(res_time_list, key=lambda t : t[0])

print(' ')

for j in res_sorted_list:
    print(j[0], j[1])

# print(len_sorted_list)

# domain = links.attrs('href')

# print(domain)


###################################################
links = soup.find('a')
# print(links.attrs['href'])
domain = links.attrs['href']
elapsed_time = response.elapsed.total_seconds()

link_list.append(elapsed_time)
link_list.append(domain)


# print(link_list)


# links.attrs['href']
# # print(links)
# link_list = []
# for link in links:
#     link_list.append(link.attrs['href'])
#     # print(link.attrs['href'])
#     print(link_list)
