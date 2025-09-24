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
