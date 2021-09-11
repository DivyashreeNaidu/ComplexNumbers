# Python3 program to Add two complex numbers

# User Defined Complex class


class Complex:

    # Constructor to accept
    # real and imaginary part
    def __init__(self, tempReal, tempImaginary):
        self.real = tempReal
        self.imaginary = tempImaginary

    # Defining addComp() method
    # for adding two complex number
    def addComp(self, C1, C2):

        # creating temporary variable
        temp = Complex(0, 0)

        # adding real part of complex numbers
        temp.real = C1.real + C2.real

        # adding Imaginary part of complex numbers
        temp.imaginary = C1.imaginary + C2.imaginary

        # returning the sum
        return temp
    # Defining diffComp() method
    # for getting difference of two complex number
    def diffComp(self, C1, C2):

        # creating temporary variable
        temp = Complex(0, 0)

        # subtracting real part of complex numbers
        temp.real = C1.real - C2.real

        # subtracting Imaginary part of complex numbers
        temp.imaginary = C1.imaginary - C2.imaginary

        # returning the diff
        return temp

    def proComp(self, C1, C2):

        # creating temporary variable
        temp = Complex(0, 0)

        # subtracting real part of complex numbers
        temp.real = (C1.real * C2.real) - (C1.imaginary*C2.imaginary)

        # subtracting Imaginary part of complex numbers
        temp.imaginary = (C1.real * C2.imaginary) + (C1.imaginary*C2.real)

        # returning the diff
        return temp


# Driver code
if __name__ == '__main__':

    # First Complex number
    C1 = Complex(3, 2)

    # printing first complex number
    print("Complex number 1 :", C1.real, "+ i" + str(C1.imaginary))

    # Second Complex number
    C2 = Complex(9, 5)

    # printing second complex number
    print("Complex number 2 :", C2.real, "+ i" + str(C2.imaginary))

    # for Storing the sum
    C3 = Complex(0, 0)

    # calling addComp() method
    C3 = C3.addComp(C1, C2)

    # printing the sum
    print("Sum of complex number :", C3.real, "+ i" + str(C3.imaginary))

    # for Storing the diff
    C4 = Complex(0, 0)

    # calling addComp() method
    C4 = C4.diffComp(C1, C2)

    # printing the difference
    print("diff of complex number :", C4.real, "+ i" + str(C4.imaginary))

 # for Storing the product
    C5 = Complex(0, 0)

    # calling addComp() method
    C5 = C5.proComp(C1, C2)
    print("product of complex number :", C5.real, "+ i" + str(C5.imaginary))
