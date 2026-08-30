from freelancermap import scrape_projects


URL = "https://www.freelancermap.de/projekte/python"


opportunities = scrape_projects(URL)

print(f"Opportunities found: {len(opportunities)}")

for opportunity in opportunities[:5]:
    print()
    print(opportunity)