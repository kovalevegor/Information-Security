# <p align = "center">Факторы, воздействующие на информацию</p>

Изучить ГОСТ Р 51275-2006 "факторы, воздействующие на информацию" (http://docs.cntd.ru/document/gost-r-51275-2006)

Сопоставить факторы с банком данных угроз (bdu.fstec.ru)

Привести примеры качеств, нарушаемых при реализации факторов. Привести примеры сценариев нарушения защищенности для этих факторов. Оформить результат в виде таблицы.

[ГОСТ Р 51275-2006](https://github.com/kovalevegor/Information-Security/blob/main/ГОСТ%20Р%2051275-2006.md)

[ФСТЭК](https://bdu.fstec.ru/threat?ajax=threats&size=100)

### Таблица факторов воздействия и соответствующих угроз

| **Фактор воздействия (ГОСТ Р 51275-2006)** | **Угрозы (ФСТЭК)** | **Нарушаемые качества** | **Примеры сценариев нарушения защищенности** |
|---------------------------------------------|----------------------|--------------------------|--------------------------------------------------|
| Физические воздействия (пожар, затопление)  | Вандализм, стихийные бедствия | Целостность, доступность | Пожар уничтожает серверное оборудование, делая данные недоступными. |
| Электромагнитные воздействия (ЭМИ)          | Электромагнитные атаки, саботаж | Целостность, доступность | Мощный электромагнитный импульс выводит из строя все электронные устройства. |
| Технические сбои (отказ оборудования)       | Отказы и сбои ИТ-инфраструктуры | Доступность | Сбой жесткого диска приводит к потере доступа к важным данным. |
| Вирусы и вредоносное ПО                     | Вирусные атаки, трояны | Конфиденциальность, целостность | Вирус шифрует файлы, требуя выкуп за их восстановление. |
| Неавторизованный доступ                     | Взломы, кража данных | Конфиденциальность | Злоумышленник получает доступ к базе данных пользователей и похищает личные данные. |
| Ошибки персонала                            | Человеческие ошибки, утечки данных | Целостность, конфиденциальность | Сотрудник случайно удаляет важные файлы или отправляет конфиденциальные данные не тому адресату. |
| Программные ошибки                          | Уязвимости ПО, баги | Целостность, доступность | Ошибка в программном обеспечении приводит к некорректной обработке данных и их искажению. |


### Таблица факторов воздействия и соответствующих угроз

| **Фактор воздействия (ГОСТ Р 51275-2006)** | **Угрозы (ФСТЭК)** | **Нарушаемые качества** | **Примеры сценариев нарушения защищенности** |
|---------------------------------------------|----------------------|--------------------------|--------------------------------------------------|
| Физические воздействия (пожар, затопление)  | Вандализм, стихийные бедствия | Целостность, доступность | Пожар уничтожает серверное оборудование, делая данные недоступными. |
| Электромагнитные воздействия (ЭМИ)          | Электромагнитные атаки, саботаж | Целостность, доступность | Мощный электромагнитный импульс выводит из строя все электронные устройства. |
| Технические сбои (отказ оборудования)       | Отказы и сбои ИТ-инфраструктуры | Доступность | Сбой жесткого диска приводит к потере доступа к важным данным. |
| Вирусы и вредоносное ПО                     | Вирусные атаки, трояны | Конфиденциальность, целостность | Вирус шифрует файлы, требуя выкуп за их восстановление. |
| Неавторизованный доступ                     | Взломы, кража данных | Конфиденциальность | Злоумышленник получает доступ к базе данных пользователей и похищает личные данные. |
| Ошибки персонала                            | Человеческие ошибки, утечки данных | Целостность, конфиденциальность | Сотрудник случайно удаляет важные файлы или отправляет конфиденциальные данные не тому адресату. |
| Программные ошибки                          | Уязвимости ПО, баги | Целостность, доступность | Ошибка в программном обеспечении приводит к некорректной обработке данных и их искажению. |

### Примеры качеств, нарушаемых при реализации факторов:
1. **Конфиденциальность**: Утечка данных при неавторизованном доступе или вирусной атаке.
2. **Целостность**: Искажение данных из-за вирусов или ошибок ПО.
3. **Доступность**: Недоступность данных из-за технических сбоев или физических воздействий.

### Примеры сценариев нарушения защищенности:
1. **Пожар в серверной**: Приводит к уничтожению серверного оборудования, что делает данные недоступными.
2. **Электромагнитная атака**: Выводит из строя все электронные устройства, нарушая доступность и целостность данных.
3. **Вирусная атака**: Вредоносное ПО шифрует файлы, требуя выкуп за их восстановление, что нарушает конфиденциальность и целостность.
4. **Взлом базы данных**: Хакер получает неавторизованный доступ и похищает личные данные пользователей.
5. **Ошибка сотрудника**: Сотрудник случайно удаляет важные файлы или неправильно настраивает систему, что приводит к потере данных.


