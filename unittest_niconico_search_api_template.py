import unittest
import requests

class TestNicoNicoSearch(unittest.TestCase):
    def test_niconico_search_good_request(self) -> None:
        response = requests.post("https://api.search.nicovideo.jp/api/v2/snapshot/video/contents/search",
        data={
            "q": "初音ミク",
            "targets": "title",
            "_sort": "-viewCounter",
            "_context": "Mac PC",
            "fields": "title,contentId",
            "_offset": "3",
            "_limit": "3"
        },
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac)"})
        self.assertEqual(response.status_code, 200)

    def test_niconico_search_bad_request(self) -> None:
        response = requests.post("https://api.search.nicovideo.jp/api/v2/snapshot/video/contents/search",
        data={
            "q": "初音ミク",
            "targets": "title",
            "_sort": "-viewCounter",
            "_context": "Mac PC",
            "fields": "title,contentId",
            "_offset": "3",
            "_limit": "invalid_input"
        },
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac)"})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
