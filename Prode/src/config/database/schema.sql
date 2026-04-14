CREATE DATABASE IF NOT EXISTS prode CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


USE prode;


CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE IF NOT EXISTS fixtures (
    id INT AUTO_INCREMENT PRIMARY KEY,
    local_team VARCHAR(100) NOT NULL,
    visitor_team VARCHAR(100) NOT NULL,
    stadium VARCHAR(100),
    city VARCHAR(100),
    date_time DATETIME NOT NULL,
    local_goals INT DEFAULT 0,
    visitor_goals INT DEFAULT 0,
    phase VARCHAR(50) NOT NULL,
    status ENUM('pending', 'in_progress', 'finished') DEFAULT 'pending',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE IF NOT EXISTS predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    fixture_id INT NOT NULL,
    predicted_local_goals INT NOT NULL DEFAULT 0,
    predicted_visitor_goals INT NOT NULL DEFAULT 0,
    points INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (fixture_id) REFERENCES fixtures(id) ON DELETE CASCADE,
    
    UNIQUE KEY unique_user_fixture (user_id, fixture_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE IF NOT EXISTS rankings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_points INT DEFAULT 0,
    position INT DEFAULT 0,
    phase VARCHAR(50),
    calculated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    
    UNIQUE KEY unique_user_phase (user_id, phase)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


