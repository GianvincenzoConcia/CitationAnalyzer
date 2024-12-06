import unittest
from unittest.mock import MagicMock, patch

from bs4 import BeautifulSoup

from src.conf_hindex import (
    init_driver,
    get_conference_hindex,
    calcola_h_index,
    all_conference_index,
    get_year_element,
)


class TestConfHindex(unittest.TestCase):

    def test_init_driver(self):
        result = init_driver()
        self.assertIsNotNone(result)

    def test_calcola_h_index(self):
        citazioni_per_articolo = [10, 8, 5, 3, 3, 2, 1]
        result = calcola_h_index(citazioni_per_articolo)
        self.assertEqual(result, 3)
    
    # def test_get_conference_hindex(self):
    #     block_elements_list = [
    #         [
    #             BeautifulSoup('<span class="title">Article 1</span>', "html.parser"),
    #             BeautifulSoup('<span class="title">Article 2</span>', "html.parser"),
    #         ],
    #         [
    #             BeautifulSoup('<span class="title">Article 3</span>', "html.parser"),
    #         ],
    #     ]
    #     result = get_conference_hindex(block_elements_list)
    #     self.assertEqual(result, 0)
    
    def test_handles_empty_block_elements_list(self):   
        # Define an empty block elements list
        block_elements_list = []
    
        # Call the function under test
        hindex = get_conference_hindex(block_elements_list)
    
        # Assert the expected h-index for an empty list is 0
        assert hindex == 0

    def test_all_conference_index(self):
        driver = MagicMock()
        driver.page_source = '<html>Mocked search page</html>'

        result = all_conference_index(driver, '2020', '2022', ['Conference 1', 'Conference 2'])
        self.assertEqual(result, [('Conference 1', 0), ('Conference 2', 0)])

    def test_get_year_element(self):
        soup = BeautifulSoup('<span itemprop="datePublished">2022</span>', "html.parser")
        result = get_year_element(soup, 2022)
        self.assertIsNotNone(result)
