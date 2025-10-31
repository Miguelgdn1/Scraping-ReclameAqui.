from src.ExportadorExcel import ExportadorExcel
from src.ReclameAquiScraper import ReclameAquiScraper


def main():
    scraper = ReclameAquiScraper()
    dados = scraper.scrape("Casa de Aposta")
    print(dados)
    exportador = ExportadorExcel()
    exportador.exportar(dados)
    
if __name__ == "__main__":
    main()
