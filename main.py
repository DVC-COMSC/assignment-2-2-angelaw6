def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    celsius = int(input("Enter a temperature in Celcius: "))
    fahrenheit = ((9 * celsius )/ 5) + 32

    print(f"Farenheit: {fahrenheit:.2f}" )
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
