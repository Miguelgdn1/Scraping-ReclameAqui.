import pandas as pd

class ExportadorExcel:
    def exportar(self, dados, nome_arquivo='casas_de_aposta.xlsx'):
        df = pd.DataFrame.from_dict(dados, orient='index')
        df.to_excel('casas_de_aposta.xlsx')

