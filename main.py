import sys

from replace import read_config, process_text


def main(config_file, text_file):
    """Главная функция которая запускает другие функции"""
    config = read_config(config_file)
    lines, replacements, results = process_text(text_file, config)
    for line in lines:
        for rep in replacements:
            if rep[1] in line:
                count = line.count(rep[1])
                print(f'Line: {line}, Replaced: {rep[0]} with {rep[1]}, Replacements: {count}')

    print(results)


# Вызываем main с аргументами, полученными из командной строки
# sys.argv[1] - путь к файлу конфигурации.
# sys.argv[2] - путь к текстовому файлу.
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Пожалуйста, предоставьте два аргумента: файл конфигурации и текстовый файл.")
    else:
        main(sys.argv[1], sys.argv[2])
