"""Check which coordinates fall inside a rectangle and calculate a score."""


class Rectangle:
    """A rectangle defined by its top-left and bottom-right corners."""

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_inside(self, x, y):
        """Return True when (x, y) is inside or on the rectangle boundary."""
        return self.x1 <= x <= self.x2 and self.y2 <= y <= self.y1


class PointChecker:
    """Filter a list of points using a Rectangle object."""

    def __init__(self, rectangle, points):
        self.rectangle = rectangle
        self.points = points

    def find_points_inside(self):
        """Return only the candidate points inside the rectangle."""
        points_inside = []

        for x, y in self.points:
            if self.rectangle.is_inside(x, y):
                points_inside.append((x, y))

        return points_inside


class ScoredPointChecker(PointChecker):
    """A point checker that awards points for each point inside."""

    def calculate_score(self, points_value):
        """Return the number of valid points multiplied by points_value."""
        valid_points = self.find_points_inside()
        return len(valid_points) * points_value


if __name__ == "__main__":
    # The rectangle spans x=1..5 and y=1..4, including its edges.
    rectangle = Rectangle(1, 4, 5, 1)
    candidate_points = [(2, 3), (5, 1), (6, 2), (0, 4), (3, 5)]

    checker = ScoredPointChecker(rectangle, candidate_points)
    valid_points = checker.find_points_inside()

    print(f"Points inside: {valid_points}")
    print(f"Score (10 points per coordinate): {checker.calculate_score(10)}")  