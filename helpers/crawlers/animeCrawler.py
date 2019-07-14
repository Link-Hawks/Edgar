from helpers.crawlers.crawler import Crawler
from os import system

class AnimeCrawler(Crawler):

    def __init__(self, anime, cli=True, host='https://horriblesubs.info/shows/'):
        super().__init__(cli)
        self.anime = anime
        self.cli = cli
        self.host = host

    def baixar(self, qualidade):
        self.acessar(self.host)
        self.encontrar_link_texto(self.anime).click()
        elementoEpisodio = self.encontrar_filho('hs-shows', 'rls-info-container').click()
        elementoDownload = self.encontrar_classe('link-'+qualidade, elementoEpisodio)
        magnet = self.encontrar_torrent_magnet(elementoDownload)
        self.adicionar_torrent(magnet)
        self.encerrar()
        
    def assistir(self, anime_path):
        system('mpc ', anime_path)
    


