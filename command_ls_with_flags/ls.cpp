#include <iostream>
#include <dirent.h>
#include <stdio.h>
#include <cstring>

int main(int argc, char const *argv[])
{
    bool mostrar_oculto = false;
    bool mostrar_completo = false;

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-a") == 0) {
            mostrar_oculto = true;
        }
        if (strcmp(argv[i], "-l") == 0) {
            mostrar_completo = true;
        }
    }

    struct dirent *dp;
    DIR *dir = opendir(".");

    while (dp = readdir(dir)) {
        if (mostrar_completo && mostrar_oculto) {
            printf("%s - %lu - %d\n", dp->d_name, dp->d_ino, dp->d_reclen);

        } else if (mostrar_completo) {
            if (dp->d_name[0] == '.') {
                continue;
            }
            printf("%s - %lu - %d\n", dp->d_name, dp->d_ino, dp->d_reclen);
        } else if (mostrar_oculto) {
            std::cout << dp->d_name << std::endl;
        } else {
            if (dp->d_name[0] == '.') {
                continue;
            }
            std::cout << dp->d_name << std::endl;

        }
    }

    return 0;
}
