def calculate_discount(price, discount_percent):
        """Calculate the final price after applying a discount if it's 20% or higher."""
            if discount_percent >= 20:
                    return price - (price * discount_percent / 100)
                        return price

                        def calculate_tax(price, tax_rate):
                            """Calculate the tax amount based on the given tax rate."""
                                return price * (tax_rate / 100)

                                def main():
                                    try:
                                            # Get user input
                                                    original_price = float(input("Enter the original price of the item: "))
                                                            discount_percentage = float(input("Enter the discount percentage: "))
                                                                    tax_rate = float(input("Enter the sales tax percentage: "))

                                                                            # Ensure input is valid
                                                                                    if original_price < 0 or discount_percentage < 0 or tax_rate < 0:
                                                                                                print("Price, discount percentage, and tax rate must be non-negative.")
                                                                                                            return

                                                                                                                    # Calculate discounted price
                                                                                                                            discounted_price = calculate_discount(original_price, discount_percentage)

                                                                                                                                    # Calculate tax on the discounted price
                                                                                                                                            tax_amount = calculate_tax(discounted_price, tax_rate)

                                                                                                                                                    # Calculate final price
                                                                                                                                                            final_price = discounted_price + tax_amount

                                                                                                                                                                    # Print the breakdown
                                                                                                                                                                            print("\n--- Price Breakdown ---")
                                                                                                                                                                                    print(f"Original Price: ${original_price:.2f}")
                                                                                                                                                                                            if discount_percentage >= 20:
                                                                                                                                                                                                        print(f"Discount Applied: {discount_percentage}%")
                                                                                                                                                                                                                    print(f"Discounted Price: ${discounted_price:.2f}")
                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                        print("No discount applied.")
                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                        print(f"Tax Amount ({tax_rate}%): ${tax_amount:.2f}")
                                                                                                                                                                                                                                                                print(f"Final Price After Tax: ${final_price:.2f}")

                                                                                                                                                                                                                                                                    except ValueError:
                                                                                                                                                                                                                                                                            print("Invalid input. Please enter numeric values for price, discount, and tax rate.")

                                                                                                                                                                                                                                                                            # Run the program
                                                                                                                                                                                                                                                                            if __name__ == "__main__":
                                                                                                                                                                                                                                                                                main()
                                                                                                                                                                                                                                                                                def calculate_discount(price, discount_percent):
                                                                                                                                                                                                                                                                                    """Calculate the final price after applying a discount if it's 20% or higher."""
                                                                                                                                                                                                                                                                                        if discount_percent >= 20:
                                                                                                                                                                                                                                                                                                return price - (price * discount_percent / 100)
                                                                                                                                                                                                                                                                                                    return price

                                                                                                                                                                                                                                                                                                    def calculate_tax(price, tax_rate):
                                                                                                                                                                                                                                                                                                        """Calculate the tax amount based on the given tax rate."""
                                                                                                                                                                                                                                                                                                            return price * (tax_rate / 100)

                                                                                                                                                                                                                                                                                                            def main():
                                                                                                                                                                                                                                                                                                                try:
                                                                                                                                                                                                                                                                                                                        # Get user input
                                                                                                                                                                                                                                                                                                                                original_price = float(input("Enter the original price of the item: "))
                                                                                                                                                                                                                                                                                                                                        discount_percentage = float(input("Enter the discount percentage: "))
                                                                                                                                                                                                                                                                                                                                                tax_rate = float(input("Enter the sales tax percentage: "))

                                                                                                                                                                                                                                                                                                                                                        # Ensure input is valid
                                                                                                                                                                                                                                                                                                                                                                if original_price < 0 or discount_percentage < 0 or tax_rate < 0:
                                                                                                                                                                                                                                                                                                                                                                            print("Price, discount percentage, and tax rate must be non-negative.")
                                                                                                                                                                                                                                                                                                                                                                                        return

                                                                                                                                                                                                                                                                                                                                                                                                # Calculate discounted price
                                                                                                                                                                                                                                                                                                                                                                                                        discounted_price = calculate_discount(original_price, discount_percentage)

                                                                                                                                                                                                                                                                                                                                                                                                                # Calculate tax on the discounted price
                                                                                                                                                                                                                                                                                                                                                                                                                        tax_amount = calculate_tax(discounted_price, tax_rate)

                                                                                                                                                                                                                                                                                                                                                                                                                                # Calculate final price
                                                                                                                                                                                                                                                                                                                                                                                                                                        final_price = discounted_price + tax_amount

                                                                                                                                                                                                                                                                                                                                                                                                                                                # Print the breakdown
                                                                                                                                                                                                                                                                                                                                                                                                                                                        print("\n--- Price Breakdown ---")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                print(f"Original Price: ${original_price:.2f}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if discount_percentage >= 20:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    print(f"Discount Applied: {discount_percentage}%")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                print(f"Discounted Price: ${discounted_price:.2f}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    print("No discount applied.")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    print(f"Tax Amount ({tax_rate}%): ${tax_amount:.2f}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            print(f"Final Price After Tax: ${final_price:.2f}")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                except ValueError:
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        print("Invalid input. Please enter numeric values for price, discount, and tax rate.")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        # Run the program
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            main()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            