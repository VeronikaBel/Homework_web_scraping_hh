import requests
import bs4
import json

''' <div class = vacancy-serp__results> -все вакансии на странице
<a class="bloko-link" href = "ссылка на ввакансию"> -ссылка на вакансию
<h2 "bloko-header-section-2"> - заголовок вакансии
<div class = "wide-container--lnYNwDTY2HXOzvtbTaHf" - тело вакансии, зп
<span class= "bloko-link bloko-link_kind-secondary"> - название компании


'''

KEYWORDS = ["Django", "Flask"]
URL = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"


response = requests.get (URL)
html_data = response.text

soup = bs4.BeautifulSoup (html_data, features= "lxml")

vacancies = soup.find_all('div', class_='vacancy-serp__results') #все вакансии на странице

vacancies_list = []

for vacancy in vacancies:
  link_tag = vacancy.find ('a', class_ = "bloko_link") # находим ссылку на вакансию
  if link_tag:
    link = link_tag['href']
  else:
    link = "No link"

  
  title_tag = vacancy.find ('h2', class_ = "bloko-header-section-2") # находим заголовок вакансии
  if title_tag:
    title = title_tag.text.strip()
  else:
    title = "No title"

  company_tag = vacancy.find ('span', class_ = "bloko-link bloko-link_kind-secondary") # находим название компании

  if company_tag:
    company = company_tag.text.strip()
  else:
    company = "No company"


  salary_tag = vacancy.find ('span', class_ = "bloko-text") #находим данные по зп !ЗДЕСЬ СОМНЕНИЯ ПО ПРАВИЛЬНОСТИ ВЫБРАННОГО ТЕГА
     
  if salary_tag:
    salary = salary_tag.text.strip()
  else:
    salary = "No salary"


  city_tag = vacancy.find ('span', class_ = "bloko-text") #находим данные по зп !ЗДЕСЬ СОМНЕНИЯ ПО ПРАВИЛЬНОСТИ ВЫБРАННОГО ТЕГА
# у города и зарплаты визуально одинаковые теги, хотя по факту это два разных места. Как поступить в таком случае? Как правильно прописать тег? 
  if city_tag:
    city = city_tag.text.strip()
  else:
    city = "No city"


  if any (keyword in title for keyword in KEYWORDS):
    vacancies_list.append ({'title': title, 'link': link, 'company':  company, 'salary': salary, 'city': city})


with open ('vacancies.json', 'w') as f:
  json.dump (vacancies_list, f, indent=2)


for vacancy in vacancies_list:
  print (f'Title: {vacancy["title"]}, link: {vacancy["link"]}, company: {vacancy["company"]}, salary: {vacancy["salary" ]}, city: {vacancy["city"]}')