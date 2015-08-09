import os
import unittest
from eventlet import GreenPool
from eventlet.green.urllib.request import urlopen
from lxml import html
from urllib.parse import urljoin


class SiteTestCase(unittest.TestCase):
    
    def local_url(self, url):
        return urljoin('http://localhost:8000', url.replace('.\\', '').replace('\\', '/'))
    
    def assert_status_code(self, url, code=200):
        with urlopen(url) as resp:
            self.assertEqual(resp.getcode(), code, url)
        return True
    
    def get_and_assert_status_code(self, url, code=200):
        with urlopen(url) as resp:
            self.assertEqual(resp.getcode(), code, url)
            data = resp.read()
        return data
        
    @classmethod
    def setUpClass(cls):
        os.chdir('output')
        cls.pool = GreenPool()
    
    def test_no_broken_links(self):
        def get_tree(page):
            page_links = set()
            data = self.get_and_assert_status_code(self.local_url(page))
            tree = html.fromstring(data)
            for result in tree.iterlinks():
                page_links.add(self.local_url(result[2]))
            return page_links
        pages = []
        links = set()
        for result in os.walk('.'):
            pages.extend([os.path.join(result[0], x) for x in result[2] if x.endswith('.html')])
        all_link_sets = self.pool.imap(get_tree, pages)
        for link_set in all_link_sets:
            links.update(link_set)
        feedback = self.pool.imap(self.assert_status_code, links)
        self.assertGreater(len([x for x in feedback if x]), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)