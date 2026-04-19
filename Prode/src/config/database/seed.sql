-- Datos de ejemplo para testing y desarrollo
-- Prode - Sistema de Predicciones de Fútbol

USE prode;

-- Limpiar datos existentes para evitar conflictos
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE rankings;
TRUNCATE TABLE predictions;
TRUNCATE TABLE fixtures;
TRUNCATE TABLE users;
SET FOREIGN_KEY_CHECKS = 1;

-- Insertar usuarios de ejemplo
INSERT INTO users (email, name, password) VALUES 
('admin@prode.com', 'Admin', 'hashed_password_123'),
('juan@prode.com', 'Juan Pérez', 'hashed_password_456'),
('maria@prode.com', 'María García', 'hashed_password_789'),
('carlos@prode.com', 'Carlos López', 'hashed_password_abc');

-- Insertar partidos de ejemplo (Mundial 2026)
INSERT INTO fixtures (local_team, visitor_team, stadium, city, date_time, phase, local_goals, visitor_goals, status) VALUES 
('Argentina', 'Marruecos', 'MetLife Stadium', 'New Jersey', '2026-06-15 18:00:00', 'Group Stage', 0, 0, 'pending'),
('Brasil', 'Croacia', 'SoFi Stadium', 'Los Angeles', '2026-06-16 15:00:00', 'Group Stage', 0, 0, 'pending'),
('España', 'Alemania', 'AT&T Stadium', 'Dallas', '2026-06-17 18:00:00', 'Group Stage', 0, 0, 'pending'),
('Francia', 'Inglaterra', 'Levi\'s Stadium', 'San Francisco', '2026-06-18 21:00:00', 'Group Stage', 0, 0, 'pending'),
('Portugal', 'Países Bajos', 'NRG Stadium', 'Houston', '2026-06-19 18:00:00', 'Group Stage', 0, 0, 'pending'),
('Italia', 'Bélgica', 'Arrowhead Stadium', 'Kansas City', '2026-06-20 15:00:00', 'Group Stage', 0, 0, 'pending');

-- Insertar predicciones de ejemplo
INSERT INTO predictions (user_id, fixture_id, predicted_local_goals, predicted_visitor_goals, points) VALUES 
-- Predicciones de admin@prode.com (id: 1)
(1, 1, 2, 1, 3),
(1, 2, 1, 1, 3),
(1, 3, 0, 1, 1),
(1, 4, 2, 0, 3),
(1, 5, 2, 0, 1),
(1, 6, 2, 1, 0),

-- Predicciones de juan@prode.com (id: 2)
(2, 1, 1, 0, 0),
(2, 2, 0, 1, 3),
(2, 3, 1, 1, 1),
(2, 4, 1, 0, 0),
(2, 5, 1, 1, 3),
(2, 6, 1, 0, 0),

-- Predicciones de maria@prode.com (id: 3)
(3, 1, 3, 0, 0),
(3, 2, 0, 0, 3),
(3, 3, 1, 2, 3),
(3, 4, 2, 1, 0),
(3, 5, 2, 1, 1),
(3, 6, 1, 0, 3),

-- Predicciones de carlos@prode.com (id: 4)
(4, 1, 2, 0, 3),
(4, 2, 1, 0, 0),
(4, 3, 0, 2, 0),
(4, 4, 1, 0, 0),
(4, 5, 1, 0, 0),
(4, 6, 0, 1, 0);

-- Actualizar rankings iniciales
INSERT INTO rankings (user_id, total_points, position, phase) 
SELECT 
    user_id,
    SUM(points) as total_points,
    ROW_NUMBER() OVER (ORDER BY SUM(points) DESC) as position,
    'General' as phase
FROM predictions 
GROUP BY user_id;
