import unittest
from unittest.mock import MagicMock

from bs4 import BeautifulSoup

from src.authors_count import (
    get_block_elements,
    get_authors,
    count_authors,
    get_author_usage,
)


class TestYourModule(unittest.TestCase):

    def test_get_author_usage(self):
        # Mock the search_conference, get_year_element, and get_contents_link functions
        search_conference = MagicMock(return_value='<html>Mocked conference page</html>')
        get_year_element = MagicMock(return_value=BeautifulSoup('<div>Mocked year element</div>', "html.parser"))
        get_contents_link = MagicMock(return_value='<div>Mocked contents page</div>')
        get_block_elements = MagicMock(return_value=[
            BeautifulSoup('<span itemprop="author"><span itemprop="name">Author 1</span></span>', "html.parser"),
            BeautifulSoup('<span itemprop="author"><span itemprop="name">Author 2</span></span>', "html.parser"),
        ])

        driver = MagicMock()
        driver.page_source = '<html>Mocked search page</html>'

        with unittest.mock.patch('src.authors_count.search_conference', search_conference):
            with unittest.mock.patch('src.authors_count.get_year_element', get_year_element):
                with unittest.mock.patch('src.authors_count.get_contents_link', get_contents_link):
                    with unittest.mock.patch('src.authors_count.get_block_elements', get_block_elements):
                        result = get_author_usage(driver, '2020', '2023', 'Conference Title')
                        self.assertCountEqual(result, [('Author 1', 4), ('Author 2', 4)])

    def test_get_block_elements(self):
        # Mock the page source
        page_source = '<div><cite class="data tts-content"></cite><cite class="data tts-content"></cite></div>'
        driver = MagicMock()
        driver.page_source = page_source

        # Test the function
        result = get_block_elements(driver.page_source)
        self.assertEqual(len(result), 1)

    def test_get_authors(self):
        # Mock the block elements
        block_elements = [
            BeautifulSoup('<span itemprop="author"><span itemprop="name">Author 1</span></span>', "html.parser"),
            BeautifulSoup('<span itemprop="author"><span itemprop="name">Author 2</span></span>', "html.parser"),
        ]

        # Test the function
        result = get_authors(block_elements)
        self.assertEqual(result, [['Author 1'], ['Author 2']])

    def test_count_authors(self):
        # Mock the author list
        author_list = [['Author 1', 'Author 2'], ['Author 1']]

        # Test the function
        result = count_authors(author_list)
        self.assertEqual(result, [('Author 1', 2), ('Author 2', 1)])


if __name__ == '__main__':
    unittest.main()
