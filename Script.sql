-- ==========================================
-- 1. ОЧИСТКА (Видаляємо старі таблиці, якщо є)
-- ==========================================
-- Спочатку видаляємо бронювання, бо вони залежать від кімнат
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS rooms;

-- ==========================================
-- 2. СТВОРЕННЯ ТАБЛИЦІ КІМНАТ (rooms)
-- ==========================================
CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,          -- Унікальний ID
    number VARCHAR(10) NOT NULL,    -- Номер ("101", "Lux-1")
    price DECIMAL(10, 2) NOT NULL,  -- Ціна
    capacity INT DEFAULT 1,         -- Місткість
    is_active BOOLEAN DEFAULT TRUE  -- Статус
);

-- ==========================================
-- 3. НАПОВНЕННЯ ДАНИМИ (rooms)
-- ==========================================
INSERT INTO rooms (number, price, capacity) 
VALUES 
    ('101', 150.00, 2),
    ('102', 250.00, 4),  -- Додали ще сімейний номер
    ('201', 500.00, 2);  -- Додали люкс

-- ==========================================
-- 4. СТВОРЕННЯ ТАБЛИЦІ БРОНЮВАНЬ (bookings)
-- ==========================================
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    room_id INT REFERENCES rooms(id), -- <== ЗВ'ЯЗОК (Foreign Key)
    guest_name VARCHAR(100),
    check_in DATE NOT NULL,
    check_out DATE NOT NULL
);

-- ==========================================
-- 5. НАПОВНЕННЯ ДАНИМИ (bookings)
-- ==========================================
-- Бронюємо кімнату з id=1 (це номер 101) для Михайла
INSERT INTO bookings (room_id, guest_name, check_in, check_out)
VALUES (1, 'Михайло', '2026-01-10', '2026-01-15');

-- Бронюємо кімнату з id=3 (це номер 201) для Ілона Маска
INSERT INTO bookings (room_id, guest_name, check_in, check_out)
VALUES (3, 'Elon Musk', '2026-02-01', '2026-02-05');

-- ==========================================
-- 6. ПЕРЕВІРКА (JOIN)
-- ==========================================
-- Виводимо красиву таблицю: Хто, в якому номері і за скільки живе
SELECT 
    r.number AS room_number, 
    r.price, 
    b.guest_name, 
    b.check_in,
    b.check_out
FROM rooms r
JOIN bookings b ON r.id = b.room_id;