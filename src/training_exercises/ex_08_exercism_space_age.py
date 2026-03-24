"""Space Age exercise from Exercism.

Calculates a person's age on different planets based on orbital periods.
"""


class SpaceAge:
    """Calculate age on various planets based on seconds lived."""

    def __init__(self, seconds: int) -> None:
        """Initialize SpaceAge with age in seconds.

        Args:
            seconds: The number of seconds lived.

        Stores the exact Earth years calculation for use in all planet age methods.
        """
        self.seconds = seconds
        self.earth_years_exact = self.seconds / 31_557_600

    def on_earth(self) -> float:
        """Calculate age in Earth years.

        Returns:
            Age in Earth years, rounded to 2 decimal places.
        """
        return round(self.earth_years_exact, 2)

    def on_mercury(self) -> float:
        """Calculate age in Mercury years.

        Returns:
            Age in Mercury years, rounded to 2 decimal places.
        """
        return round(self.earth_years_exact / 0.2408467, 2)

    def on_venus(self) -> float:
        """Calculate age in Venus years.

        Returns:
            Age in Venus years, rounded to 2 decimal places.
        """
        return round(self.earth_years_exact / 0.61519726, 2)

    def on_mars(self) -> float:
        """Calculate age in Mars years.

        Returns:
            Age in Mars years, rounded to 2 decimal places.
        """
        return round(self.earth_years_exact / 1.8808158, 2)

    def on_jupiter(self) -> float:
        """Calculate age in Jupiter years.

        Returns:
            Age in Jupiter years, rounded to 2 decimal places.
        """
        return round(self.earth_years_exact / 11.862615, 2)

    def on_saturn(self) -> float:
        """Calculate age in Saturn years.

        Returns:
            Age in Saturn years, rounded to 2 decimal places.
        """
        return round(self.earth_years_exact / 29.447498, 2)

    def on_uranus(self) -> float:
        """Calculate age in Uranus years.

        Returns:
            Age in Uranus years, rounded to 2 decimal places.
        """
        return round(self.earth_years_exact / 84.016846, 2)

    def on_neptune(self) -> float:
        """Calculate age in Neptune years.

        Returns:
            Age in Neptune years, rounded to 2 decimal places.
        """
        return round(self.earth_years_exact / 164.79132, 2)
