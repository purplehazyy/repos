def konvertuvaty_u_grivni():
    kursy_do_uah = {
        'USD': 41.91,
        'EUR': 47.78,
        'GBP': 55.77
        
    }

    print("Конвертер у гривні")
    print("Доступні валюти для конвертації:", ", ".join(kursy_do_uah.keys()))

    z_vid_valiuty = input("Яку валюту конвертуємо в гривні? ").upper()

    if z_vid_valiuty not in kursy_do_uah:
        print("Помилка: валюта недоступна.")
        return

    try:
        suma = float(input("Скільки конвертувати? "))
    except ValueError:
        print("Помилка: введіть число.")
        return

    rezultat = suma * kursy_do_uah[z_vid_valiuty]
    print(f"{suma} {z_vid_valiuty} = {round(rezultat, 2)} UAH")

konvertuvaty_u_grivni()