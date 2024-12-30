def main():
    print("TinyTroupe запускается...")
    # Основная логика программы
    from tinytroupe.examples import create_lisa_the_data_scientist

    lisa = create_lisa_the_data_scientist()
    print(f"Симуляция началась с {lisa.name}")

if __name__ == "__main__":
    main()
