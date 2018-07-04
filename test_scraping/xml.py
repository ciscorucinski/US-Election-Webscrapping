import bs4 as bs

with open('/home/ciscorucinski/PycharmProjects/Web Scraping/resources/governors.xml') as f:
    raw_xml = f.read()

    soup = bs.BeautifulSoup(raw_xml, 'xml')

    # last_names = [element.get_text().strip() for element in senators_soup.find_all("last_name")]
    # first_names = [element.get_text().strip() for element in senators_soup.find_all("first_name")]
    # party = [element.get_text().strip() for element in senators_soup.find_all("party")]
    # state = [element.get_text().strip() for element in senators_soup.find_all("state")]
    # address = [element.get_text().strip() for element in senators_soup.find_all("address")]
    # phone = [element.get_text().strip() for element in senators_soup.find_all("phone")]
    # email = [element.get_text().strip() for element in senators_soup.find_all("email")]
    # website = [element.get_text().strip() for element in senators_soup.find_all("website")]
    # class_level = [element.get_text().strip() for element in senators_soup.find_all("class")]
    count = len(soup.find_all("councilor"))

    state_name = [element.get_text().strip() for element in soup.find_all("state_name")]
    state_name_slug = [element.get_text().strip() for element in soup.find_all("state_name_slug")]
    state_code = [element.get_text().strip() for element in soup.find_all("state_code")]
    state_code_slug = [element.get_text().strip() for element in soup.find_all("state_code_slug")]
    votesmart = [element.get_text().strip() for element in soup.find_all("votesmart")]
    title = [element.get_text().strip() for element in soup.find_all("title")]
    party = [element.get_text().strip() for element in soup.find_all("party")]
    name = [element.get_text().strip() for element in soup.find_all("name")]
    name_slug = [element.get_text().strip() for element in soup.find_all("name_slug")]
    first_name = [element.get_text().strip() for element in soup.find_all("first_name")]
    middle_name = [element.get_text().strip() for element in soup.find_all("middle_name")]
    last_name = [element.get_text().strip() for element in soup.find_all("last_name")]
    name_suffix = [element.get_text().strip() for element in soup.find_all("name_suffix")]
    goes_by = [element.get_text().strip() for element in soup.find_all("goes_by")]
    pronunciation = [element.get_text().strip() for element in soup.find_all("pronunciation")]
    gender = [element.get_text().strip() for element in soup.find_all("gender")]
    ethnicity = [element.get_text().strip() for element in soup.find_all("ethnicity")]
    religion = [element.get_text().strip() for element in soup.find_all("religion")]
    openly_lgbtq = [element.get_text().strip() for element in soup.find_all("openly_lgbtq")]
    date_of_birth = [element.get_text().strip() for element in soup.find_all("date_of_birth")]
    entered_office = [element.get_text().strip() for element in soup.find_all("entered_office")]
    term_end = [element.get_text().strip() for element in soup.find_all("term_end")]
    biography = [element.get_text().strip() for element in soup.find_all("biography")]
    phone = [element.get_text().strip() for element in soup.find_all("phone")]
    fax = [element.get_text().strip() for element in soup.find_all("fax")]
    latitude = [element.get_text().strip() for element in soup.find_all("latitude")]
    longitude = [element.get_text().strip() for element in soup.find_all("longitude")]
    address_complete = [element.get_text().strip() for element in soup.find_all("address_complete")]
    address_number = [element.get_text().strip() for element in soup.find_all("address_number")]
    address_prefix = [element.get_text().strip() for element in soup.find_all("address_prefix")]
    address_street = [element.get_text().strip() for element in soup.find_all("address_street")]
    address_sec_unit_type = [element.get_text().strip() for element in soup.find_all("address_sec_unit_type")]
    address_sec_unit_num = [element.get_text().strip() for element in soup.find_all("address_sec_unit_num")]
    address_city = [element.get_text().strip() for element in soup.find_all("address_city")]
    address_state = [element.get_text().strip() for element in soup.find_all("address_state")]
    address_zipcode = [element.get_text().strip() for element in soup.find_all("address_zipcode")]
    address_type = [element.get_text().strip() for element in soup.find_all("address_type")]
    website = [element.get_text().strip() for element in soup.find_all("website")]
    contact_page = [element.get_text().strip() for element in soup.find_all("contact_page")]
    facebook_url = [element.get_text().strip() for element in soup.find_all("facebook_url")]
    twitter_handle = [element.get_text().strip() for element in soup.find_all("twitter_handle")]
    twitter_url = [element.get_text().strip() for element in soup.find_all("twitter_url")]
    photo_url = [element.get_text().strip() for element in soup.find_all("photo_url")]

    print(f"state_name\tstate_name_slug\tstate_code\tstate_code_slug\tvotesmart\ttitle\tparty\tname\tname_slug\tfirst_name\tmiddle_name\tlast_name\tname_suffix\tgoes_by\tpronunciation\tgender\tethnicity\treligion\topenly_lgbtq\tdate_of_birth\tentered_office\tterm_end\tbiography\tphone\tfax\tlatitude\tlongitude\taddress_complete\taddress_number\taddress_prefix\taddress_street\taddress_sec_unit_type\taddress_sec_unit_num\taddress_city\taddress_state\taddress_zipcode\taddress_type\twebsite\tcontact_page\tfacebook_url\ttwitter_handle\ttwitter_url\tphoto_url")
    for i in range(count):

        print(f"{state_name[i]}\t{state_name_slug[i]}\t{state_code[i]}\t{state_code_slug[i]}\t{votesmart[i]}\t{title[i]}\t{party[i]}\t{name[i]}\t{name_slug[i]}\t{first_name[i]}\t{middle_name[i]}\t{last_name[i]}\t{name_suffix[i]}\t{goes_by[i]}\t{pronunciation[i]}\t{gender[i]}\t{ethnicity[i]}\t{religion[i]}\t{openly_lgbtq[i]}\t{date_of_birth[i]}\t{entered_office[i]}\t{term_end[i]}\t{biography[i]}\t{phone[i]}\t{fax[i]}\t{latitude[i]}\t{longitude[i]}\t{address_complete[i]}\t{address_number[i]}\t{address_prefix[i]}\t{address_street[i]}\t{address_sec_unit_type[i]}\t{address_sec_unit_num[i]}\t{address_city[i]}\t{address_state[i]}\t{address_zipcode[i]}\t{address_type[i]}\t{website[i]}\t{contact_page[i]}\t{facebook_url[i]}\t{twitter_handle[i]}\t{twitter_url[i]}\t{photo_url[i]}")
