# Import external modules.
from bs4 import BeautifulSoup


def run_main():
    with open('website.html', 'r') as a_html_file:
        a_html_file_contents = a_html_file.read()
    a_soup = BeautifulSoup(a_html_file_contents, 'html.parser')
    print(a_soup.title)
    print(a_soup.title.name)
    print(a_soup.title.string)
    print(a_soup.prettify())
    print(a_soup.a)
    print(a_soup.li)
    all_anchor_tags_list = a_soup.find_all(name='a')
    print(all_anchor_tags_list)
    for a_tag in all_anchor_tags_list:
        print(a_tag.getText())
        print(a_tag.get('href'))
    heading = a_soup.find(name='h1', id='name')
    print(heading)
    section_heading = a_soup.find(name='h3', class_='heading')
    print(section_heading.getText())
    # Retrieve the company url by knowing that the anchor tag sits inside a paragraph anchor tag
    # (father and son relation)
    company_url = a_soup.select_one(selector='p a')
    print(company_url)
    # The #name refers to id 'name' inside the tag.
    site_owner = a_soup.select_one(selector='#name')
    print(site_owner)
    # The .heading refers to class 'heading' inside the tag.
    heading_list = a_soup.select(selector='.heading')
    print(heading_list)
    return


if __name__ == '__main__':
    run_main()
