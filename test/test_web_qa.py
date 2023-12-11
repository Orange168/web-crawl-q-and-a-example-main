import unittest
from unittest.mock import patch, MagicMock

from src.web_qa import get_hyperlinks, get_domain_hyperlinks, crawl, remove_newlines, split_into_many, create_context, answer_question

# Mocking external dependencies, if any, is crucial for unit testing
# For instance, if `crawl` function makes HTTP requests, those should be mocked

class TestWebQA(unittest.TestCase):
    # Each function in web-qa.py will have corresponding test methods

    @patch('web_qa.requests.get')
    def test_get_hyperlinks2(self, mock_get):
        # Set up the mock to return a predefined HTML content
        mock_get.return_value.ok = True
        mock_get.return_value.text = '<a href="https://example.com">Example</a>'

        result = get_hyperlinks("https://dummyurl.com")
        self.assertIn("https://example.com", result)

    def test_get_hyperlinks(self):
        # This test will ensure get_hyperlinks returns correct links
         # Mock HTML content with hyperlinks
        mock_html = """
        <html>
            <body>
                <a href="http://link1.com">Link 1</a>
                <a href="http://link2.com">Link 2</a>
            </body>
        </html>
        """

        # Expected list of hyperlinks
        expected_hyperlinks = ['http://link1.com', 'http://link2.com']

        # Mock the urlopen method to return the mock HTML
        mock_response = MagicMock()
        mock_response.info.return_value.get.return_value = "text/html"
        mock_response.read.return_value = mock_html.encode('utf-8')

        with patch('urllib.request.urlopen', return_value=mock_response):
            # Call the function
            result = get_hyperlinks("http://example.com")

        # Check if the result matches the expected output
        self.assertEqual(result, expected_hyperlinks)
        pass

    def test_get_domain_hyperlinks(self):
        # This test will ensure get_domain_hyperlinks filters links correctly
        local_domain = "www.localdomain.com"
        test_url = "https://www.localdomain.com/testpage"

        expected_links = {
            "https://www.localdomain.com/page1",
            "https://www.localdomain.com/page2",
            "https://www.localdomain.com/page3",
            "https://www.localdomain.com/page4",  # 假设端口不影响域的匹配
        }

        actual_links = set(get_domain_hyperlinks(local_domain, test_url))

        assert actual_links == expected_links, f"Failed, expected {expected_links} but got {actual_links}"
        pass

    # Additional test methods will be added here

if __name__ == '__main__':
    unittest.main()
