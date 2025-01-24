# importação de módulos
import warnings # módulo para manipulação de avisos

# desativando aviso de usuário
warnings.simplefilter(action='ignore', category=UserWarning)

class ExtractDataTxt:
    def __init__(self, raw_data_path: str) -> None:
        """
        Método construtor para extrair dados de um arquivo txt.

        Args:
            raw_data_path (str): Caminho do arquivo txt que contém os dados.
        """
        self.raw_data_path = raw_data_path

    def extract_file_data(self) -> list:
        """
        Método para extração dos dados de um arquivo txt.
        Este método lê um arquivo txt do caminho especificado e retorna uma lista 
        contendo os valores de cada linha do arquivo.

        Returns:
            list: Uma lista com os valores de cada linha do arquivo.
        """
        data = []
        with open(self.raw_data_path, 'r', encoding='iso-8859-1') as file:
            for line in file:
                data.append(line)
        return data