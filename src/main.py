from scraper_pack.ExportadorExcel import ExportadorExcel
from scraper_pack.ReclameAquiScraper import ReclameAquiScraper


def main():
    scraper = ReclameAquiScraper()
    dados = scraper.scrape("Casa de Aposta")
    print(dados)
    exportador = ExportadorExcel()
    exportador.exportar(dados)
    
if __name__ == "__main__":
    main()
