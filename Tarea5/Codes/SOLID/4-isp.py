class Printer:
    def print_document(self, document):
        pass


class Scanner:
    def scan_document(self):
        pass


class Photocopier:
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def copy_document(self):
        print("El documento ha sido copiado")


printer = Printer()
scanner = Scanner()
photocopier = Photocopier(printer, scanner)
photocopier.copy_document()
