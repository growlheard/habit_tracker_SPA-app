from django.core.exceptions import ValidationError


class HabitValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if self.field == 'related_habit' and value.get('reward'):
            raise ValidationError("�������� �� ����� ����� ������������ ��������� �������� � ��������������.")

        if self.field == 'estimated_time' and value.get('estimated_time') > 120:
            raise ValidationError("�������������� ����� ���������� �������� ������ ���� �� ����� 120 ������.")

        if self.field == 'related_habit' and value.get('related_habit') and not value.get(
                'related_habit').is_pleasurable:
            raise ValidationError("� �������� ��������� �������� ����� ������� ������ �������� ��������.")

        if self.field == 'is_pleasurable' and value.get('is_pleasurable') and (
                value.get('reward') or value.get('related_habit')):
            raise ValidationError("�������� �������� �� ����� ����� �������������� ��� ��������� ��������.")

        if self.field == 'periodicity' and value.get('periodicity') < 7:
            raise ValidationError("�������� ������ ��������� ����, ��� ��� � 7 ����.")