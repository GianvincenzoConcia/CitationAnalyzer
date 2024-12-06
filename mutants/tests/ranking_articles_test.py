import unittest
from unittest.mock import patch, MagicMock

from flask import Flask

from src.ranking_articles import *

class TestRankingArticles(unittest.TestCase):

    def test_init_driver(self):
        result = init_driver()
        self.assertIsNotNone(result)

    def setUp(self):
        self.app = Flask(__name__)
        setup_classifica_routes(self.app)
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    @patch('src.ranking_articles.init_driver')
    def test_search_conference_found(self, mock_init_driver):
        # Testa il caso in cui la conferenza è trovata
        mock_driver = mock_init_driver.return_value
        mock_driver.page_source = '<html>Mocked Page Source</html>'

        result = search_conference('ConferenceTitle', mock_driver)
        self.assertEqual(result, '<html>Mocked Page Source</html>')

    @patch('src.ranking_articles.init_driver')
    def test_search_conference_not_found(self, mock_init_driver):
        # Testa il caso in cui la conferenza non è trovata
        mock_driver = mock_init_driver.return_value
        mock_driver.page_source = None  # Imposta page_source su None

        result = search_conference('NonExistentConference', mock_driver)
        self.assertIsNone(result)

    @patch('src.ranking_articles.flash')
    @patch('src.ranking_articles.WebDriverWait')
    def test_search_conference_not_found(self, mock_wait, mock_flash):
        # Configura il mock per simulare un Timeout durante la chiamata a WebDriverWait
        mock_wait.side_effect = TimeoutException("Test Timeout")

        # Configura il mock per simulare l'assenza di 'toc-link' e la conferenza stessa
        mock_driver = MagicMock()
        mock_driver.page_source = '<html>Mocked Page Source</html>'
        mock_driver.find_element.side_effect = NoSuchElementException("Element not found")

        # Esegui la funzione search_conference
        result = search_conference('Test Conference', mock_driver)

        # Verifica che la funzione ritorni None a causa del TimeoutException simulato
        self.assertIsNone(result)

        # Verifica che flash sia stato chiamato con il messaggio di errore appropriato
        mock_flash.assert_called_with("Conferenza Test Conference non trovata", "error")

        # Verifica che WebDriverWait sia stato chiamato con i parametri corretti
        mock_wait.assert_called_once_with(mock_driver, 10)
        mock_driver.get.assert_called_once_with('https://dblp.org/search?q=Test Conference')

        # Verifica che find_element sia stato chiamato per cercare 'toc-link'
        mock_driver.find_element.assert_called_once_with('class name','toc-link')


    def test_get_year_element(self):
        # Testa la funzione get_year_element
        soup_mock = MagicMock()
        soup_mock.find.return_value = MagicMock()

        result = get_year_element(soup_mock, '2022')
        self.assertIsNotNone(result)

    @patch('src.ranking_articles.flash')
    def test_get_year_element_not_found(self, mock_flash):
        # Testa la funzione get_year_element quando l'elemento dell'anno non è trovato
        soup_mock = MagicMock()
        soup_mock.find.return_value = None

        result = get_year_element(soup_mock, '2022')

        mock_flash.assert_called_with(f"Anno della conferenza 2022 non trovato.", 'error')
        self.assertIsNone(result)

    def test_get_contents_link(self):
        # Testa la funzione get_contents_link
        driver_mock = MagicMock()
        driver_mock.page_source = "<html><body>Mock Page Source</body></html>"
        year_element_mock = MagicMock()
        year_element_mock.find_next.return_value = MagicMock()

        result = get_contents_link(year_element_mock, driver_mock)
        self.assertIsNotNone(result)

    @patch('src.ranking_articles.flash')
    def test_get_contents_link_not_found(self, mock_flash):
        # Testa la funzione get_contents_link quando la pagina dei contenuti non è trovata
        year_element_mock = MagicMock()
        year_element_mock.find_next.return_value = None
        driver_mock = MagicMock()

        result = get_contents_link(year_element_mock, driver_mock)

        mock_flash.assert_called_with("Nessun articolo trovato", 'error')
        self.assertIsNone(result)

    @patch('src.ranking_articles.flash')
    def test_get_contents_link_exception(self, mock_flash):
        # Testa la funzione get_contents_link quando driver.get solleva un'eccezione
        year_element_mock = MagicMock()
        year_element_mock.find_next.return_value = MagicMock()
        driver_mock = MagicMock()
        driver_mock.get.side_effect = TimeoutException("Timeout during page load")

        result = get_contents_link(year_element_mock, driver_mock)

        mock_flash.assert_called_with("Timeout durante il caricamento della pagina dei contenuti", 'error')
        self.assertIsNone(result)

    def test_get_block_elements(self):
        # Testa la funzione get_block_elements
        page_source = "<html><body><cite class='data tts-content'></cite></body></html>"
        block_elements = get_block_elements(page_source)
        self.assertIsNotNone(block_elements)
        self.assertEqual(len(block_elements), 1)

    def test_get_article_data_list(self):
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

    # @patch('requests.get')
    # def test_get_citations_success(self, mock_requests_get):
    #     # Configura il mock della richiesta API di successo
    #     mock_response = MagicMock()
    #     mock_response.json.return_value = {
    #         'search-results': {
    #             'entry': [{'citedby-count': 10}]
    #         }
    #     }
    #     mock_requests_get.return_value = mock_response

    #     # Chiamata alla funzione get_citations
    #     result = get_citations('Test Article Title')

    #     # Verifica che la chiamata API sia stata eseguita con l'URL corretto
    #     mock_requests_get.assert_called_with(
    #         f'https://api.elsevier.com/content/search/scopus?query=TITLE("Test Article Title")&apiKey={SCOPUS_API_KEY}')

    #     # Verifica che il risultato della funzione sia corretto
    #     self.assertEqual(result, 10)

    # @patch('requests.get')
    # def test_get_citations_failure(self, mock_requests_get):
    #     # Configura il mock della richiesta API con errore
    #     mock_requests_get.side_effect = Exception('Test API Error')

    #     # Chiamata alla funzione get_citations
    #     result = get_citations('Test Article Title')

    #     # Verifica che la chiamata API sia stata eseguita con l'URL corretto
    #     mock_requests_get.assert_called_with(
    #         f'https://api.elsevier.com/content/search/scopus?query=TITLE("Test Article Title")&apiKey={SCOPUS_API_KEY}')

    #     # Verifica che il risultato della funzione sia 0 in caso di errore
    #     self.assertEqual(result, 0)
