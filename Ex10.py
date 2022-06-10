
class Test:
    def test_check(self):
        print("Введите в консоли любую фразу короче 15 символов")
        phrase = input("")
        print(f"Длина введённой фразы: {len(phrase)}")
        assert len(phrase) <= 15, f"Фраза больше 15 символов"
