class Tijd:
    """
    A simple class that represents a timestamp on a 24-hour clock.
    """
    def __init__(self, hour: int, minute: int, second: int) -> None:
        """Create a new Tijd instance."""
        self.validate_input(hour, minute, second)
        self._hour = hour
        self._minute = minute
        self._second = second


    def validate_input(self, hour: int, minute: int, second: int) -> None:
        """Checks if the input parameters are valid."""
        #Deze method hoort een functie te zijn, maar er staat in de opdracht dat we alleen een class mochten maken.
        if not (0 <= hour < 24):
            raise ValueError("Hour must be between 0 and 23")
        if not (0 <= minute < 60):
            raise ValueError("Minute must be between 0 and 59")
        if not (0 <= second < 60):
            raise ValueError("Second must be between 0 and 59")


    def geef_uren(self) -> int:
        """Returns the hour value."""
        return self._hour


    def geef_minuten(self) -> int:
        """Returns the minute value."""
        return self._minute


    def geef_seconden(self) -> int:
        """Returns the second value."""
        return self._second


    def verander_uren(self, hour: int) -> None:
        """Changes the hour value."""
        if not (0 <= hour <= 23):
            raise ValueError("Hour must be between 0 and 23")
        self._hour = hour


    def verander_minuten(self, minute: int) -> None:
        """Changes the minute value."""
        if not (0 <= minute <= 59):
            raise ValueError("Minute must be between 0 and 59")
        self._minute = minute


    def verander_seconden(self, second: int) -> None:
        """Changes the second value."""
        if not (0 <= second <= 59):
            raise ValueError("Second must be between 0 and 59")
        self._second = second


    def __add__(self, other: "Tijd") -> "Tijd":
        """Adds two Tijd instances."""
        if not isinstance(other, Tijd):
            raise TypeError(f"Can't add {type(other)} to Tijd class")

        seconds = self._second + other._second
        minutes = self._minute + other._minute + seconds // 60
        hours = self._hour + other._hour + minutes // 60

        return Tijd(hours % 24, minutes % 60, seconds % 60)


    def __sub__(self, other: "Tijd") -> "Tijd":
        """Subtracts two Tijd instances."""
        if not isinstance(other, Tijd):
            raise TypeError(f"Can't subtract {type(other)} with Tijd class")

        seconds_combined_self = self._hour * 3600 + self._minute * 60 + self._second
        seconds_combined_other = other._hour * 3600 + other._minute * 60 + other._second
        difference = seconds_combined_self - seconds_combined_other
        #24 hours in a day converts to 3600 * 24 = 86400 secconds
        difference %= 86400

        hour = difference // 3600
        difference %= 3600
        minute = difference // 60
        second = difference % 60

        return Tijd(hour, minute, second)


    def __str__(self) -> str:
        """Returns a string representation of the Tijd instance."""
        return f"{self._hour}:{self._minute}:{self._second}"
