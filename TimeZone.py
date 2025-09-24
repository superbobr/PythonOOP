"""
 **TimeZone Class**
In this task, you will implement a class to store information about a time zone.
To accomplish this, create a `TimeZone` class that accepts the following inputs:
- the name of the time zone,
- the hour offset relative to Coordinated Universal Time (UTC),
- the minute offset relative to UTC.
Your task is to implement three properties to manage and validate the input values. Their names must be:
- `name`
- `offset_hours`
- `offset_minutes`
The `name` property must accept only non-empty strings, trimming any leading or trailing whitespace. If the provided time zone name does not meet these requirements, raise a `ValueError` with the message:
`'Timezone bad name - <value>'`
The `offset_hours` property must accept only integer values ranging from -12 to 14 (inclusive). If the provided hour offset is not an integer, raise:
`ValueError('Hour offset must be an integer.')`
If the integer is outside the allowed range, raise:
`ValueError('Offset must be between -12:00 and +14:00.')`
The `offset_minutes` property must accept only integer values ranging from -59 to 59 (inclusive). If the provided minute offset is not an integer, raise:
`ValueError('Minutes offset must be an integer.')`
If the integer is outside the allowed range, raise:
`ValueError('Minutes offset must be between -59 and 59.')`
 """
class TimeZone:
    def __init__(self, name, offset_hours, offset_minutes):
        self.name = name
        self.offset_hours = offset_hours
        self.offset_minutes = offset_minutes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError(f'Timezone bad name - {value}')
        stripped = value.strip()
        if len(stripped) == 0:
            raise ValueError(f'Timezone bad name - {value}')
        else:
            self._name = stripped

    @property
    def offset_hours(self):
        return self._offset_hours

    @offset_hours.setter
    def offset_hours(self, value):
        if not isinstance(value, int):
            raise ValueError('Hour offset must be an integer.')
        elif not(-12 <= value <= 14):
            raise ValueError('Offset must be between -12:00 and +14:00.')
        else:
            self._offset_hours = int(value)

    @property
    def offset_minutes(self):
        return self._offset_minutes

    @offset_minutes.setter
    def offset_minutes(self, value):
        if not isinstance(value, int):
            raise ValueError('Minutes offset must be an integer.')
        elif not(-59 <= value <= 59):
            raise ValueError('Minutes offset must between -59 and 59.')
        else:
            self._offset_minutes = int(value)
