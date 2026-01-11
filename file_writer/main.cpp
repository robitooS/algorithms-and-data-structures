#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// definindo alias para char (0-255) como byte pq nao tem nativo
typedef unsigned char byte_8;

void read(string filename, byte_8 key) {
    ifstream file(filename, ios::binary);
    
    if (!file) {
        cerr << "O arquivo não foi encontrado" << endl;
        return;
    }

    byte_8 header;
    file.read(reinterpret_cast<char*>(&header), 1); // Vai ler o primeiro byte e atribuir a header
    if (header != 0xFF) {
        cerr << "O arquivo foi corrompido" << endl;
        return;
    }

    byte_8 size;
    file.read(reinterpret_cast<char*>(&size), 1);
    cout << "Tamanho da mensagem: " << int(size) << endl;

    string content_total;
    byte_8 checksum = 0;
    for (int i = 0; i < size; i++) {
        byte_8 content;
        file.read(reinterpret_cast<char*>(&content), 1);
        byte_8 uncrypted = content ^ key;

        checksum = checksum ^ uncrypted;
        content_total += uncrypted;
    }

    if (checksum == file.get()) {
        cout << "Contéudo do arquivo: " << string(content_total) << endl;
        return;
    }

    cerr << "O arquivo foi alterado" << endl;
}

void write(string text, byte_8 key) {
    ofstream file("dados.dat", ios::binary);

    if (!file){
        cerr << "Não foi possível criar o arquivo" << endl;
        return;
    }

    cout << "Iniciando gravação no arquivo" << endl;
    byte_8 header = 0xFF;
    file.write(reinterpret_cast<char*>(&header), sizeof(header)); // Vai fazer o casting para char* o ponteiro de unsigned char e escrever no arquivo o head

    byte_8 size = text.size();
    file.write(reinterpret_cast<char*>(&size), 1);

    byte_8 checksum = 0;
    for (int i = 0; i < text.size(); i++){
        // Para gravar cada caracter devemos encriptá-lo primeiro
        byte_8 encripted = text[i] ^ key;
        file.write(reinterpret_cast<char*>(&encripted), 1);
        checksum = checksum ^ encripted;
    }
    file.write(reinterpret_cast<char*>(&checksum), 1);
}

int main(int argc, char const *argv[])
{
    write("Hello World!", 0x55);
    read("dados.dat", 0x55);
    return 0;
}
