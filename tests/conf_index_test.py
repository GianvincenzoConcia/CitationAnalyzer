import unittest
from unittest.mock import MagicMock, patch

from bs4 import BeautifulSoup

from conf_hindex import (
    init_driver,
    get_conference_hindex,
    calcola_h_index,
    all_conference_index,
    get_year_element,
    setup_hindex_routes,
)


class TestYourModule(unittest.TestCase):

    def test_init_driver(self):
        result = init_driver()
        self.assertIsNotNone(result)

    def test_calcola_h_index(self):
        citazioni_per_articolo = [10, 8, 5, 3, 3, 2, 1]
        result = calcola_h_index(citazioni_per_articolo)
        self.assertEqual(result, 3)

    def test_get_conference_hindex(self):
        block_elements_list = [
            [
                BeautifulSoup('<span class="title">Article 1</span>', "html.parser"),
                BeautifulSoup('<span class="title">Article 2</span>', "html.parser"),
            ],
            [
                BeautifulSoup('<span class="title">Article 3</span>', "html.parser"),
            ],
        ]
        result = get_conference_hindex(block_elements_list)
        self.assertEqual(result, 0)

    @patch('conf_hindex.search_conference', return_value='<html>Mocked conference page</html>')
    @patch('conf_hindex.get_year_element', return_value=BeautifulSoup('<div>Mocked year element</div>', "html.parser"))
    @patch('conf_hindex.get_contents_link', return_value='<div>Mocked contents page</div>')
    def test_all_conference_index(self, mock_search_conference, mock_get_year_element, mock_get_contents_link):
        driver = MagicMock()
        driver.page_source = '<html>Mocked search page</html>'

        result = all_conference_index(driver, '2020', '2022', ['Conference 1', 'Conference 2'])
        self.assertEqual(result, [('Conference 1', 0), ('Conference 2', 0)])

    def test_get_year_element(self):
        soup = BeautifulSoup('<span itemprop="datePublished">2022</span>', "html.parser")
        result = get_year_element(soup, 2022)
        self.assertIsNotNone(result)

    # def test_setup_hindex_routes(self):
    #     app = MagicMock()
    #     setup_hindex_routes(app)
    #
    #     # Test route /search_hindex
    #     with app.test_request_context('/search_hindex', method='GET'):
    #         response = app.dispatch_request()
    #         self.assertIn(b'search_hindex', response.data)
    #
    #     # Test route /h_index
    #     with app.test_request_context('/h_index', method='POST', data={'start_year': '2020', 'end_year': '2022', 'conference_list': ['Conference 1']}):
    #         response = app.dispatch_request()
    #         self.assertIn(b'h_index', response.data)


if __name__ == '__main__':
    unittest.main()
