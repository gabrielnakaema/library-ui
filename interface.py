from database import Book, session, Withdrawal
import datetime


def select_all_books():
    return session.query(Book).order_by(Book.title).all()


def withdraw_book(barcode, student_name, student_grade):
    current_date = datetime.datetime.now()
    new_withdrawal = Withdrawal(book_barcode=barcode, student_name=student_name, student_grade=student_grade,
                                withdrawal_date=current_date, is_returned=False,
                                return_date=datetime.datetime.fromtimestamp(0))
    session.add(new_withdrawal)
    session.commit()


def select_all_withdrawals():
    return session.query(Withdrawal).all()


def insert_one_book(barcode, title, author, amount):
    session.execute('''
    INSERT INTO books(barcode, title, author, amount_available, amount_borrowed) VALUES(:barcode,:title,:author,
    :amount_available, 0)
        ON CONFLICT(barcode) DO UPDATE SET amount_available=amount_available+:amount_available;
    ''', {"barcode": barcode, "title": title, "author": author, "amount_available": amount})
    session.commit()

    # new_book = Book(barcode, title, author, amount)
    # session.add(new_book)
    # session.commit()


def initialize_db():
    if len(session.query(Book).all()) < 5:
        for query in queries.split(';'):
            if len(query.strip()) > 0:
                session.execute(query + ';')
        session.commit()
    else:
        pass


