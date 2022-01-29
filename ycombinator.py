# Import external modules.
from bs4 import BeautifulSoup
import requests as req


def run_main():
    yc_response = req.get(url='https://news.ycombinator.com/newest')
    yc_html_page_str = yc_response.text
    yc_soup = BeautifulSoup(markup=yc_html_page_str, features='html.parser')
    a_article_tag_list = yc_soup.find_all(name='a', class_='titlelink')
    a_article_tag_text_list = [item.getText() for item in a_article_tag_list]
    a_article_tag_link_list = [item.get(key='href') for item in a_article_tag_list]
    a_article_tag_list = yc_soup.find_all(name='span', class_='score')
    a_article_tag_upvote_list = [int(item.getText().split(' ')[0]) for item in a_article_tag_list]
    # Get the first highest score.
    highest_score_value = max(a_article_tag_upvote_list)
    highest_score_index = a_article_tag_upvote_list.index(highest_score_value)
    # Order the list by score value.
    a_article_index_mtx = list(
        zip(a_article_tag_upvote_list, a_article_tag_text_list, a_article_tag_link_list)
    )
    a_article_index_mtx.sort(reverse=True)
    # Print the most upvote links.
    print(a_article_index_mtx[:3])
    for a_vote, a_title, a_link in a_article_index_mtx:
        if 'python' in a_title or 'Python' in a_title:
            print(f"Upvote: {a_vote}, Title: {a_title}, Link: {a_link}")
    return


if __name__ == '__main__':
    run_main()
