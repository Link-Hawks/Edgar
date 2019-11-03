
from helpers.crawlers.crawler import Crawler

class NoticiasCrawler(Crawler):
    def buscar(self):
        self.acessar("https://g1.globo.com/")
        noticias = {}
        noticias["conteudos"] = self.encontrar_elementos_classe("feed-post-link")
        noticias["titulos"] = self.encontrar_elementos_classe("feed-post-header-chapeu")
        return noticias