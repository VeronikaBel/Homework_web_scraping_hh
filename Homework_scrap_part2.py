import requests
import bs4
import json

URL = "https://spb.hh.ru/search/vacancy"

response = requests.get(URL)
html_data = response.text

soup = bs4.BeautifulSoup(html_data, features = "lxml")
vacancies = soup.find_all('div', class_='vacancy-serp__results') #все вакансии

vacancies_list = []

for vacancy in vacancies_list:
  title_tag = vacancy.find ("h2", class_ = "bloko-header-section-2")
  title = title_tag.text.strip()

  link_tag = vacancy.find ("a", class_ = "bloko-link")["href"]

  salary_tag = vacancy.find ("span", class_ = "fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh")
  salary = salary_tag.text.strip()
  if USD not in salary:
    continue

  vacancies_list.append ({"title": title, "salary": salary, "link": link_tag})

with open ("vacancies.json", "w") as f:
  json.dump (vacancies_list, f, indent = 3)
  

