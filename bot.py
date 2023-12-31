import telebot
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='6279214678:AAGIBptzgSOYI3hdqSrVCQywHoAl2u-vEo8')
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Здарова, экзамен по кситу")

@dp.message_handler(text="1")
async def q1(message: types.Message):
    with open('1.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Принцип многоуровневого подхода при решении задачи сетевого взаимодействия заключается в разделении задач на набор уровней, каждый из которых выполняет свои функции и взаимодействует с уровнями, расположенными выше и ниже в иерархии. Это позволяет создавать более гибкие, надежные и эффективные сети.")
@dp.message_handler(text="2")
async def q1(message: types.Message):
    with open('2.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Многоуровневый подход реализуется с помощью стека протоколов, в котором каждый уровень выполняет определенные функции для обеспечения передачи данных. Протокол - это соглашение об обмене данными между устройствами в сети. Инкапсуляция - это процесс добавления заголовков и/или футеров к данным на каждом уровне стека протоколов.")
@dp.message_handler(text="3")
async def q1(message: types.Message):
    with open('3.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Модель OSI (Open Systems Interconnection) состоит из 7 уровней:Физический, Канальный, Сетевой, Транспортный, Сеансовый, Представительный, Прикладной, Каждый уровень выполняет определенные функции, которые обеспечивают передачу данных между устройствами в сети.")
@dp.message_handler(text="4")
async def q1(message: types.Message):
    with open('4.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Физический уровень решает задачи, связанные с передачей битов через физические среды. Канальный уровень решает задачи, связанные с управлением доступом к каналу связи и обеспечением надежной передачи данных.")
@dp.message_handler(text="5")
async def q1(message: types.Message):
    with open('5.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Сетевой уровень решает задачи маршрутизации пакетов между сетями. Этот уровень определяет, как выбирать оптимальный путь для передачи пакета и как обрабатывать ошибки в сети.")
@dp.message_handler(text="6")
async def q1(message: types.Message):
    with open('6.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Транспортный уровень решает задачи обеспечения надежной передачи данных между приложениями, работающими на разных устройствах. Этот уровень определяет, какие протоколы транспортировки должны использоваться для передачи данных и как обрабатывать ошибки в передаче данных.")
@dp.message_handler(text="7")
async def q1(message: types.Message):
    with open('7.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Сеансовый, представительный и прикладной уровни решают задачи, связанные с управлением сеансами связи между приложениями, переводом данных в формат, понятный приложениям и обеспечением доступа к различным приложениям в сети.")
@dp.message_handler(text="8")
async def q1(message: types.Message):
    await message.answer("Стек протоколов TCP/IP состоит из 4 уровней:\nСетевой\nТранспортный\nПрикладной\nСетевой интерфейс\nПротоколы на каждом уровне выполняют специфические функции для обеспечения передачи данных по сети. Некоторые примеры протоколов на каждом уровне:\nСетевой уровень: IP, ICMP, ARP\nТранспортный уровень: TCP, UDP\nПрикладной уровень: HTTP, FTP, DNS\nСетевой интерфейс: Ethernet, Wi-Fi\nСоответствие уровней стека протоколов TCP/IP уровням модели OSI:\nСетевой уровень TCP/IP соответствует сетевому уровню OSI.\nТранспортный уровень TCP/IP соответствует транспортному уровню OSI.\nПрикладной уровеньTCP/IP соответствует совокупности сеансового, представительного и прикладного уровней OSI.\nСетевой интерфейс TCP/IP соответствует физическому и канальному уровням OSI.")
@dp.message_handler(text="9")
async def q1(message: types.Message):
    await message.answer("Технология Ethernet использует несколько разновидностей форматов кадра, таких как Ethernet II, IEEE 802.3, IEEE 802.2 и другие. Каждый формат имеет свои назначения и отличия, но общими для них являются поля, такие как преамбула, заголовок кадра, данные и CRC-код. Преамбула содержит уникальную последовательность битов, которая помогает приемнику синхронизироваться с передатчиком. Заголовок кадра содержит информацию о MAC-адресах отправителя и получателя, типе протокола и другие параметры. Данные - это непосредственно передаваемая информация. CRC-код используется для обнаружения ошибок в передаче данных. Алгоритм распознавания формата кадра заключается в анализе значений полей в заголовке кадра, которые определяют тип кадра и его содержание.")
@dp.message_handler(text="10")
async def q1(message: types.Message):
    await message.answer("Локальные сети могут быть структурированы по различным принципам, таким как физическая, логическая, функциональная и другие. Физическая структуризация основана на физической топологии сети, такой как звезда, кольцо, шина и т.п. Логическая структуризация основана на логической организации сети, такой как VLAN (Virtual Local Area Network) или VPN (Virtual Private Network). Функциональная структуризация основана на функциональных группах устройств в сети, таких как серверы, коммутаторы, маршрутизаторы и т.п. Каждый из этих подходов имеет свои преимущества и недостатки, и выбор подходящей структуры зависит от конкретных требований и задач, которые должна решать локальная сеть.")
@dp.message_handler(text="11")
async def q1(message: types.Message):
    await message.answer("Прозрачный мост (Transparent Bridge) - это устройство сетевого уровня, которое соединяет две локальные сети и обеспечивает передачу данных между ними. Он работает на основе алгоритма обучения, который учит мост, какие устройства находятся в какой сети, и на основе этого принимает решение о том, в какую сеть должен быть передан пакет данных. Мост анализирует MAC-адреса в пакетах данных и использует таблицу MAC-адресов для определения, в какую сеть нужно отправить пакет. Если мост не знает, куда отправить пакет, он передает его во все порты, кроме того, на который он получен.")
@dp.message_handler(text="12")
async def q1(message: types.Message):
    await message.answer("Коммутатор (Switch) - это устройство сетевого уровня, которое соединяет несколько устройств в локальной сети и обеспечивает коммутацию данных между ними. Он работает на основе таблицы MAC-адресов, которая содержит информацию о том, какие устройства находятся на каких портах. Когда коммутатор получает пакет данных, он анализирует его MAC-адрес и использует таблицу MAC-адресов для определения, на какой порт нужно отправить пакет. Если коммутатор не знает, куда отправить пакет, он отправляет его на все порты, кроме того, на который он получен. Основное отличие коммутатора от моста заключается в том, что коммутатор имеет более сложную структуру коммутирующего блока, позволяющую обеспечивать более высокую пропускную способность и ускоренную обработку данных.")
@dp.message_handler(text="13")
async def q1(message: types.Message):
    with open('13.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Уровень межсетевого взаимодействия (Network Layer) стека протоколов TCP/IP обеспечивает маршрутизацию пакетов между различными сетями. Основными протоколами на этом уровне являются IP (Internet Protocol), ICMP (Internet Control Message Protocol) и ARP (Address Resolution Protocol). IP обеспечивает адресацию и маршрутизацию пакетов, ICMP используется для передачи сообщений об ошибках и управления сетью, а ARP используется для определения MAC-адреса устройства по его IP-адресу.")
@dp.message_handler(text="14")
async def q1(message: types.Message):
    with open('14.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Транспортный уровень (Transport Layer) стека протоколов TCP/IP обеспечивает надежную передачу данных между приложениями, работающими на разных устройствах. Основными протоколами на этом уровне являются TCP (Transmission Control Protocol) и UDP (User Datagram Protocol). TCP обеспечивает надежную передачу данных с помощью механизма контроля ошибок, управления потоком и механизма переотправки данных. UDP не обеспечивает надежности, но обладает более высокой скоростью передачи данных.")
@dp.message_handler(text="15")
async def q1(message: types.Message):
    with open('15.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Прикладной уровень (Application Layer) стека протоколов TCP/IP обеспечивает интерфейс между приложениями и сетью. Основными протоколами на этом уровне являются HTTP (Hypertext Transfer Protocol), FTP (File Transfer Protocol), DNS (Domain Name System) и другие. HTTP используется для передачи веб-страниц и других ресурсов, FTP используется для передачи файлов, а DNS используется для разрешения имен в IP-адреса.")
@dp.message_handler(text="16")
async def q1(message: types.Message):
    with open('16.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Уровень сетевых интерфейсов (Network Interface Layer) стека протоколов TCP/IP обеспечивает интерфейс между устройством и физической средой передачи данных. Основными протоколами на этом уровне являются Ethernet, Wi-Fi, PPP (Point-to-Point Protocol) и другие. Эти протоколы обеспечивают передачу данных через соответствующую физическую среду и управление доступом к среде передачи.")
@dp.message_handler(text="17")
async def q1(message: types.Message):
    await message.answer("IP-адреса бывают четырех классов: A, B, C и D. Класс IP-адреса определяет, какая часть адреса отведена для идентификации сети, а какая - для идентификации устройства внутри сети. Классы IP-адресов отличаются по количеству бит, выделенных для идентификации сети и устройства. В классе A первые 8 бит отводятся для идентификации сети, а оставшиеся 24 бита - для идентификации устройства. В классе B первые 16 бит отводятся для идентификации сети, а оставшиеся 16 бит - для идентификации устройства. В классе C первые 24 бита отводятся для идентификации сети, а оставшиеся 8 бит - для идентификации устройства. В классе D адреса используются для мультикастинга.")
@dp.message_handler(text="18")
async def q1(message: types.Message):
    await message.answer("Особыми IP-адресами являются: адрес сети сети (Network Address), широковещательный адрес сети (Broadcast Address), адрес петли обратной связи (Loopback Address) и адресы для приватных сетей (Private Addresses). Адрес сети сети используется для идентификации сети, а широковещательный адрес сети - для отправки пакетов на все устройства в сети. Адрес петли обратной связи используется для тестирования сетевых настроек и отправки пакетов на собственный компьютер. Адреса для приватных сетей используются в локальных сетях и не могут быть использованы в Интернете.")
@dp.message_handler(text="19")
async def q1(message: types.Message):
    await message.answer("Маска подсети (Subnet Mask) используется для определения того, какие биты IP-адреса отводятся для идентификации сети, а какие - для идентификации устройства. Маска представляет собой последовательность единиц и нулей, где единицы указывают на биты, отведенные для идентификации сети, а нули - на биты, отведенные для идентификации устройства. Использование масок позволяет более гибко использовать адресное пространство и уменьшить количество неиспользуемых адресов. Например, если у нас есть сеть класса B, но в ней используется только 4 подсети, то можно использовать маску подсети, которая отведет для идентификации сети не 16 бит, а только 2, и тем самым использовать адреса более эффективно.")
@dp.message_handler(text="20")
async def q1(message: types.Message):
    with open('20.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("IPv6 (Internet Protocol version 6) - это новая версия протокола IP, которая была разработана для замены IPv4. Основные особенности системы адресации IPv6 включают в себя: увеличение длины адреса с 32 бит до 128 бит, что позволяет создавать намного больше уникальных адресов; использование новой системы адресации, которая включает в себя глобальные адреса, локальные адреса, адреса приватных сетей и другие; поддержка автоматической настройки адресов и конфигурации сети.")
@dp.message_handler(text="21")
async def q1(message: types.Message):
    with open('21.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Основные отличия протокола IPv6 от IPv4 включают в себя: увеличение длины адреса с 32 бит до 128 бит; использование новой системы адресации; поддержка автоматической настройки адресов и конфигурации сети; поддержка более безопасной передачи данных с помощью протокола IPsec; улучшенная поддержка мультимедиа и потоковой передачи данных; более эффективное использование пропускной способности сети.")
@dp.message_handler(text="22")
async def q1(message: types.Message):
    with open('22.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Протокол ARP (Address Resolution Protocol) используется для определения MAC-адреса устройства по его IP-адресу. ARP-таблица содержит информацию о связи между IP-адресами и MAC-адресами устройств в локальной сети. Алгоритм разрешения адресов с помощью протокола ARP включает в себя отправку ARP-запроса на широковещательный адрес, который содержит IP-адрес устройства, для которого нужно определить MAC-адрес. Устройство, которому адресован запрос, отвечает ARP-ответом, содержащим свой MAC-адрес.")
@dp.message_handler(text="23")
async def q1(message: types.Message):
    await message.answer("Протокол DHCP (Dynamic Host Configuration Protocol) используется для автоматической настройки параметров сетевой конфигурации узлов в сети. Алгоритм назначения узлу параметров сетевой конфигурации с помощью протокола DHCP включает в себя запрос узлом IP-адреса и других параметров сетевой конфигурации у DHCP-сервера. DHCP-сервер назначает узлу IP-адрес и другие параметры сетевой конфигурации и отправляет их узлу в ответном сообщении. Примеры параметров сетевой конфигурации, назначаемых узлу, включают в себя IP-адрес, маску подсети, адрес шлюза по умолчанию, адресы DNS-серверов и другие.")
@dp.message_handler(text="24")
async def q1(message: types.Message):
    with open('24.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Система доменных имен DNS (Domain Name System) используется для разрешения имен хостов в IP-адреса. Алгоритм разрешения имен с помощью протокола DNS включает в себя отправку запроса на DNS-сервер, содержащий имя хоста, для которого нужно определить IP-адрес. DNS-сервер отвечает ответом, содержащим соответствующий IP-адрес.")
@dp.message_handler(text="25")
async def q1(message: types.Message):
    await message.answer("Алгоритм скользящего окна в протоколе TCP (Transmission Control Protocol) используется для контроля надежности передачи данных. Он позволяет отправителю отправлять несколько пакетов данных без ожидания подтверждения от получателя за каждый пакет. Размер окна определяет количество пакетов, которые отправитель может отправить до получения подтверждения от получателя. Получатель отправляет подтверждения, содержащие номер последнего успешно полученного пакета, и этот номер используется отправителем для определения нового размера окна.")
@dp.message_handler(text="26")
async def q1(message: types.Message):
    await message.answer("Алгоритм установления соединения по протоколу TCP (также называемый алгоритмом трех рукопожатий) включает в себя следующие шаги: 1) клиент отправляет серверу сообщение SYN (synchronize) с указанием своего начального номера последовательности; 2) сервер отправляет клиенту сообщение SYN-ACK (synchronize-acknowledge) с указанием своего начального номера последовательности и подтверждением начального номера последовательности клиента; 3) клиент отправляет серверу сообщение ACK (acknowledge) с подтверждением начального номера последовательности сервера.")
@dp.message_handler(text="27")
async def q1(message: types.Message):
    await message.answer("Протокол ICMP (Internet Control Message Protocol) используется для передачи сообщений об ошибках и другой информации о состоянии сети. Категории передаваемых сообщений включают в себя: сообщения об ошибках, такие как сообщения о недоступности узла или порта, сообщения о превышении времени ожидания, сообщения о неправильно сформированных пакетах и другие; сообщения о запросе, такие как сообщения типа ping, использующиеся для проверки доступности узла и определения времени задержки; другие сообщения, такие как сообщения о маршрутизации и передаче данных.")
@dp.message_handler(text="28")
async def q1(message: types.Message):
    await message.answer("Команда ping используется для проверки доступности узла в сети и определения времени задержки. Синтаксис вызова команды ping: ping [адрес узла]. Команда tracert используется для определения маршрута, который пакет данных проходит от отправителя к получателю. Синтаксис вызова команды tracert: tracert [адрес узла]. Команда ipconfig используется для получения информации о сетевой конфигурации узла. Синтаксис вызова команды ipconfig: ipconfig.")
@dp.message_handler(text="29")
async def q1(message: types.Message):
    await message.answer("Протоколы маршрутизации классифицируются по способу передачи информации о маршрутах и обновлении таблиц маршрутизации. Примеры протоколов маршрутизации включают в себя: протокол RIP (Routing Information Protocol), использующий простой алгоритм передачи информации о маршрутах и обновления таблиц маршрутизации; протокол OSPF (Open Shortest Path First), использующий более сложный алгоритм передачи информации о маршрутах и обновления таблиц маршрутизации; протокол BGP (Border Gateway Protocol), используемый для маршрутизации между автономными системами в Интернете.")
@dp.message_handler(text="30")
async def q1(message: types.Message):
    await message.answer("Классы маршрутизаторов могут быть определены по различным критериям, например, по уровню функциональности, скорости обработки данных, количеству портов и поддерживаемым протоколам маршрутизации. Некоторые классы маршрутизаторов включают в себя: маршрутизаторы доступа (access routers), которые обеспечивают доступ к сети для конечных пользователей; маршрутизаторы распределения (distribution routers), которые обеспечивают маршрутизацию между различными подсетями в сети; маршрутизаторы ядра (core routers), которые обеспечивают маршрутизацию между различными сегментами сети на высоких скоростях.")
@dp.message_handler(text="31")
async def q1(message: types.Message):
    with open('31.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Протоколы маршрутизации могут быть классифицированы по способу передачи информации о маршрутах (по векторам расстояния, по состоянию канала, по пути) и по области применения (внутренние протоколы маршрутизации, которые используются в пределах одной автономной системы, и внешние протоколы маршрутизации, которые используются для маршрутизации между автономными системами).")
@dp.message_handler(text="32")
async def q1(message: types.Message):
    with open('32.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Протокол RIP (Routing Information Protocol) использует алгоритм поиска кратчайшего пути (shortest path algorithm) для построения таблицы маршрутизации. Каждый маршрутизатор, работающий с протоколом RIP, периодически обменивается сообщениями RIP с другими маршрутизаторами в сети, чтобы обновить свою таблицу маршрутизации. Процедура построения таблицы маршрутизации включает в себя определение кратчайшего пути до каждого узла в сети на основе информации, полученной от других маршрутизаторов.")
@dp.message_handler(text="33")
async def q1(message: types.Message):
    with open('33.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("В протоколе RIP используются методы борьбы с ложными маршрутами, включая использование таймеров для удаления устаревших записей таблицы маршрутизации, ограничение количества прыжков (hop count) до узла и использование суммарных маршрутов (summary routes) для объединения нескольких маршрутов в один. Также в протоколе RIP можно использовать аутентификацию сообщений RIP, чтобы предотвратить подмену маршрутов.")
@dp.message_handler(text="34")
async def q1(message: types.Message):
    with open('34.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Протокол OSPF (Open Shortest Path First) использует алгоритм Dijkstra для построения таблицы маршрутизации. Процедура построения таблицы маршрутизации включает в себя обмен сообщениями OSPF между маршрутизаторами, обновление стоимости маршрутов и построение дерева кратчайших путей до всех узлов в сети.")
@dp.message_handler(text="35")
async def q1(message: types.Message):
    await message.answer("Fast Ethernet - это технология сетевых соединений, которая обеспечивает скорость передачи данных до 100 Мбит/с. Она была разработана для замены стандарта Ethernet, который обеспечивал скорость до 10 Мбит/с. Основными достоинствами Fast Ethernet являются более высокая скорость передачи данных и совместимость со стандартом Ethernet. Однако недостатками могут быть ограниченная дальность передачи данных (100 метров) и ограниченное количество устройств, которые можно подключить к одному сегменту сети.")
@dp.message_handler(text="36")
async def q1(message: types.Message):
    await message.answer("Gigabit Ethernet - это технология сетевых соединений, которая обеспечивает скорость передачи данных до 1 Гбит/с. Она была разработана для замены Fast Ethernet и предоставляет более высокую скорость передачи данных и возможность подключения большего количества устройств к одному сегменту сети. Однако недостатком может быть более высокая стоимость устройств и более высокие требования к кабельной инфраструктуре.")
@dp.message_handler(text="37")
async def q1(message: types.Message):
    with open('37.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Token Ring - это технология сетевых соединений, которая использует токены для передачи данных между устройствами. Одним из достоинств этой технологии является более высокая стабильность передачи данных в условиях высокой нагрузки на сеть. Однако недостатком может быть более высокая стоимость устройств и сложность конфигурации сети.")
@dp.message_handler(text="38")
async def q1(message: types.Message):
    with open('38.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("FDDI (Fiber Distributed Data Interface) - это технология сетевых соединений, которая использует оптические волокна для передачи данных. Одним из достоинств этой технологии является более высокая скорость передачи данных и более высокая стабильность передачи данных в условиях высокой нагрузки на сеть. Однако недостатками могут быть более высокая стоимость устройств и сложность конфигурации сети.")
@dp.message_handler(text="39")
async def q1(message: types.Message):
    await message.answer("Методы доступа к среде в беспроводных сетях могут включать в себя методы CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance), TDMA (Time Division Multiple Access) и FDMA (Frequency Division Multiple Access). Метод CSMA/CA используется в стандарте Wi-Fi и представляет собой метод, в котором устройство передает данные только тогда, когда среда свободна, и использует протокол ACK для подтверждения получения данных. Метод TDMA используется в стандарте GSM и представляет собой метод, в котором время передачи данных разделено на несколько слотов, которые могут быть выделены различным устройствам. Метод FDMA используется в стандарте WiMAX и представляет собой метод, в котором частотный диапазон разделен на несколько каналов, каждый из которых может быть выделен различным устройствам. Каждый метод имеет свои достоинства и недостатки, и выбор метода зависит от конкретных требований к сети.")
@dp.message_handler(text="40")
async def q1(message: types.Message):
    await message.answer("Преимущества:\nБеспроводные сети на основе стека протоколов IEEE802.11 обеспечивают мобильность и гибкость, позволяя пользователям подключаться к сети в любом месте, где есть доступ к беспроводной точке доступа.\nБеспроводные сети на основе стека протоколов IEEE802.11 могут поддерживать высокие скорости передачи данных в зависимости от стандарта (например, до 54 Мбит/с для стандарта 802.11g и до 10 Гбит/с для стандарта 802.11ax).\nБеспроводные сети на основе стека протоколов IEEE802.11 позволяют экономить на проводной инфраструктуре и уменьшать затраты на обслуживание и сопровождение сети.\nНедостатки:\nБеспроводные сети на основе стека протоколов IEEE802.11 могут быть подвержены помехам от других электронных устройств или от других беспроводных сетей.\nБеспроводные сети на основе стека протоколов IEEE802.11 могут иметь ограниченную дальность передачи данных и требовать установки дополнительных точек доступа для покрытия большой площади.\nБеспроводные сети на основе стека протоколов IEEE802.11 могут быть подвержены угрозам безопасности, таким как несанкционированный доступ или перехват данных.")
@dp.message_handler(text="41")
async def q1(message: types.Message):
    await message.answer("802.11a: обеспечивает скорость передачи данных до 54 Мбит/с в частотном диапазоне 5 ГГц. Использует технологию OFDM (Orthogonal Frequency Division Multiplexing).\n802.11b: обеспечивает скорость передачи данных до 11 Мбит/с в частотном диапазоне 2,4 ГГц. Использует технологию DSSS (Direct Sequence Spread Spectrum).\n802.11g: обеспечивает скорость передачи данных до 54 Мбит/с в частотном диапазоне 2,4 ГГц. Использует технологию OFDM.\n802.11n: обеспечивает скорость передачи данных до 600 Мбит/с в частотном диапазоне 2,4 и 5 ГГц. Использует технологию MIMO (Multiple-Input Multiple-Output) и OFDM.\n802.11ac: обеспечивает скорость передачи данных до 6,9 Гбит/с в частотном диапазоне 5 ГГц. Использует технологию MIMO и OFDM.\n802.11ax (Wi-Fi 6): обеспечивает скорость передачи данных до 9,6 Гбит/с в частотном диапазоне 2,4 и 5 ГГц. Использует технологию MIMO, OFDMA (Orthogonal Frequency Division Multiple Access) и MU-MIMO (Multi-User Multiple-Input Multiple-Output).\n802.11be (Wi-Fi 7): ожидается, что этот стандартбудет обеспечивать еще более высокие скорости передачи данных, но его спецификации еще не определены.")
@dp.message_handler(text="42")
async def q1(message: types.Message):
    await message.answer("WiMAX (Worldwide Interoperability for Microwave Access) - это технология беспроводного широкополосного доступа в сеть, которая использует стандарт IEEE 802.16. WiMAX работает в диапазонах частот от 2 до 66 ГГц и может обеспечивать скорость передачи данных до 70 Мбит/с на расстоянии до нескольких километров.\nСтек протоколов WiMAX состоит из четырех уровней:\nФизический уровень (PHY): обеспечивает передачу данных по воздуху и управление частотным диапазоном.\nУправление доступом к среде (MAC): обеспечивает управление доступом к среде для передачи данных и управление качеством обслуживания (QoS).\nСетевой уровень (NWK): обеспечивает маршрутизацию пакетов данных и управление сетью.\nУровень приложений (APP): обеспечивает приложения, работающие поверх WiMAX.\nWiMAX может работать в двух режимах: точка-многоточка (Point-to-Multipoint, PMP) и точка-точка (Point-to-Point, P2P). В режиме PMP одна базовая станция (Base Station, BS) обслуживает несколько абонентских станций (Subscriber Stations, SS), а в режиме P2P две абонентские станции могут обмениваться данными напрямую.")
@dp.message_handler(text="43")
async def q1(message: types.Message):
    with open('43.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer('DDoS-атака (Distributed Denial of Service) - это атака на компьютерные системы или сети, при которой злоумышленник использует множество компьютеров для одновременной отправки большого количества запросов на целевой сервер или сеть. Это приводит к перегрузке сервера и отказу в обслуживании легитимных пользователей.\nСхематично DDoS-атаку можно представить следующим образом: злоумышленник заражает множество компьютеров, которые в дальнейшем становятся "зомби" или ботами, и использует их для отправки большого количества запросов на целевой сервер или сеть. Это приводит к перегрузке сервера и отказу в обслуживании легитимных пользователей.')
@dp.message_handler(text="44")
async def q1(message: types.Message):
    with open('44.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("DoS-атака с применением протокола TCP - это атака, которая заключается в перегрузке компьютерной системы запросами на установление соединения с использованием протокола TCP. Атакующий посылает на целевую систему множество пакетов с запросами на установку соединения, но не завершает их, что приводит к исчерпанию ресурсов системы. Схематично атака может быть представлена следующим образом:\n[Атакующий компьютер] -> [Цель атаки]")
@dp.message_handler(text="45")
async def q1(message: types.Message):
    await message.answer("Аутентификация - это процесс проверки подлинности пользователя или устройства, который предоставляет доступ к защищенным ресурсам. Авторизация - это процесс установления прав пользователя или устройства на доступ к определенным ресурсам. Доказательства аутентичности могут включать логины и пароли, смарт-карты, биометрические данные и другие факторы. Формы предоставления правил доступа могут включать списки контроля доступа (ACL), ролевую модель и др. Программные средства аутентификации и авторизации могут быть реализованы в виде приложений, которые работают на серверах или устройствах пользователя.")
@dp.message_handler(text="46")
async def q1(message: types.Message):
    await message.answer("Сетевой экран - это система безопасности, которая контролирует входящий и исходящий трафик в сети. Сетевые экраны могут быть реализованы в виде программного или аппаратного обеспечения. Типы сетевых экранов включают пакетные фильтры, брандмауэры, системы предотвращения вторжений (IPS) и системы обнаружения вторжений (IDS). Основные функции сетевого экрана включают фильтрацию трафика, контроль доступа и мониторинг сетевой активности. Вспомогательные функции могут включать автоматическое обновление системы, логирование событий, оповещение об атаках и др.")
@dp.message_handler(text="47")
async def q1(message: types.Message):
    with open('47.ogg', 'rb') as audio:
        await bot.send_audio(message.chat.id, audio=audio)
    await message.answer("Прокси-сервер - это сервер, который действует как посредник между клиентом и сервером. Основные функции прокси-сервера включают кэширование, фильтрацию трафика, контроль доступа и управление полосой пропускания. Прокси-сервер может располагаться между клиентом и Интернетом (внешний прокси-сервер), между клиентом и сервером приложений (прокси-сервер приложений) или между серверами (прокси-сервер пересылки).")


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)