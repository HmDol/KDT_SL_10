-- ===================================================
-- 팀원 4명 계정에 권한 부여 
-- ProjectDB : 팀의 Database이름으로 변경
-- ===================================================


GRANT ALL PRIVILEGES ON ProjectDB.* TO 'user1'@'172.30.1.66';
GRANT ALL PRIVILEGES ON ProjectDB.* TO 'user2'@'172.30.1.58';
GRANT ALL PRIVILEGES ON ProjectDB.* TO 'user3'@'172.30.1.99';
-- GRANT ALL PRIVILEGES ON ProjectDB.* TO 'user4'@'203.0.113.13';

FLUSH PRIVILEGES;


-- GRANT ALL PRIVILEGES ON ProjectDB.* TO 'user1'@'%';
-- GRANT ALL PRIVILEGES ON ProjectDB.* TO 'user2'@'%';
-- GRANT ALL PRIVILEGES ON ProjectDB.* TO 'user3'@'%';
-- GRANT ALL PRIVILEGES ON ProjectDB.* TO 'user4'@'%';

-- FLUSH PRIVILEGES;
