import unittest
from unittest.mock import MagicMock, patch

from bs4 import BeautifulSoup

from main import app, search_conference, get_year_element, get_contents_link, get_block_elements, get_article_data_list


class TestWebApp(unittest.TestCase):

    def setUp(self):
        # Configura l'applicazione Flask per l'ambiente di test
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.soup_mock = MagicMock()
        self.page_source = """
                    <html>
                        <body>
                            <cite class="data tts-content">
                                <span itemprop="author"><span itemprop="name">Author 1</span></span>
                                <span class="title">Article 1</span>
                            </cite>
                            <cite class="data tts-content">
                                <span itemprop="author"><span itemprop="name">Author 1</span></span>
                                <span itemprop="author"><span itemprop="name">Author 2</span></span>
                                <span class="title">Titolo esempio</span>
                            </cite>
                        </body>
                    </html>
                """

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


    @patch('main.BeautifulSoup')
    def test_get_block_elements(self, mock_beautifulsoup):
        # Configurare il mock di BeautifulSoup per restituire un risultato predefinito
        mock_beautifulsoup.return_value = self.soup_mock
        self.soup_mock.find_all.return_value = ['elemento1', 'elemento2']  # Puoi sostituire con i tuoi dati di esempio

        # Chiamare la funzione da testare
        result = get_block_elements('pagina_html_di_test')

        # Verificare che la funzione restituisca il risultato atteso
        self.assertEqual(result, ['elemento1', 'elemento2'])

    def test_get_article_data_list(self):
        block_elements = get_block_elements(self.page_source)
        result = get_article_data_list(block_elements)

        # Assicurati che il risultato sia una lista non vuota
        self.assertTrue(result)

        # Assicurati che il risultato sia una lista di tuple
        self.assertTrue(all(isinstance(item, tuple) for item in result))

        # Assicurati che ogni tupla abbia tre elementi
        self.assertTrue(all(len(item) == 3 for item in result))

        # Verifica la presenza della tupla desiderata con due autori
        expected_tuple = ("Titolo esempio", ["Author 1", "Author 2"], 0)
        self.assertIn(expected_tuple, result)


if __name__ == '__main__':
    unittest.main()
