# Import external modules.
from bs4 import BeautifulSoup


def run_main():
    # Read the file contents (HTML).
    with open('website.html', 'r') as a_html_file:
        a_html_file_contents = a_html_file.read()
    # Create the soup object that holds all information about the HTML code.
    a_soup = BeautifulSoup(a_html_file_contents, 'html.parser')
    print(a_soup.prettify())
    # Get the HTML code with tag 'title'.
    print(f'1: {a_soup.title}')
    # Get the tag name, in this case 'title'.
    print(f'2: {a_soup.title.name}')
    # Get the text of the HTML code with tag 'title'.
    print(f'3: {a_soup.title.string}')
    # Print an indented version of the HTML code.
    print(f'4: {a_soup.prettify()}')
    # Get the HTML code of first occurrence of the 'a' tag.
    print(f'5: {a_soup.a}')
    # Get the HTML code of first occurrence of the 'li' tag.
    print(f'6: {a_soup.li}')
    # Get all the HTML code of all occurrences of the 'a' tags as a list.
    all_anchor_tags_list = a_soup.find_all(name='a')
    print(f'7: {all_anchor_tags_list}')
    # Iterate the list of all HTML code with tag 'a'.
    for a_tag in all_anchor_tags_list:
        # Get the text of a 'a' tag.
        print(f'8: {a_tag.getText()}')
        # Get the attribute value 'href' of the 'a' tag.
        print(f"8: {a_tag.get('href')}")
    # Get the first occurrence of HTML code with tag 'h1' and 'id' attribute 'name'.
    heading = a_soup.find(name='h1', id='name')
    print(f'10: {heading}')
    # Get the first occurrence of HTML code with tag 'h3' and 'class' 'heading'.
    section_heading = a_soup.find(name='h3', class_='heading')
    print(f'11: {section_heading.getText()}')
    # Retrieve the company url by knowing that the anchor tag sits inside a paragraph anchor tag
    # (father and son relation)
    company_url = a_soup.select_one(selector='p a')
    print(f'12: {company_url}')
    # The #name refers to id 'name' inside the tag.
    site_owner = a_soup.select_one(selector='#name')
    print(f'13: {site_owner}')
    # The .heading refers to class 'heading' inside the tag.
    heading_list = a_soup.select(selector='.heading')
    print(f'14: {heading_list}')
    return


if __name__ == '__main__':
    run_main()
