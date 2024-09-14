# Today i am building number exploration game for a friend who like to  explore number tools
## steps to make exporation game  
  * first we will ask the friend to Enter his name
  * after that we will ask the user to enter his three favorite numbers
  * we will store the user's favorite number in a list
  * we will loop through the list to tell the user number is odd or even
  * and we will  also print the each numbr and it's square
  * finally will calculate the sum of number and check if it's  a prime number
# CODE
 ```python
 def is_prime(num):
    if num <= 1:
        return False
    elif num == 2 : 
        return True
    elif num % 2 == 0:
        return False
    for i in range(3, int(num **0.5) +1, 2):
        if num % i ==0:
            return False
    return True


def main():


    name: str = input("Enter your name: ")
    numbers: list[int] = []
    first_favorite_number: int =int (input("Enter your first favorite number: "))
    numbers.append(first_favorite_number)
    second_favorite_number: int = int(input("Enter your second favourite number:"))

    numbers.append(second_favorite_number)
    third_favorite_number : int =int (input("Enter your third favorite number: "))
    numbers.append(third_favorite_number)
    print(f"Hello,{name}! Let,s explore your favorite numbers:" )
    list_tuple: list[tuple[int, int]] =[]
    for num in numbers:
        if num % 2 == 0:
            print(f'the number {num} is an even.')
            list_tuple.append((num, num **2))
        else:
            print(f'the number {num} is odd.')
            list_tuple.append ((num, num**2))

    for num, num_square in list_tuple:
        print(f"number {num} and its square is {num_square}.")

    total_sum: int = sum(numbers)
    print(f"The sum of your favorite number is : {total_sum}.")
    
    if is_prime(total_sum):
        print(f"Amazing the {total_sum} is a prime number!")
    else: 
        print(f"the {total_sum} is not a prime number but its still a special number")

if __name__ == "__main__":
    main()
    ``` 