import re


class TextUtils:
    @staticmethod
    def remove_blank_spaces(phrase):
        """
            - phrase: string que tera os espacos em branco seguidos removidos.
            - retorna: string contendo apenas espacos entre as palavras.
                Exemplo: entrada: '  foo   bar  ' saida: 'foo bar'.
        """
        phrase = phrase.strip()
        phrase = re.sub(' +', ' ', phrase)
        return phrase

    @staticmethod
    def remove_text_formatters(phrase):
        """
            - phrase: string que tera os formatadores de texto (\n, \r e \t) removidos.
            - retorna: string sem formatadores de texto.
                Exemplo: entrada: 'foo\nbar' saida: 'foo bar'.
        """
        phrase = re.sub('\n+', ' ', phrase)
        phrase = re.sub('\r+', ' ', phrase)
        phrase = re.sub('\t+', ' ', phrase)
        return phrase

    @staticmethod
    def remove_term(phrase, term_to_remove):
        """
            - phrase: string que tera todos os termos removidos.
            - term_to_remove: string que contem o termo a ser removido.
            - retorna: string sem o termo.
                Exemplo: entrada: phrase='foo bar', term_to_remove='bar' saida: 'foo '.
        """
        phrase = re.sub(f'{term_to_remove}+', '', phrase)
        return phrase
