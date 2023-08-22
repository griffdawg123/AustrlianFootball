from get_page import get

result = []
soup = get("https://fbref.com/en/squads/a3aba642/Australia-Women-Stats")
stat_table = soup.find_all("tbody")
print((stat_table))