"""Estimate paint requirements and costs for a paint shop."""


class House:
    """A house represented by its wall area."""

    def __init__(self, wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        """Return the number of paint buckets needed for this house."""
        return 2.5 * self.wall_area


class Paint:
    """Paint with a bucket count and a color."""

    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color

    def total_price(self):
        """Return the price before any discount."""
        if self.color == "white":
            return self.buckets * 1.99
        return self.buckets * 2.19


class DiscountedPaint(Paint):
    """Paint that can calculate a discounted total price."""

    def discounted_price(self, discount_percentage):
        """Return the total after applying a percentage discount.

        Pass a value such as 10 for a 10% discount.
        """
        original_price = self.total_price()
        discount_amount = original_price * discount_percentage / 100
        return original_price - discount_amount


if __name__ == "__main__":
    house = House(10)
    buckets = house.paint_needed()

    paint = DiscountedPaint(buckets, "white")

    print(f"Buckets needed: {buckets}")
    print(f"Original price: ${paint.total_price():.2f}")
    print(f"Price after 10% discount: ${paint.discounted_price(10):.2f}")



