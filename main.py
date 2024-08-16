from wallet import Wallet


def main():
    wallet = Wallet()

    while True:
        print("\n1. Balans")
        print("2. Daromad qo'shish")
        print("3. Harajat qo'shish")
        print("4. Hisobotni tahrirlash")
        print("5. Hisobot bo'yicha qidiruv")
        print("6. Chiqish")

        choice = input("\nVariant tanlang: ")

        if choice == '1':
            wallet.show_balance()

        elif choice == '2':
            print("Daromad qo'shish\n")
            amount = float(input("Miqdorni kiriting: "))
            description = input("Ma'lumot qoldiring: ")
            wallet.add_data('income', amount, description)

        elif choice == '3':
            print("Harajat qo'shish\n")
            amount = float(input("Miqdorni kiriting: "))
            description = input("Ma'lumot qoldiring: ")
            wallet.add_data('expense', amount, description)

        elif choice == '4':
            search = input("Tahrirlash uchun qiymat kiriting: ")
            wallet.edit_data(search)

        elif choice == '5':
            search_term = input("Qidiruv: ")
            wallet.search_informations(search_term)

        elif choice == '6':
            break
        else:
            print("Noto'g'ri tanlov, iltimos qaytadan urinib ko'ring.")


if __name__ == "__main__":
    main()
