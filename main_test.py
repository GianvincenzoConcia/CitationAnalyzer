import unittest
from unittest.mock import MagicMock

from bs4 import BeautifulSoup

from main import app, search_conference, get_year_element, get_contents_link, get_block_elements, get_article_data_list, \
    get_citations


class TestWebApp(unittest.TestCase):

    def setUp(self):
        # Configura l'applicazione Flask per l'ambiente di test
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def test_index_route(self):
        # Testa la rotta index
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ricerca conferenza su DBLP', response.data)

    def test_search_route(self):
        # Testa la rotta di ricerca
        response = self.app.post('/search', data={'conference_title': 'TestConf', 'conference_year': '2022'})
        self.assertEqual(response.status_code, 302)  # Redirect dopo la ricerca

    def test_search_conference(self):
        # Testa la funzione di ricerca della conferenza
        driver_mock = MagicMock()
        driver_mock.page_source = "<html><body>Mock Page Source</body></html>"

        # Supponendo che 'TestConf' e '2022' siano parametri validi per il test
        result = search_conference('aaaaa', driver_mock)
        self.assertIsNotNone(result)

    def test_get_year_element(self):
        # Testa la funzione get_year_element
        soup_mock = MagicMock()
        soup_mock.find.return_value = MagicMock()

        result = get_year_element(soup_mock, '2022')
        self.assertIsNotNone(result)

    def test_get_contents_link(self):
        # Testa la funzione get_contents_link
        driver_mock = MagicMock()
        driver_mock.page_source = "<html><body>Mock Page Source</body></html>"
        year_element_mock = MagicMock()
        year_element_mock.find_next.return_value = MagicMock()

        result = get_contents_link(year_element_mock, driver_mock)
        self.assertIsNotNone(result)

    def test_get_block_elements(self):
        # Testa la funzione get_block_elements
        page_source = "<html><body><cite class='data tts-content'></cite></body></html>"
        block_elements = get_block_elements(page_source)
        self.assertIsNotNone(block_elements)
        self.assertEqual(len(block_elements), 1)

    def test_get_article_data_list(self):
        # Testa la funzione get_article_data_list
        block_elements = [
            MagicMock(find_all=lambda *args, **kwargs: [
                MagicMock(find=lambda *args, **kwargs: BeautifulSoup('<span itemprop="author">Author 1</span>',
                                                                     'html.parser')),
                MagicMock(find=lambda *args, **kwargs: BeautifulSoup('<span class="title">Article Title</span>',
                                                                     'html.parser')),
            ]),
        ]

        result = get_article_data_list(block_elements)
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], 'Article Title')
        self.assertEqual(result[0][1], ['Author 1'])

    # def test_get_citations(self):
    #     # Testa la funzione get_citations
    #     article_title = 'TestArticle'
    #     with requests_mock.Mocker() as m:
    #         # Configura il mock per rispondere alle richieste di Scopus
    #         m.get(f'https://api.elsevier.com/content/search/scopus?query=TITLE("{article_title}")&apiKey=ce1da58cc35b89014c26ff7de31cca85',
    #               json={'search-results': {'entry': [{'citedby-count': 5}]}})
    #         result = get_citations(article_title)
    #         self.assertEqual(result, 5)

# ... (altro codice)


if __name__ == '__main__':
    unittest.main()
