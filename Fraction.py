# Define your Fraction class here
class Fraction(object):
    def __init__(self, denominator, numerator):
        if self.denominator == 0:
            raise ValueError
        else:
            self.denominator = denominator
            self.numerator = numerator
    def get_numerator(self):
        return self.numerator
    def get_denominator(self):
        return self.denominator
    def set_numerator(self, new_numerator):
        self.numerator = new_numerator
    def set_denominator(self, new_denominator):
        if self.denominator == 0:
            raise ValueError
        else:
            self.denominator = new_denominator
    def __str__(self):
        return (str(self.denominator) + " / " + (str(self.numerator))
    def add(self, otherFraction):
        if self.denominator == otherFraction.denominator
            self.numerator







        



if __name__ == '__main__':
  # put your code that utilizes your Fraction class here
  pass
