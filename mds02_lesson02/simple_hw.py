def main():
    while True:
        try:
            text = input('Введіть вираз (або "exit" для виходу): ')
            if text.lower() == 'exit':
                print("Вихід із програми.")
                break
            result = eval(text)
            print(result)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
