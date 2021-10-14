class house:
    doors: int
    color: str

    def __init__(self, doors: int,color: str) -> None:
        self.doors= doors
        self.color= color

    def change_color(self, new_color: str) -> None:
        if new_color == self.color:
            raise ValueError("Ten sam kolor")

        self.color = new_color

    def __len__(self)-> int:
        return 8

    def __str__(self)-> str:
        return f'liczba drzwi:{self.doors}'
        f'Kolor:'{self.color}'

green_house: house = house(doors=15, color="green")
print(green_house.doors)
print(len(green_house))
print(green_house)