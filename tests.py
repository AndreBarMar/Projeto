import unittest
import hashlib
import os
from utils import calculate_md5

class TestMD5Generation(unittest.TestCase):

    def setUp(self):
        # Cria um arquivo temporário para teste
        with open("test_file.txt", "w") as f:
            f.write("Este é um arquivo de teste.")

    def test_md5_generation(self):
        # Gera o MD5 do arquivo criado
        md5_result = calculate_md5("test_file.txt")
        
        # Calcula o MD5 esperado
        expected_md5 = hashlib.md5("Este é um arquivo de teste.".encode()).hexdigest()
        
        # Verifica se os MD5 são iguais
        self.assertEqual(md5_result, expected_md5)

    def tearDown(self):
        # Remove o arquivo temporário após o teste
        if os.path.exists("test_file.txt"):
            os.remove("test_file.txt")

if __name__ == "__main__":
    unittest.main()