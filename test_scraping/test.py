from typing import List
import resources

import requests
from bs4 import BeautifulSoup, Tag
from dateutil.parser import parse

import logging

# states = ("WI", "CA", "CT")


# states = ("TE") # Issue!!!

# states = (
#     "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
#     "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR",
#     "PA",
#     "RI", "SC", "SD", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")


state_abbrs = (
    "AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA",
    "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR",
    "PA", "RI", "SC", "SD", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY")

state_names = (
    "Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia",
    "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky",
    "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana",
    "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York",
    "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Texas", "Utah",
    "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"
)

states = list(zip(state_abbrs, state_names))

# states = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
# "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA",
# "RI", "SC", "SD", "TE", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")


class Note(object):
    text: str
    raw: list


class Meta(object):
    column_count: int
    row_count: int


class Info(object):
    note = Note()
    meta = Meta()


# def print_html(html):
#
#     print("--------------------------")
#
#     for group in html:
#
#         print(group.text)
#         print("--------------------------")


def print_tables(tables: List[Tag], state):
    for table_html in tables:
        headers, body, info = extract_table_resources(table_html)

        # Print the main table_html header
        print_election_type(headers, state)

        name, date, kind = extract_election_information_simple(headers)
        # extract_election_information_complex(body, info.meta)

        if name == f"{state} General Election" or name == f"{state} Primary Election":
            print(f"\n - {date} : {kind} - {name}\n")
            extract_election_information_complex(body, info.meta, state)


def extract_table_resources(table_html):
    info = Info()
    count = 0

    # Get Table Heads
    headers = table_html.select("thead tr")
    body = []

    for row in table_html.select("tr"):

        if row.select("td[class='note']") and row.text.strip() != '':
            info.note.raw = row
            info.note.text = row.get_text()
        elif not row.th:
            body.append(row)
            count += 1
        else:
            # logging.warning(f"Issue with table. Not Table Header (th). Not Table Data Note (td[class='note']): {row}")
            pass

    info.meta.column_count = int(headers[0].th['colspan'])
    info.meta.row_count = count

    return headers, body, info


def extract_election_information_simple(headers):
    date_length = 16
    ignored_phrase_length = 9
    buffer = 0

    election_string = headers[0].select("h4")[0].get_text()

    date = parse(election_string[-date_length:])

    if date.day < 10:
        buffer = 1

    election_name = election_string[0:buffer - (date_length + ignored_phrase_length)]
    election_type = determine_election_type(election_name)
    election_date = date.strftime('%a %b %d')

    return election_name, election_date, election_type


def extract_election_information_complex(body_rows: List[Tag], info: Meta, state):
    # early_registration = body_rows[4]
    # absentee_voting = body_rows[3]
    #
    # titles = (early_registration.h4.get_text(), absentee_voting.h4.get_text())
    # dates = (early_registration.select('td')[1].get_text().strip(), absentee_voting.select('td')[1].get_text().strip())
    #
    # for title, date in zip(titles, dates):
    #     if date == "none on record":
    #         date = ""
    #
    #     if date == "":
    #         print(f"{title:>25}\t.\t.")
    #     else:
    #         d = date.split(" - ")
    #
    #         if len(d) == 0:
    #             print(f"{title:>25}\t.\t. 0")
    #         elif len(d) == 1:
    #             try:
    #                 d1 = parse(d[0]).strftime('%a %b %d')
    #             except:
    #                 d1 = "error"
    #
    #             print(f"{title:>25}\t{d1}\t. 1")
    #         else:
    #
    #             try:
    #                 d1 = parse(d[0]).strftime('%a %b %d')
    #             except:
    #                 d1 = "error"
    #
    #             try:
    #                 d2 = parse(d[1]).strftime('%a %b %d')
    #             except:
    #                 d2 = "error"
    #
    #             print(f"{title:>25}\t{d1}\t{d2}")
    for row in body_rows:

        data = list(zip(row.select("td"), range(info.column_count)))
        events = [item.get_text() for item, position in data if position == 0]
        dates = [item for item, position in data if position == 1]

        for event, date in zip(events, dates):

            if event != "In-Person Absentee Voting" and event != "Early Voting":
                continue

            items = date.select('li')

            date = date.get_text().strip()
            if date == "none on record":
                date = ""

            if date != "":
                d = date.split(" - ")
                d1 = ""
                d2 = ""

                if len(d) == 1:
                    try:
                        d1 = parse(d[0]).strftime('%a %b %d')
                    except:
                        d1 = ""

                else:

                    try:
                        d1 = parse(d[0]).strftime('%a %b %d')
                    except:
                        d1 = ""

                    try:
                        d2 = parse(d[1]).strftime('%a %b %d')
                    except:
                        d2 = ""

                if len(items) >= 1:
                    print(f"\t - {event:<25}")
                    print()
                else:
                    print(f"\t - {event:<25}\t\t{d1}\t{d2}")

        # # For multiple items in a single cell
        # for number, item in enumerate(items):
        #
        #     if item.strong:
        #         full_text = item.get_text().strip()
        #         event_type = item.select("strong")[0].get_text().strip()
        #
        #         type_date = full_text.replace(event_type, "").strip()
        #     else:
        #         event_type = "* * * * * * * * * * * * * * * *"
        #         type_date = item.get_text().strip()
        #
        #     print(f"\t\t - {event_type:<35} :: {type_date}")
        #     if number + 1 == len(items):
        #         print()


def determine_election_type(election_name):
    if "Special" in election_name:
        election_type = "Special"
        if "Primary" in election_name:
            election_type += " P"
        elif "General" in election_name and "General Assembly" not in election_name:
            election_type += " G"
        else:
            election_type += " E"  # Election
    elif "Nominating" in election_name:
        election_type = "Nominate "
    elif "Runoff" in election_name:
        election_type = "Runoff"

        if "Primary" in election_name:
            election_type += " P "
        else:
            election_type += " G "

    elif "Primary" in election_name:
        election_type = "Primary  "
    elif "General" in election_name:
        election_type = "General  "
    else:
        election_type = "         "
    return election_type


def print_election_type(headers, state):
    if len(headers) > 1:
        print("--------------------------")
        print(state)
        print(headers.pop(0).select("h4")[0].get_text())
        print("--------------------------")


# i = 0
for state_abbr, state_name in states:
    # i += 1
    url = f"https://www.usvotefoundation.org/vote/us/state-voting-information/{state_abbr}"

    page = requests.get(url)
    html = page.text.replace("\n", "")
    soup = BeautifulSoup(html, 'html.parser')

    accordion = soup.select('div#accordion div.panel')

    panel_titles = accordion[0].select("h4.panel-title")
    # print_html(panel_titles)

    panel_tables = accordion[0].select("table")
    print_tables(panel_tables, state_name)

    # if i == 2:
    #     break
