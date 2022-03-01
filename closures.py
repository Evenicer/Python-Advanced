def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "You can only use Strings"
        return string * n
    return repeater    

def make_division_by(n: int) -> int:
    def division(x: int) -> int:
        return x // n  
    return division      


def run():
    # repeat_5 = make_repeater_of(5)
    # print(repeat_5("Hola"))

    # repeat_10 = make_repeater_of(10)
    # print(repeat_10("Platzi"))
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_3 = make_division_by(5)
    print(division_by_3(100))

if __name__ == '__main__':
    run()    
