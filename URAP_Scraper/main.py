from bs4 import BeautifulSoup
import csv
import requests

url = "https://urapprojects.berkeley.edu/list.php?keywords=&category=&status=&faculty_department=&hours=&site=&sort=&faculty_id=&record_id=&modified=&max=50&skip=0"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all('div', class_="mt-3 h5")
professors = soup.find_all("strong")
main = soup.find("main", class_="container-lg").find_all("p")



# Open the CSV file for writing
with open('URAP_Data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Title', 'Professor', 'Weekly Hours',"main_description"])

    for i in range(4):
        url = "https://urapprojects.berkeley.edu/list.php?keywords=&category=&status=&faculty_department=&hours=&site=&sort=&faculty_id=&record_id=&modified=&max=50&skip=" + str(i*50)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        titles = soup.find_all('div', class_="mt-3 h5")
        professors = soup.find_all("strong")
        main = soup.find("main", class_="container-lg").find_all("p")

        weekly_hours_list = []
        descriptions_list = []
        for p in main:
            if "Weekly Hours: " in p.text:
                weekly_hours = p.text.split("Weekly Hours: ")[1].split(" hrs")[0]
                weekly_hours_list.append(weekly_hours)
                try:
                    description = main[main.index(p)+1].text
                    descriptions_list.append(description)
                except:
                    IndexError


        for i in range(len(titles)):
            title = titles[i].text
            professor = professors[i].text
            weekly_hours = weekly_hours_list[i]
            description = descriptions_list[i]
            writer.writerow([title, professor, weekly_hours,description])
