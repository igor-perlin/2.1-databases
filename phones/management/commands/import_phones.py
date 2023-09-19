import os
import csv
from django.core.management.base import BaseCommand
from phones.models import Phone

# Устанавливаем переменную окружения для Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

import django

django.setup()


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Открываем файл с телефонами
        with open('phones.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')  # Обратите внимание на разделитель ';'

            # Пропускаем заголовок
            next(reader)

            for row in reader:
                # Проверяем, что в строке есть хотя бы 6 колонок (id не нужен, так как он автоматически генерируется)
                if len(row) >= 6:
                    Phone.objects.create(
                        name=row[1],
                        image=row[2],
                        price=row[3],
                        release_date=row[4],
                        lte_exists=row[5]
                    )
                else:
                    self.stdout.write(self.style.WARNING(f"Пропущена строка с недостаточным числом колонок: {row}"))