queries = ''' insert into books (barcode, title, author, amount_available, amount_borrowed) values ('1809a28b-a9b4-49e8-b8b0-beef6d280a00', 'nec nisi volutpat eleifend', 'Tarra Portwaine', 1, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('963770af-5007-41bc-8871-02ea6b632461', 'justo in', 'Johnette Dunsmore', 10, 6);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('6ccaf0f6-9d99-4c6d-abe1-fb32430cae47', 'fringilla', 'Alberto Aughton', 7, 4);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('d1ccdd19-48e3-4c0e-bdf2-53e20942a311', 'integer ac leo pellentesque', 'Leslie Franc', 3, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('f7a07f4c-e028-4960-a7a7-c8f4e2ea5c62', 'fusce posuere felis sed lacus', 'Mandi Milmo', 0, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('b37e4bed-52b9-4f07-8b89-5ed4f60f65b5', 'nulla ut erat', 'Durward Texton', 10, 8);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('ba1c941c-735a-425a-9e05-8a39c60e24ed', 'molestie sed justo pellentesque', 'Jackson Brugger', 10, 4);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('41570733-d105-41a9-8049-8daf01b4be7c', 'luctus et ultrices posuere', 'Teodoro Roughley', 3, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('837532e0-9d27-42ce-a7ca-83f198118f22', 'ante', 'Lazaro Faughnan', 1, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('a2536cc5-7c1f-47de-91f2-d2090a84f66f', 'tortor risus', 'Imelda Winterburn', 7, 5);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('ae33707b-612d-44bb-b379-360c068de966', 'rhoncus mauris enim leo', 'Sigvard Igglesden', 8, 3);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('d86db243-57af-41f3-896b-da90f3d10d03', 'metus aenean fermentum donec', 'Veronika Bottlestone', 2, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('b5b28554-f48f-4ce3-b134-86e47d8abcb7', 'blandit nam', 'Corissa Klos', 10, 7);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('156e0379-7a74-431a-b7de-38faed40c17b', 'ac nibh fusce lacus purus', 'Zitella Cowdrey', 6, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('488474e5-b5cd-4121-98d3-09163738b31c', 'eu orci', 'Dulsea Nanson', 2, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('82b23059-cd8a-4c10-9e6f-6c7670ee790a', 'tristique est et tempus semper', 'Lynnette Kendle', 2, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('34501628-5e39-44af-8967-44ccf323538e', 'habitasse platea dictumst maecenas ut', 'Benedikt Brood', 2, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('6e4698ad-cbad-4b17-9a94-e99186f6f684', 'felis ut at', 'Gwenny Pudner', 8, 3);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('a7ca3bb5-aa0c-4da1-ae1d-559746a57177', 'nisl', 'Duffie Corry', 2, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('37cf33b6-85f4-448e-a384-40a019c1990a', 'posuere cubilia curae', 'Otha Ornells', 3, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('cb942bc8-5dae-426f-be65-15e504bb4d2d', 'eget elit sodales scelerisque mauris', 'Ania Becarra', 10, 3);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('91dc649d-c7cd-4062-ba70-22e5db674ef9', 'convallis eget', 'Verney Aubery', 0, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('bc477902-9bf8-4929-bbe2-bfe6995cd849', 'eros suspendisse', 'Nap Trusdale', 9, 7);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('c2e9c5c9-29a6-4fe6-bd1b-d807dda79f30', 'aliquam convallis nunc', 'Madelina McKimmey', 3, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('55c24d9a-c0a1-4440-976a-5e7fe21071d7', 'amet lobortis', 'Faber Granville', 0, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('d1e3955b-a10f-42b3-a3c1-cbe6205bfff7', 'luctus', 'Benni Thomtson', 7, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('9ed95125-2f4d-4467-a70c-85792faf4e29', 'ipsum primis in faucibus orci', 'Douglas Kobieriecki', 7, 4);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('7b996c37-99f9-4385-8a20-8daf1d3ef730', 'eget semper rutrum nulla', 'Dasi Garton', 1, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('9de6647a-1704-4e67-8fcc-c252d8516fa0', 'imperdiet sapien urna', 'Baird Abramovitz', 2, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('0ebf6c35-2909-45be-8a55-551ab7ba3a2d', 'mauris viverra diam', 'Northrop Petranek', 2, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('af3b236e-4ac6-406f-845c-daed41bc7238', 'lorem', 'Olia Joules', 2, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('b26f58bd-5a56-4f4c-8193-f4895253e05b', 'ipsum primis in faucibus', 'Leticia McDougall', 6, 3);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('af443514-a469-4056-9d98-1b15667b12e1', 'leo odio', 'Marnia Frowing', 9, 7);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('e08efd9b-97bc-4b77-a6fa-3c6695b704af', 'vivamus in felis eu sapien', 'Riva Larderot', 7, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('6c6c0e12-0aa1-471c-b566-f3e8204c1e06', 'erat quisque erat', 'Josiah Pogosian', 5, 3);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('81b52be0-abfe-4fd5-a2a0-f0e0c925a026', 'quis', 'Adan Trobey', 1, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('f269a13c-a781-49a6-a607-a5487367324a', 'eu', 'Helene Kelshaw', 4, 3);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('ab480a56-931f-4624-9cc3-605e4137b55c', 'turpis sed', 'Rozelle Bunney', 2, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('7fa7f042-9b00-40ce-a1c8-558963b2f106', 'non lectus aliquam sit', 'Constancia Pringell', 1, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('11a66c05-a3d1-41eb-8b69-03339908dec2', 'ipsum', 'Milo Romeo', 3, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('3eb81f51-927f-46f0-a762-013285e9bbb4', 'ridiculus mus', 'Sumner Tirte', 6, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('b051fbd9-63dd-4ce4-a68e-2fafe096614b', 'dolor morbi', 'Liana Broune', 4, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('f378299f-fe05-481e-95b2-ed08422f9266', 'et ultrices posuere cubilia curae', 'Barclay Mattiazzo', 9, 9);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('abfac0b1-df11-4ded-b5ae-881bded2d366', 'faucibus cursus urna', 'Berte Branthwaite', 4, 4);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('ebeefb0d-4372-463d-a6ff-3c39464dbad3', 'mollis molestie lorem', 'Kara Gallemore', 4, 3);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('ce27e4b1-b7e8-4354-8f6d-32924aeb002f', 'risus praesent lectus vestibulum quam', 'Correy Agutter', 3, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('dddb670e-cd5d-438a-8539-368af75656dc', 'pulvinar sed nisl', 'Merralee Warin', 6, 6);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('3137f3fc-d2c3-4279-9571-d2dc1397f1d2', 'ultrices', 'Tedman Foster-Smith', 10, 4);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('6343d9a1-0e92-49bd-b7ab-e8aa4ad69541', 'ac', 'Robena Giovannacci', 1, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('110ef6d5-b29d-43a8-bd71-e74f5acf28d7', 'dui', 'Glenine Skinn', 3, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('8c97c627-58df-435a-a2e6-525e76f538bd', 'ante', 'Dee Scamerdine', 3, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('0cda5695-12e8-483b-8549-f2d25d39e66a', 'quam pede lobortis ligula sit', 'Patrizia Venour', 2, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('b42a2e0f-f61c-41fc-9d6f-2edf6cbf7267', 'sagittis', 'Ric Lathaye', 10, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('7412a16f-d441-455c-8862-781d11162827', 'nibh quisque id', 'Sabina Van Haeften', 2, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('841d7c44-050a-43e3-b6e0-0d66be82fadd', 'odio justo sollicitudin ut', 'Sherman Izakof', 10, 9);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('54e48c55-8999-4d31-bf89-b975020bfc78', 'erat nulla tempus vivamus in', 'Tera Riha', 2, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('398019f6-416f-40c9-ace8-f85559e0bf4b', 'tempus vel', 'Veda Stobo', 8, 7);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('2dff9b71-c4fe-4cb6-a0be-ec8cc0715adc', 'feugiat et eros vestibulum', 'Yance Tissington', 0, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('e0dad7d8-09c7-49ac-86d2-f1b354f3578b', 'arcu sed augue aliquam', 'Minni Dono', 7, 6);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('74b00b3d-6ab2-44ed-bc43-6f5a8f4c27d6', 'orci luctus', 'Ninnetta Fewell', 9, 8);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('107e99f1-5fb8-406c-820b-3328ef61f42d', 'hac habitasse platea', 'Bertie Russel', 3, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('6a49ea1c-00e0-4ada-ab67-02279aeff067', 'aliquet pulvinar sed', 'Hillard Stathor', 6, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('ff9d0553-a48b-4c4b-ae36-b5aa4a12b08f', 'justo', 'Dusty Ellington', 1, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('7338c91b-d959-46f0-85d9-1c0552a77674', 'lectus pellentesque at nulla suspendisse', 'Dannel Christofor', 7, 3);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('23b57b6f-8c91-4363-ad96-7a73db5d071b', 'turpis eget elit sodales scelerisque', 'Teddie Schoular', 5, 4);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('7610665a-9212-4d7e-a40c-5c8af147e2ab', 'praesent id massa id', 'Aymer Simonsson', 10, 10);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('d1485f2c-f207-41de-8199-f0ea2eb90ad0', 'id', 'Averil Winsley', 0, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('8ca0ac4c-caa9-4026-960a-80b01ec4dce4', 'dictumst etiam faucibus cursus urna', 'Annabal Ourtic', 0, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('1e037428-cf55-478c-8198-a253d3eb3f4b', 'luctus', 'Wood Clendening', 0, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('81fb2863-f956-4cef-afca-98aff160ab57', 'et', 'Ileana Inglesant', 5, 4);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('bc2fa656-d754-44d7-b7f2-12c9ae61b289', 'potenti nullam', 'Gael Tatem', 4, 3);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('7aa2cc33-41d9-4df4-ae98-34f5309301f5', 'duis mattis', 'Marylynne Demangeot', 6, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('d02db922-dbbc-41cf-94d4-81e23836954e', 'diam neque vestibulum', 'Ferdinande Dix', 10, 7);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('37557674-4cb1-46e5-a916-b47eb85e671c', 'in quam', 'Kassandra Sidden', 6, 4);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('7bc7c0f5-cb80-4b72-b854-1786d9541dd4', 'dui luctus rutrum nulla tellus', 'Danya Boughtwood', 8, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('4ee0cbe8-b25a-448d-bf5d-f2df7ef4e205', 'sit', 'Ysabel Pennick', 10, 5);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('36e5db3e-4134-4e63-8adb-8c2eece3d768', 'et ultrices posuere cubilia curae', 'Cornie Wraight', 2, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('3f72af3c-521e-422e-b7be-88f25fb5c1bd', 'dui vel sem', 'Kiel Roslen', 5, 3);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('5bc1b089-bfd4-4862-a772-c805ede96026', 'vestibulum ante ipsum primis', 'Brittni Melior', 8, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('71fc7a64-20fe-4118-817d-337e6db839bd', 'luctus et ultrices', 'Briny McQuilliam', 7, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('2ae86e5f-41e0-418d-9161-e15b8ff4b20f', 'eu tincidunt', 'Sari Pendrey', 6, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('7177212a-4467-451e-bbc1-12d8bd86b1bf', 'vestibulum proin eu mi', 'Miguelita Branwhite', 4, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('bc5d013a-c559-4653-b3a4-c9a9cab052b6', 'volutpat in', 'Riccardo Fitzhenry', 3, 2);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('f7096421-11d4-4483-b175-56a98fa8a9dc', 'platea', 'Sophie Manthorpe', 7, 6);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('59e9436e-e9b2-489e-9f5f-6947d7789f7b', 'felis sed', 'Welbie Speir', 9, 9);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('36e09ccf-6da9-4a4f-9ac7-9fc06635c656', 'etiam justo etiam', 'Daloris Croxon', 6, 6);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('d536296a-e3da-4a7c-a85a-9186e8392521', 'eget elit sodales scelerisque mauris', 'Faun Shepard', 7, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('00cb3791-fcc7-4f3d-88bf-b958ad488824', 'vulputate nonummy maecenas tincidunt', 'Rica Ganley', 8, 6);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('51383047-6940-4161-a259-02878f49c42c', 'libero nullam sit amet', 'Liesa Blencowe', 10, 4);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('259408b6-9b66-4d41-bc43-5e05dfb53041', 'tellus nisi eu', 'Trey Florentine', 6, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('0d53dc3f-0041-4191-a182-cceef0d854c2', 'curabitur at', 'Ardath Gilson', 1, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('afb93799-c4ab-4c47-9024-09ab35fa7573', 'in hac habitasse platea dictumst', 'Genvieve Lomas', 7, 6);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('aa7e0388-aa15-4cf5-8ab2-11853e784f04', 'sapien dignissim vestibulum', 'Portia Corroyer', 10, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('06bcfd85-dba5-484d-b5c0-1ebf7814a26e', 'etiam vel', 'Burr Attree', 8, 4);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('3780bcd5-4150-4683-b50b-28202fee3b2b', 'pede libero', 'Anthea Klimas', 1, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('d257f374-d992-4cb2-8f8a-3e4e992061d8', 'mattis pulvinar', 'Brockie Jago', 7, 1);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('4d4a93ff-ac2d-4241-b494-7063cd895bc2', 'eu est congue elementum in', 'Fernando Dudeney', 3, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('9341c826-7d8d-409d-936d-24ba5b9b8e2c', 'erat quisque erat', 'Sarah Nannini', 9, 5);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('38b7c193-f8c4-40e4-a4c7-95dcd94bb9b3', 'proin at', 'Klarika Bolzen', 0, 0);
insert into books (barcode, title, author, amount_available, amount_borrowed) values ('a14569ac-6f88-4422-a5a0-092ad16c23a6', 'massa donec dapibus duis', 'Corry Vasyukhin', 10, 6);
'''