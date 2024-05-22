# <p align = "center">Факторы, воздействующие на информацию</p>

Изучить ГОСТ Р 51275-2006 "факторы, воздействующие на информацию" (http://docs.cntd.ru/document/gost-r-51275-2006)

Сопоставить факторы с банком данных угроз (bdu.fstec.ru)

Привести примеры качеств, нарушаемых при реализации факторов. Привести примеры сценариев нарушения защищенности для этих факторов. Оформить результат в виде таблицы.

ttps://github.com/kovalevegor/Information-Security/blob/main/ГОСТ%20Р%2051275-2006.md

[ГОСТ Р 51275-2006](https://github.com/kovalevegor/Information-Security/blob/main/ГОСТ%20Р%2051275-2006.md)

[ФСТЭК](https://bdu.fstec.ru/threat?ajax=threats&size=100)

### Таблица факторов воздействия и соответствующих угроз

| **Фактор воздействия (ГОСТ Р 51275-2006)** | **Угрозы (ФСТЭК)** | **Нарушаемые качества** | **Примеры сценариев нарушения защищенности** |
|---------------------------------------------|----------------------|--------------------------|--------------------------------------------------|
| Передача сигналов  | [УБИ.001]() |  |  |
| Излучения сигналов, функционально присущие техническим средствам (устройствам) ОИ | [УБИ 001]() |  |  |
| Побочные электромагнитные излучения | [УБИ 001]() |  |  |
| Паразитное электромагнитное излучение | [УБИ 001]() |  |  |
| Наличие акустоэлектрических преобразователей в элементах ТС ОИ | [УБИ 001]() |  |  |
| Дефекты, сбои отказы, аварии ТС и систем ОИ | [УБИ 001]() |  |  |
| Дефекты, сбои и отказы программного обеспечения ОИ | [УБИ 001]() |  |  |
| Явления техногенного характера | [УБИ 001]() |  |  |
| Природные явления, стихийные бедствия | [УБИ 001]() |  |  |
| Разглашение защищаемой информации лицами, и имеющими к ней право доступа | [УБИ 001]() |  |  |
| Неправомерные действия со стороны лиц, и имеющих право доступа к защищаемой информации | [УБИ.063](https://bdu.fstec.ru/threat/ubi.063v): Угроза некорректного использования функционала программного и аппаратного обеспечения | Конфиденциальность, целостность, доступность | Злоумышленник изучает документацию и возможности программных и аппаратных средств, чтобы выявить потенциальные слабости и нестандартные способы их использования. Он получает доступ к системе, возможно, под видом легитимного пользователя. Злоумышленник вводит нестандартные или некорректные команды, которые не ожидаются системой. Например, команда может использовать функцию системы таким образом, чтобы она выполняла деструктивные действия, такие как удаление данных, переполнение буфера или запуск несанкционированных процессов. |
| Несанкционированный доступ к информации | [УБИ.074](https://bdu.fstec.ru/threat/ubi.074): Угроза несанкционированного доступа к аутентификационной информации | Конфиденциальность | Злоумышленник получает физический или удаленный доступ к компьютеру. Это может быть достигнуто через эксплуатацию уязвимостей в ПО, социальную инженерию или использование вредоносного ПО. Злоумышленник использует специальные инструменты или скрипты для сканирования оперативной памяти компьютера, чтобы найти и извлечь пароли и учетные данные, которые временно сохраняются там. Это может быть достигнуто через использование дебаггера или других программных инструментов для анализа памяти. Злоумышленник ищет файлы, которые могут содержать пароли и учетные данные, например, файлы конфигураций, файлы сессий или текстовые файлы с открытыми паролями. Эти файлы могут быть скопированы на внешние носители или отправлены злоумышленнику через интернет. |
| Недостатки организационного обеспечения защиты информации | [УБИ.098](https://bdu.fstec.ru/threat/ubi.098): Угроза обнаружения открытых портов и идентификации привязанных к ним сетевых служб | Конфиденциальность | Злоумышленник получает доступ к дискредитируемой вычислительной сети, возможно, через эксплойт, фишинговую атаку или с использованием скомпрометированных учетных данных. Злоумышленник использует специализированное программное обеспечение для сканирования сетевых портов системы. Сканирование позволяет выявить открытые порты и определить, какие сервисы на них работают. Определяется, по каким портам можно осуществлять деструктивные воздействия напрямую, а по каким требуется обход межсетевых экранов. Для атак на защищенные порты могут быть применены специальные техники обхода, такие как туннелирование, фрагментация пакетов или использование легитимных сервисов для скрытого доступа. |
| Ошибки обслуживающего персонала ОИ | [УБИ.097](https://bdu.fstec.ru/threat/ubi.097): Угроза несогласованности правил доступа к большим данным | Конфиденциальность, доступность | Обслуживающий персонал или администраторы системы допускают ошибки при назначении прав доступа пользователям. Пользователь, получивший избыточные привилегии, получает доступ к защищаемой информации, к которой он не должен иметь доступа. Это может привести к утечке конфиденциальной информации или её неправомерному использованию. |
| Доступ к защищаемой информации с применением технических средств | [УБИ.088](https://bdu.fstec.ru/threat/ubi.088): Угроза несанкционированного копирования защищаемой информации | Конфиденциальность | Злоумышленник получает доступ к системе через уязвимость в программном обеспечении, фишинговую атаку, кражу учетных данных или социальную инженерию. Злоумышленник использует учетную запись с недостаточно ограниченными правами доступа. Злоумышленник осуществляет поиск конфиденциальной информации в системе, используя имеющиеся права доступа. Он находит файлы, документы или базы данных, содержащие защищаемую информацию. Злоумышленник копирует найденную информацию на съемный носитель (USB-накопитель, внешний жесткий диск) или загружает её в облачное хранилище, доступное вне системы. Если информация обрабатывается в нешифрованном виде, злоумышленник делает копию именно в этот момент. |
| Несанкционированный доступ к защищаемой информации | [УБИ.023](https://bdu.fstec.ru/threat/ubi.023): Угроза изменения компонентов информационной (автоматизированной) системы | Конфиденциальность, целостность, доступность | Злоумышленник получает доступ к сети, файлам и внедряет закладки путем несанкционированного изменения программных или аппаратных средств информационной системы. Это позволяет ему или другому нарушителю осуществлять несанкционированные действия. |
| Блокирование доступа к защищаемой информации путем перегрузки технических средств обработки информации ложными заявками на ее обработку | [УБИ.029](https://bdu.fstec.ru/threat/ubi.029): Угроза использования вычислительных ресурсов суперкомпьютера «паразитными» процессами | Доступность | Злоумышленник получает доступ к суперкомпьютеру, возможно, через учетную запись с недостаточными мерами безопасности. Вредоносное ПО или скрипт подготавливается для запуска на суперкомпьютере. Злоумышленник запускает задание, которое создаёт большое количество процессов-потомков. Эти процессы не завершаются корректно после выполнения задания и продолжают оставаться в памяти. Вредоносное ПО запускается и начинает создавать дополнительные процессы, маскируясь под легитимные задачи. |
| Действия криминальных групп и отдельных преступных субъектов | [УБИ.061](https://bdu.fstec.ru/threat/ubi.061?viewtype=list): Угроза некорректного задания структуры данных транзакции | Целостность, доступность | Злоумышленник получает доступ к клиентскому приложению или базе данных с возможностью выполнения транзакций. Злоумышленник изучает механизм обработки транзакций и ищет уязвимости. Злоумышленник инициирует транзакцию и прерывает её выполнение, что приводит к неполному выполнению. Например, транзакция может быть прервана на этапе передачи данных, что приводит к некорректным или неполным записям в базе данных. |
| Искажение, уничтожение или блокирование информации с применением технических средств | [УБИ.006](https://bdu.fstec.ru/threat/ubi.006): Угроза внедрения кода или данных | Конфиденциальность, доступность, целостность | Злоумышленник внедряет вредоносный код в информационную систему или IoT-устройство через уязвимости ПО, слабую антивирусную защиту или открытый Telnet-порт. Код активируется вручную пользователем, автоматически при наступлении определенных условий или с использованием учетных данных по умолчанию. |

