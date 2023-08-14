from django.core.exceptions import ValidationError


class HabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if self.field == 'related_habit' and value.get('reward'):
            raise ValidationError("Привычка не может иметь одновременно связанную привычку и вознаграждение.")

        if self.field == 'estimated_time' and value.get('estimated_time') > 120:
            raise ValidationError("Предполагаемое время выполнения привычки должно быть не более 120 секунд.")

        if self.field == 'related_habit' and value.get('related_habit') and not value.get(
                'related_habit').is_pleasurable:
            raise ValidationError("В качестве связанной привычки можно выбрать только приятную привычку.")

        if self.field == 'is_pleasurable' and value.get('is_pleasurable') and (
                value.get('reward') or value.get('related_habit')):
            raise ValidationError("Приятная привычка не может иметь вознаграждение или связанную привычку.")

        if self.field == 'periodicity' and value.get('periodicity') < 7:
            raise ValidationError("Привычку нельзя выполнять реже, чем раз в 7 дней.")