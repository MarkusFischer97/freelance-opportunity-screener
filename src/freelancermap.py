import requests
from bs4 import BeautifulSoup

from models import Opportunity


BASE_URL = "https://www.freelancermap.de"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/151.0.0.0 Safari/537.36"
    )
}


def scrape_projects(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    projects = soup.select(".project-card")

    opportunities = []

    for project in projects:
        company = project.select_one(".project-info > div:first-child")
        title = project.select_one('[data-testid="title"]')
        skills = project.select('[data-id="project-card-keyword-link"]')
        remote = project.select_one('[data-testid="remoteInPercent"]')
        project_type = project.select_one('[data-testid="type"]')
        duration = project.select_one('[data-testid="duration"]')
        beginning = project.select_one('[data-testid="beginningMonth"]')
        created = project.select_one('[data-testid="created"]')
        location = project.select_one('[data-testid="city"]')

        if not title:
            continue

        skill_names = [skill.get_text(strip=True) for skill in skills]

        url_path = title.get("href")
        full_url = BASE_URL + url_path if url_path else ""

        remote_text = remote.get_text(strip=True) if remote else ""
        remote_percent = (
            int(remote_text.split("%")[0])
            if "%" in remote_text
            else 0
        )

        opportunity = Opportunity(
            company=company.get_text(strip=True) if company else "",
            title=title.get_text(strip=True),
            url=full_url,
            skills=skill_names,
            remote_percent=remote_percent,
            contract_type=(
                project_type.get_text(strip=True)
                if project_type
                else ""
            ),
            duration=duration.get_text(strip=True) if duration else "",
            beginning=beginning.get_text(strip=True) if beginning else "",
            created=created.get_text(strip=True) if created else "",
            location=location.get_text(" ", strip=True) if location else "",
        )

        opportunities.append(opportunity)

    return opportunities