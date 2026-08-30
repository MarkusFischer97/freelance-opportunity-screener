import requests
from bs4 import BeautifulSoup


URL = "https://www.freelancermap.de/projekte/python"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/151.0.0.0 Safari/537.36"
    )
}

response = requests.get(URL, headers=headers)

print("Status code:", response.status_code)
print("Content length:", len(response.text))

soup = BeautifulSoup(response.text, "html.parser")

projects = soup.select(".project-card")

print(f"Projects found: {len(projects)}")

for project in projects[:5]:
    company = project.select_one(".project-info > div:first-child")
    title = project.select_one('[data-testid="title"]')
    skills = project.select('[data-id="project-card-keyword-link"]')
    remote = project.select_one('[data-testid="remoteInPercent"]')
    project_type = project.select_one('[data-testid="type"]')
    duration = project.select_one('[data-testid="duration"]')
    beginning = project.select_one('[data-testid="beginningMonth"]')
    created = project.select_one('[data-testid="created"]')

    skill_names = [skill.get_text(strip=True) for skill in skills]
    full_url = "https://www.freelancermap.de" + title.get("href")

    print()
    print("COMPANY:", company.get_text(strip=True))
    print("TITLE:", title.get_text(strip=True))
    print("URL:", full_url)
    print("SKILLS:", skill_names)
    print("REMOTE:", remote.get_text(" ", strip=True))
    print("TYPE:", project_type.get_text(" ", strip=True))
    print("DURATION:", duration.get_text(" ", strip=True))
    print("BEGINNING:", beginning.get_text(" ", strip=True))
    print("CREATED:", created.get_text(" ", strip=True))