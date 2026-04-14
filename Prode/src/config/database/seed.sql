-- Datos de ejemplo para testing y desarrollo
-- Prode - Sistema de Predicciones de Fútbol

USE prode;

-- Insertar usuarios de ejemplo
INSERT INTO users (email, password) VALUES 
('admin@prode.com', 'hashed_password_123'),
('juan@prode.com', 'hashed_password_456'),
('maria@prode.com', 'hashed_password_789'),
('carlos@prode.com', 'hashed_password_abc')
ON DUPLICATE KEY UPDATE email = email;

-- Insertar partidos de ejemplo (Copa América 2024)
INSERT INTO fixtures (local_team, visitor_team, stadium, city, date_time, phase, local_goals, visitor_goals, status) VALUES 
('Argentina', 'Canadá', 'Mercedes-Benz Stadium', 'Atlanta', '2024-06-20 20:00:00', 'Group A', 2, 0, 'finished'),
('Perú', 'Chile', 'AT&T Stadium', 'Arlington', '2024-06-21 18:00:00', 'Group A', 0, 0, 'finished'),
('Ecuador', 'Venezuela', 'Levi\'s Stadium', 'Santa Clara', '2024-06-22 18:00:00', 'Group B', 1, 2, 'finished'),
('México', 'Jamaica', 'NRG Stadium', 'Houston', '2024-06-22 21:00:00', 'Group B', 1, 0, 'finished'),
('Argentina', 'Ecuador', 'NRG Stadium', 'Houston', '2024-06-25 21:00:00', 'Quarter-Finals', 1, 1, 'finished'),
('Venezuela', 'Canadá', 'AT&T Stadium', 'Arlington', '2024-06-26 18:00:00', 'Quarter-Finals', 1, 1, 'finished')
ON DUPLICATE KEY UPDATE local_team = local_team;

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
(4, 6, 0, 1, 0)
ON DUPLICATE KEY UPDATE user_id = user_id;

-- Actualizar rankings iniciales
INSERT INTO rankings (user_id, total_points, position, phase) 
SELECT 
    user_id,
    SUM(points) as total_points,
    ROW_NUMBER() OVER (ORDER BY SUM(points) DESC) as position,
    'General' as phase
FROM predictions 
GROUP BY user_id
ON DUPLICATE KEY UPDATE 
    total_points = VALUES(total_points),
    position = VALUES(position);
